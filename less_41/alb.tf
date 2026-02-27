resource "aws_lb" "demo-alb" {
  name               = "demo-alb"
  internal           = false
  load_balancer_type = "application"
  security_groups    = [aws_security_group.alb-sg.id]
  subnets = [
    aws_subnet.public-a.id,
    aws_subnet.public-b.id
  ]
  tags = {
    Name = "demo-alb"
  }
}

resource "aws_lb_target_group" "demo-tg" {
  name        = "demo-tg"
  port        = 80
  protocol    = "HTTP"
  target_type = "instance"
  vpc_id      = aws_vpc.demo.id

  health_check {
    enabled             = true
    path                = "/"
    port                = 80
    protocol            = "HTTP"
    matcher             = "200"
    interval            = 20
    timeout             = 5
    healthy_threshold   = 3
    unhealthy_threshold = 3
  }

  tags = {
    Name = "demo-tg"
  }
}

resource "aws_lb_listener" "demo-http" {
  load_balancer_arn = aws_lb.demo-alb.arn
  port              = 80
  protocol          = "HTTP"

  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.demo-tg.id
  }
}