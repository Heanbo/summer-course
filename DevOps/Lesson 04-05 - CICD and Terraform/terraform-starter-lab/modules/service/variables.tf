variable "name" {
  description = "Base service name."
  type        = string
}

variable "environment" {
  description = "Environment name for the service."
  type        = string
}

variable "app_version" {
  description = "Application version for this service release."
  type        = string
}
