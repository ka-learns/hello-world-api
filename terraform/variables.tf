variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Project Name"
  type        = string
  default     = "hello-world-api"
}

variable "ecr_image_uri" {
  description = "ECR Image URI for the Hello World API"
  type        = string
}