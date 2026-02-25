variable "public_key" {
    type = string
    default = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIOxWhTj+Gyvz+8pPgQWS8NPnaimpPOUXtWtDGpZp/udJ gitlab-runner@ip-172-31-34-248"
}

variable "instance-type" {
    type = string
    default = "t3.micro"
}