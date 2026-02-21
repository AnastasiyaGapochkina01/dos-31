module "dev-environment" {
  source        = "./infra"
  env           = "dev"
  vpc_ips       = "10.0.0.0/16"
  subnet_ips    = "10.0.1.0/24"
  az            = "us-east-2a"
  ami_id        = "ami-06e3c045d79fd65d9"
  instance-type = "t3.micro"
}
