resource "aws_ecs_cluster" "winners_api_sync_ecs_cluster" {
  name = "winners-api-sync"

  setting {
    name  = "containerInsights"
    value = "enabled"
  }
}

# https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ecs_task_definition
