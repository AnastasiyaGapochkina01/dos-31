resource "aws_internet_gateway" "demo-igw" {
  vpc_id = aws_vpc.demo.id

  tags = {
    Name = "demo-igw"
  }
}

resource "aws_eip" "demo-nat-ip" {
  domain = "vpc"

  tags = {
    Name = "demo-nat-ip"
  }
}

resource "aws_nat_gateway" "demo-ngw" {
#  vpc_id = aws_vpc.demo.id

  subnet_id     = aws_subnet.public-a.id
  allocation_id = aws_eip.demo-nat-ip.id

  tags = {
    Name = "demo-ngw"
  }

  depends_on = [aws_internet_gateway.demo-igw]
}