terraform {
  required_providers {
    aws = {
        source = "hashicorp/aws"
        version = "~> 6.0"
    }
  }
}

# configure the AWS provider
provider "aws" {
    region = "eu-north-1"
}

resource "aws_s3_bucket" "exmaple" {
  bucket = "hamzah-bucket"
  
}