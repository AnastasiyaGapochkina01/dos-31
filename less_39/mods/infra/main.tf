resource "aws_vpc" "vpc-1" {
  cidr_block = var.vpc_ips
  tags = {
    Name = "vpc-${var.env}"
  }
}

resource "aws_subnet" "subnet-1" {
  vpc_id = aws_vpc.vpc-1.id
  cidr_block = var.subnet_ips
  availability_zone = var.az
  tags = {
    Name = "subnet-${var.env}"
  }
}

resource "aws_instance" "server" {
  ami = var.ami_id
  instance_type = var.instance-type
  subnet_id = aws_subnet.subnet-1.id

  tags = {
    Name = "server-${var.env}"
    Env = var.env
  }
}
