package main

import (
    "log"
    "docker-dashboard/handlers"
    "docker-dashboard/utils"

    "github.com/gin-gonic/gin"
)

func main() {
    r := gin.Default()
    
    // Initialize database
    utils.InitDB()
    
    // Initialize RabbitMQ
    utils.InitRabbitMQ()
    
    // Load templates and static files
    r.LoadHTMLGlob("templates/*")
    r.Static("/static", "./static")
    
    // Routes
    r.GET("/", handlers.IndexHandler)
    r.GET("/login", handlers.LoginPageHandler)
    r.POST("/login", handlers.LoginHandler)
    r.GET("/register", handlers.RegisterPageHandler)
    r.POST("/register", handlers.RegisterHandler)
    
    // Protected routes
    authorized := r.Group("/")
    authorized.Use(handlers.AuthMiddleware())
    {
        authorized.GET("/dashboard", handlers.DashboardHandler)
        authorized.GET("/dashboard/data", handlers.DashboardDataHandler)
        authorized.GET("/container/:id", handlers.ContainerHandler)
        authorized.POST("/report", handlers.GenerateReportHandler)
        authorized.GET("/events", handlers.SSEHandler)
    }
    
    r.GET("/logout", handlers.LogoutHandler)
    
    log.Fatal(r.Run(":8080"))
}