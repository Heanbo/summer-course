run "release_record_uses_input_values" {
  command = apply

  variables {
    environment  = "test"
    app_version  = "2.0.0"
    service_name = "payments"
  }

  assert {
    condition     = terraform_data.release.output.environment == "test"
    error_message = "release record should use the provided environment."
  }

  assert {
    condition     = terraform_data.release.output.version == "2.0.0"
    error_message = "release record should use the provided app version."
  }

  assert {
    condition     = terraform_data.release.output.name == "payments-test"
    error_message = "release record name should combine service_name and environment."
  }
}

run "module_output_uses_input_values" {
  command = apply

  variables {
    environment  = "stage"
    app_version  = "3.1.4"
    service_name = "checkout"
  }

  assert {
    condition     = module.checkout_service.service.full_name == "checkout-stage"
    error_message = "module service full_name should combine service name and environment."
  }
}
