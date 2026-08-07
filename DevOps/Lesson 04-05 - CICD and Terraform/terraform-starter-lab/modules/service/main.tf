locals {
  full_name = "${var.name}-${var.environment}"
}

resource "terraform_data" "service" {
  input = {
    name        = var.name
    full_name   = local.full_name
    environment = var.environment
    version     = var.app_version
  }
}
