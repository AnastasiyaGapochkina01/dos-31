package main

import (
	"backend/api"
	"backend/postgres"
	"backend/rabbitmq"
	"net/http"
	"log"
)

func main() {
    db := postgres.NewDB()
    rmq := rabbitmq.NewRabbit()

    http.HandleFunc("/login", api.LoginHandler(db))
    http.HandleFunc("/logout", api.LogoutHandler())
    http.HandleFunc("/admin", api.AdminHandler(db))
    http.HandleFunc("/orders", api.OrdersHandler(db, rmq))
    http.HandleFunc("/order/status", api.UpdateStatusHandler(db, rmq))
	http.HandleFunc("/order/status/view", api.OrderStatusViewHandler(db))
	

    http.Handle("/static/", http.StripPrefix("/static/", http.FileServer(http.Dir("./static"))))

    log.Println("Server started on :8080")
    log.Fatal(http.ListenAndServe(":8080", nil))
}
