provider "aws" {
  region = var.AWS_REGION
}

module "winners-api-sync" {
  source = "./aws-resource-configs"
}
