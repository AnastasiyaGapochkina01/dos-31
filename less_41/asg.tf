resource "aws_autoscaling_group" "demo-asg" {
  name = "demo-asg"
  max_size = 4
  min_size = 1
  desired_capacity = 3
  vpc_zone_identifier = [
    aws_subnet.private-a.id,
    aws_subnet.private-b.id
  ]

  launch_template {
    id = aws_launch_template.demo-lt.id
    version = "$Latest"
  }

  target_group_arns = [aws_lb_target_group.demo-tg.arn]

  tag {
    key = "Name"
    value = "demo-instance"
    propagate_at_launch = true
  }

  depends_on = [aws_lb_listener.demo-http]
}