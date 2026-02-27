resource "aws_vpc" "demo" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_support   = true
  enable_dns_hostnames = true

  tags = {
    Name = "demo"
  }
}

resource "aws_subnet" "public-a" {
  vpc_id                  = aws_vpc.demo.id
  cidr_block              = "10.0.1.0/24"
  availability_zone       = "us-east-2a"
  map_public_ip_on_launch = true

  tags = {
    Name = "demo-public-a"
  }
}

resource "aws_subnet" "public-b" {
  vpc_id                  = aws_vpc.demo.id
  cidr_block              = "10.0.2.0/24"
  availability_zone       = "us-east-2b"
  map_public_ip_on_launch = true

  tags = {
    Name = "demo-public-b"
  }
}

resource "aws_subnet" "private-a" {
  vpc_id            = aws_vpc.demo.id
  cidr_block        = "10.0.65.0/24"
  availability_zone = "us-east-2a"

  tags = {
    Name = "demo-private-a"
  }
}

resource "aws_subnet" "private-b" {
  vpc_id            = aws_vpc.demo.id
  cidr_block        = "10.0.66.0/24"
  availability_zone = "us-east-2b"

  tags = {
    Name = "demo-private-b"
  }
}