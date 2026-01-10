package api

import "net/http"

func SetSession(w http.ResponseWriter, user string) {
	http.SetCookie(w, &http.Cookie{
		Name:  "session",
		Value: user,
		Path:  "/",
	})
}

func IsLoggedIn(r *http.Request) bool {
	cookie, err := r.Cookie("session")
	return err == nil && cookie.Value != ""
}

func ClearSession(w http.ResponseWriter) {
	http.SetCookie(w, &http.Cookie{
		Name:   "session",
		Value:  "",
		Path:   "/",
		MaxAge: -1,
	})
}
