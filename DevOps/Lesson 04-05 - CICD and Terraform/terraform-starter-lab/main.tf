terraform {
  required_version = ">= 1.4.0"
}

locals {
  service_name = "${var.service_name}-${var.environment}"
  release_tags = {
    owner       = var.owner
    environment = var.environment
    managed_by  = "terraform"
  }
}

resource "terraform_data" "release" {
  input = {
    name        = local.service_name
    version     = var.app_version
    environment = var.environment
    tags        = local.release_tags
  }
}

module "checkout_service" {
  source = "./modules/service"

  name        = var.service_name
  environment = var.environment
  app_version = var.app_version
}
