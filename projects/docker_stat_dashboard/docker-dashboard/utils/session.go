package utils

import (
    "github.com/gin-gonic/gin"
    "strconv"
)

const sessionName = "session"

func SetSession(c *gin.Context, userID int) {
    c.SetCookie(sessionName, strconv.Itoa(userID), 3600, "/", "", false, true)
}

func ClearSession(c *gin.Context) {
    c.SetCookie(sessionName, "", -1, "/", "", false, true)
}

func IsAuthenticated(c *gin.Context) bool {
    cookie, err := c.Cookie(sessionName)
    if err != nil {
        return false
    }
    return cookie != ""
}

func GetUserID(c *gin.Context) int {
    cookie, err := c.Cookie(sessionName)
    if err != nil {
        return 0
    }
    userID, _ := strconv.Atoi(cookie)
    return userID
}