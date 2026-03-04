resource "aws_instance" "demo-app-vm" {
  ami           = var.default_ami
  instance_type = var.default_type

  network_interface {
    device_index         = 0
    network_interface_id = aws_network_interface.demo-app-if-1.id
  }

  tags = {
    Name = "demo-app-1"
  }
}