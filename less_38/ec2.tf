data "aws_ami" "ubuntu" {
  most_recent = true

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd-gp3/ubuntu-noble-24.04-amd64-server-*"]
  }

  owners = ["099720109477"]
}

resource "aws_instance" "server-2" {
  ami           = "ami-06e3c045d79fd65d9"
  instance_type = var.instance-type
  key_name      = "anestesia-main"
  monitoring    = false
  security_groups = [
    "launch-wizard-1",
  ]
  subnet_id = "subnet-0e85977bad3d55bad"
  tags = {
    "Name" = "server-2"
  }

}

resource "aws_instance" "app-server" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = var.instance-type
  key_name      = aws_key_pair.admin-key.key_name
  vpc_security_group_ids = [
    aws_security_group.app-server-sg.id
  ]

  tags = {
    Name = "tf-server-1"
    Team = "dos-31"
    Kind = "temporary"
  }
}

resource "aws_security_group" "app-server-sg" {
  name        = "tf-servers-sg"
  description = "Allow access for tf-servers"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_key_pair" "admin-key" {
  key_name   = "control-plain-key"
  public_key = file("~/.ssh/id_ed25519.pub")
}
