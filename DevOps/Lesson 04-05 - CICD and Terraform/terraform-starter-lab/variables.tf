variable "service_name" {
  description = "Base service name used for the training release record."
  type        = string
  default     = "checkout"
}

variable "environment" {
  description = "Deployment environment name."
  type        = string
  default     = "dev"

  validation {
    condition     = contains(["dev", "test", "stage", "prod"], var.environment)
    error_message = "environment must be one of: dev, test, stage, prod."
  }
}

variable "app_version" {
  description = "Application version to record in the local release object."
  type        = string
  default     = "1.0.0"
}

variable "owner" {
  description = "Team or person responsible for the service."
  type        = string
  default     = "platform-training"
}
