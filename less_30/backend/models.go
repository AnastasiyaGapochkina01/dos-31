package main

import "time"

type Note struct {
	ID          int64      `json:"id"`
	Title       string     `json:"title"`
	Content     string     `json:"content"`
	ReminderAt  *time.Time `json:"reminder_at,omitempty"`
	CreatedAt   time.Time  `json:"created_at"`
	UpdatedAt   time.Time  `json:"updated_at"`
	IsCompleted bool       `json:"is_completed"`
}

