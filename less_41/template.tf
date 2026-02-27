data "aws_ami" "ubuntu" {
  most_recent = true

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd-gp3/ubuntu-noble-24.04-amd64-server-*"]
  }

  owners = ["099720109477"]
}


resource "aws_launch_template" "demo-lt" {
  name_prefix   = "demo-asg-"
  image_id      = data.aws_ami.ubuntu.id
  instance_type = "t3.micro"

  vpc_security_group_ids = [aws_security_group.ec2-sg.id]
  user_data              = filebase64("scripts/init.sh")

  tag_specifications {
    resource_type = "instance"

    tags = {
      Name = "vm"
    }
  }

}