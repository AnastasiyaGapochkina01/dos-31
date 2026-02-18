terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.92"
    }
  required_version = ">= 1.2"
  backend "s3" {
    bucket = "dos-31-tfstates"
    key    = "17-02/terraform.tfstate"
    region = "us-east-2"
  }

}

provider "aws" {
  region = "us-east-2"
}
