package handlers

import (
    "net/http"
    "docker-dashboard/utils"

    "github.com/gin-gonic/gin"
)

func DashboardHandler(c *gin.Context) {
    containers, err := utils.GetContainers()
    if err != nil {
        c.HTML(http.StatusInternalServerError, "dashboard.html", gin.H{"error": err.Error()})
        return
    }
    
    c.HTML(http.StatusOK, "dashboard.html", gin.H{
        "containers": containers,
    })
}

func DashboardDataHandler(c *gin.Context) {
    containers, err := utils.GetContainers()
    if err != nil {
        c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
        return
    }
    
    c.JSON(http.StatusOK, gin.H{
        "containers": containers,
    })
}

func ContainerHandler(c *gin.Context) {
    containerID := c.Param("id")
    container, err := utils.GetContainer(containerID)
    if err != nil {
        c.HTML(http.StatusNotFound, "container.html", gin.H{"error": "Container not found"})
        return
    }
    
    c.HTML(http.StatusOK, "container.html", gin.H{
        "container": container,
    })
}

func GenerateReportHandler(c *gin.Context) {
    userID := utils.GetUserID(c)
    go utils.GenerateAndSendReport(userID)
    c.JSON(http.StatusOK, gin.H{"message": "Report generation started"})
}