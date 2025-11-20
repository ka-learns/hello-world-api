output "ecs_cluster_name" {
  description = "Name of the ECS Cluster"
  value       = aws_ecs_cluster.main.name
}

output "ecs_service_name" {
  description = "Name of the ECS Service"
  value       = aws_ecs_service.app.name
}

output "cloudwatch_log_group" {
  description = "Name of the CloudWatch Log Group"
  value       = aws_cloudwatch_log_group.app.name
}
