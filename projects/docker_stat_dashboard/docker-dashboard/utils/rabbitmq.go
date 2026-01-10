package utils

import (
    "log"

    "github.com/streadway/amqp"
)

var RabbitMQConn *amqp.Connection
var RabbitMQChannel *amqp.Channel

func InitRabbitMQ() {
    var err error
    RabbitMQConn, err = amqp.Dial("amqp://user:password@rabbitmq:5672/")
    if err != nil {
        log.Fatal(err)
    }
    
    RabbitMQChannel, err = RabbitMQConn.Channel()
    if err != nil {
        log.Fatal(err)
    }
    
    _, err = RabbitMQChannel.QueueDeclare(
        "report_queue", // name
        true,           // durable
        false,          // delete when unused
        false,          // exclusive
        false,          // no-wait
        nil,            // arguments
    )
    if err != nil {
        log.Fatal(err)
    }
}