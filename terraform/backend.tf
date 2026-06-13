terraform {
  backend "s3" {
    bucket = "my-devops-tf-state"
    key    = "eks/terraform.tfstate"
    region = "eu-west-2"
  }
}