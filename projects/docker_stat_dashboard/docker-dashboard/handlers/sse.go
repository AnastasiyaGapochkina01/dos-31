package handlers

import (
    "time"
    "docker-dashboard/utils"

    "github.com/gin-gonic/gin"
)

func SSEHandler(c *gin.Context) {
    c.Writer.Header().Set("Content-Type", "text/event-stream")
    c.Writer.Header().Set("Cache-Control", "no-cache")
    c.Writer.Header().Set("Connection", "keep-alive")
    
    ticker := time.NewTicker(2 * time.Second)
    defer ticker.Stop()
    
    for {
        select {
        case <-ticker.C:
            containers, err := utils.GetContainers()
            if err != nil {
                continue
            }
            
            c.SSEvent("containers", containers)
            c.Writer.Flush()
        case <-c.Writer.CloseNotify():
            return
        }
    }
}