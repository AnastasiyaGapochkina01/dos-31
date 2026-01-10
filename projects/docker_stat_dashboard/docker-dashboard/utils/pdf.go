package utils

import (
    "bytes"
    "strconv"
    "docker-dashboard/models"

    "github.com/docker/docker/api/types"
    "github.com/jung-kurt/gofpdf"
)

func GeneratePDF(containers []types.Container) []byte {
    pdf := gofpdf.New("P", "mm", "A4", "")
    pdf.AddPage()
    pdf.SetFont("Arial", "B", 16)
    pdf.Cell(40, 10, "Docker Containers Report")
    pdf.Ln(20)
    
    for _, container := range containers {
        pdf.SetFont("Arial", "B", 12)
        pdf.Cell(40, 10, "Container: "+container.Names[0])
        pdf.Ln(10)
        pdf.SetFont("Arial", "", 12)
        pdf.Cell(40, 10, "Status: "+container.Status)
        pdf.Ln(10)
        pdf.Cell(40, 10, "Image: "+container.Image)
        pdf.Ln(10)
        pdf.Ln(10)
    }
    
    var buf bytes.Buffer
    pdf.Output(&buf)
    return buf.Bytes()
}

func GenerateAndSendReport(userID int) {
    user, err := models.GetUserByID(userID)
    if err != nil {
        return
    }
    
    containers, err := GetContainers()
    if err != nil {
        return
    }
    
    pdf := GeneratePDF(containers)
    chatID, _ := strconv.Atoi(user.TelegramID)
    SendTelegramMessage(chatID, pdf, "report.pdf")
}