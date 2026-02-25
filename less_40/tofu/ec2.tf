resource "aws_instance" "server2" {
  ami = "ami-06e3c045d79fd65d9"
  instance_type = "t3.micro"
  subnet_id = "subnet-0e85977bad3d55bad"

  tags = {
    Name = "server2"
  }
}