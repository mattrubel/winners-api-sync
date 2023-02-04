resource "aws_ecs_cluster" "winners_api_sync_ecs_cluster" {
  name = "winners-api-sync"

  setting {
    name  = "containerInsights"
    value = "enabled"
  }
}

resource "aws_ecs_task_definition" "winners_api_sync_ecs_runner_task" {
  family = "winners-api-sync-family"
  container_definitions = jsonencode([
    {
      name      = "winners-api-sync"
      image     = aws_ecr_repository.winners_api_sync_repository.repository_url
      cpu       = 1
      memory    = 1024
      essential = true
      portMappings = [
        {
          containerPort = 80
          hostPort      = 80
        }
      ]
    }
  ])
}
