package handlers

import (
    "net/http"
    "docker-dashboard/utils"
    "docker-dashboard/models"

    "github.com/gin-gonic/gin"
    "golang.org/x/crypto/bcrypt"
)

func IndexHandler(c *gin.Context) {
    c.HTML(http.StatusOK, "index.html", nil)
}

func LoginPageHandler(c *gin.Context) {
    c.HTML(http.StatusOK, "login.html", nil)
}

func LoginHandler(c *gin.Context) {
    username := c.PostForm("username")
    password := c.PostForm("password")
    
    user, err := models.GetUserByUsername(username)
    if err != nil {
        c.HTML(http.StatusBadRequest, "login.html", gin.H{"error": "Invalid credentials"})
        return
    }
    
    if err := bcrypt.CompareHashAndPassword([]byte(user.Password), []byte(password)); err != nil {
        c.HTML(http.StatusBadRequest, "login.html", gin.H{"error": "Invalid credentials"})
        return
    }
    
    // Set session
    utils.SetSession(c, user.ID)
    
    c.Redirect(http.StatusFound, "/dashboard")
}

func RegisterPageHandler(c *gin.Context) {
    c.HTML(http.StatusOK, "register.html", nil)
}

func RegisterHandler(c *gin.Context) {
    username := c.PostForm("username")
    password := c.PostForm("password")
    telegramID := c.PostForm("telegram_id")
    
    hashedPassword, _ := bcrypt.GenerateFromPassword([]byte(password), bcrypt.DefaultCost)
    
    user := models.User{
        Username: username,
        Password: string(hashedPassword),
        TelegramID: telegramID,
    }
    
    if err := models.CreateUser(&user); err != nil {
        c.HTML(http.StatusBadRequest, "register.html", gin.H{"error": "User already exists"})
        return
    }
    
    c.Redirect(http.StatusFound, "/login")
}

func LogoutHandler(c *gin.Context) {
    utils.ClearSession(c)
    c.Redirect(http.StatusFound, "/")
}