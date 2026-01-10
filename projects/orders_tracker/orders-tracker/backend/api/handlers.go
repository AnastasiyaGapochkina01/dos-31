package api

import (
	"backend/model"
	"backend/postgres"
	"backend/rabbitmq"
	"encoding/json"
	"net/http"
	"log"
	"html/template"
)

func LoginHandler(db *postgres.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		if r.Method == http.MethodGet {
			http.ServeFile(w, r, "./static/login.html")
			return
		}
		r.ParseForm()
		user := r.FormValue("username")
		pass := r.FormValue("password")
		if db.CheckUser(user, pass) {
			SetSession(w, user)
			http.Redirect(w, r, "/admin", http.StatusFound)
			return
		}
		http.Error(w, "Invalid login", http.StatusUnauthorized)
	}
}

func LogoutHandler() http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		ClearSession(w)
		http.Redirect(w, r, "/login", http.StatusFound)
	}
}

func AdminHandler(db *postgres.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		if !IsLoggedIn(r) {
			http.Redirect(w, r, "/login", http.StatusFound)
			return
		}
		http.ServeFile(w, r, "./static/admin.html")
	}
}

func OrdersHandler(db *postgres.DB, rmq *rabbitmq.Rabbit) http.HandlerFunc {
    return func(w http.ResponseWriter, r *http.Request) {
        switch r.Method {
        case http.MethodGet:
            orders, err := db.GetAllOrders()
            if err != nil {
                http.Error(w, "Could not fetch orders", http.StatusInternalServerError)
                return
            }
            w.Header().Set("Content-Type", "application/json")
            json.NewEncoder(w).Encode(orders)
        case http.MethodPost:
            var order model.Order
            if err := json.NewDecoder(r.Body).Decode(&order); err != nil {
                http.Error(w, "Invalid JSON", http.StatusBadRequest)
                return
            }
            if order.ID == "" {
                http.Error(w, "Order ID required", http.StatusBadRequest)
                return
            }
            if order.Name == "" {
                http.Error(w, "Order name required", http.StatusBadRequest)
                return
            }
            if err := db.CreateOrder(&order); err != nil {
    			log.Printf("Error creating order: %v\n", err)
    			http.Error(w, "Failed to add order", http.StatusInternalServerError)
    			return
			}
            rmq.PublishStatus(order.ID, "created")
            w.WriteHeader(http.StatusCreated)
        default:
            http.Error(w, "Method not allowed", http.StatusMethodNotAllowed)
        }
    }
}

func UpdateStatusHandler(db *postgres.DB, rmq *rabbitmq.Rabbit) http.HandlerFunc {
    return func(w http.ResponseWriter, r *http.Request) {
        if r.Method != http.MethodPost {
            http.Error(w, "Method not allowed", http.StatusMethodNotAllowed)
            return
        }
        err := r.ParseForm()
        if err != nil {
            http.Error(w, "Failed to parse form", http.StatusBadRequest)
            return
        }
        id := r.FormValue("order_id")
        status := r.FormValue("status")
        if id == "" || status == "" {
            http.Error(w, "Missing order_id or status", http.StatusBadRequest)
            return
        }

        err = db.ChangeOrderStatus(id, status)
        if err != nil {
            http.Error(w, "Failed to update status", http.StatusInternalServerError)
            return
        }
        rmq.PublishStatus(id, status)
        http.Redirect(w, r, "/admin", http.StatusSeeOther)
    }
}

func OrderStatusViewHandler(db *postgres.DB) http.HandlerFunc {
    return func(w http.ResponseWriter, r *http.Request) {
        if r.Method != http.MethodGet {
            http.Error(w, "Method not allowed", http.StatusMethodNotAllowed)
            return
        }
        orders, err := db.GetAllOrders()
        if err != nil {
            http.Error(w, "Failed to load orders", http.StatusInternalServerError)
            return
        }
        
        tmpl, err := template.ParseFiles("./static/order_status.html")
        if err != nil {
            log.Println("Error parsing template:", err)
            http.Error(w, "Internal server error", http.StatusInternalServerError)
            return
        }
        
        err = tmpl.Execute(w, orders)
        if err != nil {
            log.Println("Error executing template:", err)
            http.Error(w, "Internal server error", http.StatusInternalServerError)
            return
        }
    }
}
