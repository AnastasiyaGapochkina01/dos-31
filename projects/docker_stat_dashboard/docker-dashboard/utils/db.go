package utils

import (
    "database/sql"
    "docker-dashboard/models"
    _ "github.com/lib/pq"
    "log"
)

var DB *sql.DB

func InitDB() {
    var err error
    DB, err = sql.Open("postgres", "user=user password=password dbname=docker_dashboard host=db sslmode=disable")
    if err != nil {
        log.Fatal(err)
    }
    
    // Create users table if not exists
    createTable := `
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL,
        password VARCHAR(255) NOT NULL,
        telegram_id VARCHAR(50)
    );
    `
    _, err = DB.Exec(createTable)
    if err != nil {
        log.Fatal(err)
    }
    
    models.SetDB(DB)
}