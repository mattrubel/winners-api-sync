resource "aws_ecr_repository" "winners_api_sync_repository" {
  name                 = "winners-api-sync"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }
}
