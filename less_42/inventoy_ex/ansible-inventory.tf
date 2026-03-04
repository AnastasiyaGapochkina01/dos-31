locals {
  ansible_template = {
    all = {
      vars = {
        project = var.project_name
      }
      hosts = {
        "demo-app-vm-1" = {
          ansible_host = aws_network_interface.demo-app-if-1.private_ip
        }
      }
    }
  }
}

resource "local_file" "inventory" {
  content = yamlencode(local.ansible_template)
  filename = "hosts.yaml"
}