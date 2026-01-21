package main

import (
	"context"
	"database/sql"
	"encoding/json"
	"log"
	"net/http"
	"os"
	"strconv"
	"time"

	"github.com/rs/cors"
)

type Server struct {
	db *sql.DB
}

func main() {
	db, err := openDB()
	if err != nil {
		log.Fatalf("db open error: %v", err)
	}
	if err := migrate(db); err != nil {
		log.Fatalf("db migrate error: %v", err)
	}

	s := &Server{db: db}

	mux := http.NewServeMux()
        mux.HandleFunc("/api/notes", s.handleNotes)
        mux.HandleFunc("/api/notes/", s.handleNotes)
        mux.HandleFunc("/api/notes/", s.handleNoteByID)

	handler := cors.New(cors.Options{
		AllowedOrigins:   []string{"*"},
		AllowedMethods:   []string{"GET", "POST", "PUT", "DELETE", "OPTIONS"},
		AllowedHeaders:   []string{"Content-Type", "Accept"},
		AllowCredentials: true,
                OptionsSuccessStatus: 204,
	}).Handler(mux)

	port := os.Getenv("APP_PORT")
	if port == "" {
		port = "8080"
	}

	log.Printf("listening on :%s", port)
	if err := http.ListenAndServe(":"+port, handler); err != nil {
		log.Fatalf("server error: %v", err)
	}
}

func (s *Server) handleNotes(w http.ResponseWriter, r *http.Request) {
	switch r.Method {
	case http.MethodGet:
		s.listNotes(w, r)
	case http.MethodPost:
		s.createNote(w, r)
	default:
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
	}
}

func (s *Server) handleNoteByID(w http.ResponseWriter, r *http.Request) {
	idStr := r.URL.Path[len("/api/notes/"):]
	id, err := strconv.ParseInt(idStr, 10, 64)
	if err != nil {
		http.Error(w, "invalid id", http.StatusBadRequest)
		return
	}

	switch r.Method {
	case http.MethodGet:
		s.getNote(w, r, id)
	case http.MethodPut:
		s.updateNote(w, r, id)
	case http.MethodDelete:
		s.deleteNote(w, r, id)
	default:
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
	}
}

func (s *Server) listNotes(w http.ResponseWriter, r *http.Request) {
	rows, err := s.db.Query(`
		SELECT id, title, content, reminder_at, is_completed, created_at, updated_at
		FROM notes
		ORDER BY created_at DESC`)
	if err != nil {
		http.Error(w, "db error", http.StatusInternalServerError)
		return
	}
	defer rows.Close()

	var notes []Note
	for rows.Next() {
		var n Note
		var reminderAt sql.NullTime
		if err := rows.Scan(&n.ID, &n.Title, &n.Content, &reminderAt, &n.IsCompleted, &n.CreatedAt, &n.UpdatedAt); err != nil {
			http.Error(w, "scan error", http.StatusInternalServerError)
			return
		}
		if reminderAt.Valid {
			t := reminderAt.Time
			n.ReminderAt = &t
		}
		notes = append(notes, n)
	}
	writeJSON(w, http.StatusOK, notes)
}

func (s *Server) createNote(w http.ResponseWriter, r *http.Request) {
	var payload struct {
		Title      string `json:"title"`
		Content    string `json:"content"`
		ReminderAt string `json:"reminder_at"`
	}
	if err := json.NewDecoder(r.Body).Decode(&payload); err != nil {
		http.Error(w, "bad json", http.StatusBadRequest)
		return
	}
	if payload.Title == "" {
		http.Error(w, "title required", http.StatusBadRequest)
		return
	}

	var reminder *time.Time
	if payload.ReminderAt != "" {
		t, err := time.Parse(time.RFC3339, payload.ReminderAt)
		if err != nil {
			http.Error(w, "invalid reminder_at", http.StatusBadRequest)
			return
		}
		reminder = &t
	}

	ctx, cancel := context.WithTimeout(r.Context(), 5*time.Second)
	defer cancel()

	var id int64
	query := `
		INSERT INTO notes (title, content, reminder_at)
		VALUES ($1, $2, $3)
		RETURNING id`
	if err := s.db.QueryRowContext(ctx, query, payload.Title, payload.Content, reminder).Scan(&id); err != nil {
		http.Error(w, "insert error", http.StatusInternalServerError)
		return
	}

	s.getNote(w, r, id)
}

func (s *Server) getNote(w http.ResponseWriter, r *http.Request, id int64) {
	var n Note
	var reminderAt sql.NullTime
	query := `
		SELECT id, title, content, reminder_at, is_completed, created_at, updated_at
		FROM notes WHERE id = $1`
	err := s.db.QueryRow(query, id).
		Scan(&n.ID, &n.Title, &n.Content, &reminderAt, &n.IsCompleted, &n.CreatedAt, &n.UpdatedAt)
	if err == sql.ErrNoRows {
		http.Error(w, "not found", http.StatusNotFound)
		return
	}
	if err != nil {
		http.Error(w, "db error", http.StatusInternalServerError)
		return
	}
	if reminderAt.Valid {
		t := reminderAt.Time
		n.ReminderAt = &t
	}
	writeJSON(w, http.StatusOK, n)
}

func (s *Server) updateNote(w http.ResponseWriter, r *http.Request, id int64) {
	var payload struct {
		Title       *string `json:"title"`
		Content     *string `json:"content"`
		ReminderAt  *string `json:"reminder_at"`
		IsCompleted *bool   `json:"is_completed"`
	}
	if err := json.NewDecoder(r.Body).Decode(&payload); err != nil {
		http.Error(w, "bad json", http.StatusBadRequest)
		return
	}

	var reminder *time.Time
	if payload.ReminderAt != nil {
		if *payload.ReminderAt == "" {
			reminder = nil
		} else {
			t, err := time.Parse(time.RFC3339, *payload.ReminderAt)
			if err != nil {
				http.Error(w, "invalid reminder_at", http.StatusBadRequest)
				return
			}
			reminder = &t
		}
	}

	ctx, cancel := context.WithTimeout(r.Context(), 5*time.Second)
	defer cancel()

	query := `
UPDATE notes
SET title = COALESCE($1, title),
    content = COALESCE($2, content),
    reminder_at = COALESCE($3, reminder_at),
    is_completed = COALESCE($4, is_completed)
WHERE id = $5
RETURNING id`
	var retID int64
	err := s.db.QueryRowContext(ctx, query,
		payload.Title, payload.Content, reminder, payload.IsCompleted, id,
	).Scan(&retID)
	if err == sql.ErrNoRows {
		http.Error(w, "not found", http.StatusNotFound)
		return
	}
	if err != nil {
		http.Error(w, "update error", http.StatusInternalServerError)
		return
	}

	s.getNote(w, r, id)
}

func (s *Server) deleteNote(w http.ResponseWriter, r *http.Request, id int64) {
	ctx, cancel := context.WithTimeout(r.Context(), 5*time.Second)
	defer cancel()

	res, err := s.db.ExecContext(ctx, `DELETE FROM notes WHERE id = $1`, id)
	if err != nil {
		http.Error(w, "delete error", http.StatusInternalServerError)
		return
	}
	affected, _ := res.RowsAffected()
	if affected == 0 {
		http.Error(w, "not found", http.StatusNotFound)
		return
	}
	w.WriteHeader(http.StatusNoContent)
}

func writeJSON(w http.ResponseWriter, status int, v any) {
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(status)
	_ = json.NewEncoder(w).Encode(v)
}

