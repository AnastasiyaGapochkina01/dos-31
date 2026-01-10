package rabbitmq

import (
	"log"
	"os"

	"github.com/streadway/amqp"
)

type Rabbit struct {
	conn    *amqp.Connection
	channel *amqp.Channel
}

func NewRabbit() *Rabbit {
	url := os.Getenv("RABBITMQ_URL")
	if url == "" {
		url = "amqp://guest:guest@rabbitmq:5672/"
	}
	conn, err := amqp.Dial(url)
	if err != nil {
		log.Fatal("RabbitMQ connection error:", err)
	}

	ch, err := conn.Channel()
	if err != nil {
		log.Fatal("RabbitMQ channel error:", err)
	}

	ch.QueueDeclare("order-status", true, false, false, false, nil)

	return &Rabbit{conn: conn, channel: ch}
}

func (r *Rabbit) PublishStatus(id, status string) {
	body := id + ":" + status
	r.channel.Publish(
		"", "order-status", false, false,
		amqp.Publishing{
			ContentType: "text/plain",
			Body:        []byte(body),
		},
	)
}
