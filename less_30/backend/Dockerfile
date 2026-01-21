FROM golang:1.24-alpine AS builder
WORKDIR /app
COPY . .
RUN go mod init notes
RUN go mod tidy
RUN go build -o server ./...

FROM alpine:3.20
WORKDIR /app
COPY --from=builder /app/server /app/server
CMD ["/app/server"]
