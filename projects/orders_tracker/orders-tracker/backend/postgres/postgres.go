package postgres

import (
	"backend/model"
	"database/sql"
	"log"
	"os"

	_ "github.com/lib/pq"
)

type DB struct {
	db *sql.DB
}

func NewDB() *DB {
	connStr := os.Getenv("POSTGRES_DSN")
	if connStr == "" {
        log.Fatal("POSTGRES_DSN environment variable is not set")
    }
	db, err := sql.Open("postgres", connStr)
	if err != nil {
		log.Fatal("Postgres connection error:", err)
	}
	return &DB{db: db}
}

func (d *DB) CheckUser(user, pass string) bool {
	// Простейшая заглушка
	return user == "admin" && pass == "admin"
}

func (d *DB) GetAllOrders() ([]model.Order, error) {
	rows, err := d.db.Query("SELECT id, name, status FROM orders")
	if err != nil {
		return nil, err
	}
	defer rows.Close()

	var orders []model.Order
	for rows.Next() {
		var o model.Order
		if err := rows.Scan(&o.ID, &o.Name, &o.Status); err != nil {
			return nil, err
		}
		orders = append(orders, o)
	}
	return orders, nil
}

func (d *DB) CreateOrder(o *model.Order) error {
    _, err := d.db.Exec("INSERT INTO orders(id, name, status) VALUES($1, $2, $3)", o.ID, o.Name, o.Status)
    if err != nil {
        log.Printf("Error inserting order: %v\n", err)
    }
    return err
}

func (d *DB) ChangeOrderStatus(id, status string) error {
	_, err := d.db.Exec("UPDATE orders SET status=$1 WHERE id=$2", status, id)
	return err
}
