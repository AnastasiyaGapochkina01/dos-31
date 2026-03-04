resource "aws_network_interface" "demo-app-if-1" {
  subnet_id = var.default_subnet
  tags = {
    Name = "demo-app-if-1"
  }
}