output "service" {
  description = "Service release information returned to the root module."
  value       = terraform_data.service.output
}
