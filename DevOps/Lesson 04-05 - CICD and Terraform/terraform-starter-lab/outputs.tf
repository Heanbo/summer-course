output "release_record" {
  description = "The root module release record tracked by Terraform."
  value       = terraform_data.release.output
}

output "checkout_service" {
  description = "The service record returned from the child module."
  value       = module.checkout_service.service
}
