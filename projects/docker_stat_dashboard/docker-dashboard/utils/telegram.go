package utils

import (
    "bytes"
    "fmt"
    "io"
    "mime/multipart"
    "net/http"
    "os"
    "strconv"
)

func SendTelegramMessage(chatID int, document []byte, filename string) error {
    botToken := os.Getenv("TELEGRAM_BOT_TOKEN")
    if botToken == "" {
        return fmt.Errorf("TELEGRAM_BOT_TOKEN not set")
    }

    url := fmt.Sprintf("https://api.telegram.org/bot%s/sendDocument", botToken)

    var requestBody bytes.Buffer
    multipartWriter := multipart.NewWriter(&requestBody)

    // Add chat_id
    multipartWriter.WriteField("chat_id", strconv.Itoa(chatID))

    // Add document
    part, err := multipartWriter.CreateFormFile("document", filename)
    if err != nil {
        return err
    }
    part.Write(document)

    multipartWriter.Close()

    resp, err := http.Post(url, multipartWriter.FormDataContentType(), &requestBody)
    if err != nil {
        return err
    }
    defer resp.Body.Close()

    if resp.StatusCode != http.StatusOK {
        body, _ := io.ReadAll(resp.Body)
        return fmt.Errorf("failed to send document: %s", body)
    }

    return nil
}