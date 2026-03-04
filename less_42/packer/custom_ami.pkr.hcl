packer {
  required_plugins {
    aws = {
      version = ">= 1.2.8"
      source = "github.com/hashicorp/amazon"
    }
    ansible = {
      source = "github.com/hashicorp/ansible"
      version = "~> 1"
    }
  }
}

source "amazon-ebs" "ubuntu" {
  ami_name = "dos-31-custom-ubuntu"
  instance_type = "t3.micro"
  region = "us-east-2"
  ssh_pty = true
  ssh_clear_authorized_keys = true
  source_ami_filter {
    filters = {
      name = "ubuntu/images/*ubuntu-jammy-22.04-amd64-server-*"
      root-device-type = "ebs"
      virtualization-type = "hvm"
    }
    most_recent = true
    owners = ["099720109477"]
  }
  ssh_username = "ubuntu"
}

build {
  sources = ["source.amazon-ebs.ubuntu"]

    provisioner "file" {
      source = "files"
      destination = "/tmp"
    }

  provisioner "shell" {
    inline = ["sudo /tmp/files/setup.sh"]
  }

  provisioner "ansible" {
    playbook_file = "./mongo.yml"
    ansible_env_vars = [
      "ANSIBLE_HOST_KEY_CHECK=False",
      "ANSIBLE_SSH_ARGS=-o StrictHostKeyChecking no",
      "ANSIBLE_SCP_IF_SSH=True",
      "ANSIBLE_SCP_EXTRA_VARS='-0'"
    ]
  }

}