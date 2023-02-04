Add this to readme later:

Steps to configure Terraform:
1. add terraform/backend.tf file as such:
        ```
        terraform {
          backend "s3" {
            bucket         = "terraform-s3-bucket"
            key            = "winners-api-sync/terraform.tfstate"
            region         = "us-east-1"
            dynamodb_table = "tf-state-lock-table-name"
          }
        }
        ```

2. add terraform/variables.tf as such:
        ```
        variable "AWS_REGION" {
          default = "us-east-1"
        }
        ```