resource "aws_key_pair" "control-plain" {
  key_name   = "control-plain-ssh-key"
  public_key = var.public_key
}

resource "aws_instance" "server-2" {
  ami           = "ami-06e3c045d79fd65d9"
  instance_type = var.instance-type
  key_name      = aws_key_pair.control-plain.id
  monitoring    = false
  security_groups = [
    "launch-wizard-1",
  ]
  subnet_id = "subnet-0e85977bad3d55bad"
  tags = {
    "Name" = "target-server"
  }

  connection {
    type        = "ssh"
    user        = "ubuntu"
    private_key = file("~/aws/.ssh/id_ed25519")
    host        = self.public_ip
  }

  provisioner "remote-exec" {
    script = "./scripts/wait-host.sh"
  }

  provisioner "local-exec" {
    command = "cd ../ansible && ansible-playbook -i '${self.private_ip},' -u ubuntu mongo.yml"
  }
}