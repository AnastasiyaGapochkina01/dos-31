package models

import "database/sql"

type User struct {
    ID         int
    Username   string
    Password   string
    TelegramID string
}

func CreateUser(user *User) error {
    _, err := db.Exec("INSERT INTO users (username, password, telegram_id) VALUES ($1, $2, $3)",
        user.Username, user.Password, user.TelegramID)
    return err
}

func GetUserByUsername(username string) (User, error) {
    var user User
    err := db.QueryRow("SELECT id, username, password, telegram_id FROM users WHERE username = $1", username).
        Scan(&user.ID, &user.Username, &user.Password, &user.TelegramID)
    return user, err
}

func GetUserByID(id int) (User, error) {
    var user User
    err := db.QueryRow("SELECT id, username, password, telegram_id FROM users WHERE id = $1", id).
        Scan(&user.ID, &user.Username, &user.Password, &user.TelegramID)
    return user, err
}

var db *sql.DB

func SetDB(database *sql.DB) {
    db = database
}