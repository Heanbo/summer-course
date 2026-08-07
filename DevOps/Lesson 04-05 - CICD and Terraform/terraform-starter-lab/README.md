# Terraform Starter Lab

## What is Terraform?

Terraform is an **Infrastructure as Code (IaC)** tool. Instead of clicking through a web console to create servers, databases, or other resources, you write a configuration file that *describes* what you want, and Terraform figures out how to create it.

The core idea is **desired state**: you declare the end result you want, and Terraform computes the steps to get there — and later, to update or remove it.

**This lab requires no cloud account.** All resources are created locally on your machine so you can learn the Terraform workflow without any cost or sign-up.

---

## How Terraform Works (The Core Loop)

Every Terraform workflow follows the same four steps:

```
Write  →  Plan  →  Apply  →  Destroy
```

| Step | What it does |
|------|--------------|
| **Write** | Edit `.tf` files to describe what you want |
| **Plan** | Terraform previews what it *would* change — nothing is created yet |
| **Apply** | Terraform makes the actual changes |
| **Destroy** | Terraform removes everything it created |

---

## Project Structure

```
terraform-starter-lab/
├── main.tf           # The main configuration — resources are defined here
├── variables.tf      # Input variables (like function parameters)
├── outputs.tf        # Values Terraform prints after applying
├── modules/
│   └── service/      # A reusable child module
│       ├── main.tf
│       ├── variables.tf
│       └── outputs.tf
└── tests/
    └── release.tftest.hcl   # Automated tests for the configuration
```

**Key concepts:**
- **`main.tf`** — Defines the resources Terraform manages. In this lab, those are `terraform_data` objects (simple local records, no cloud needed).
- **`variables.tf`** — Declares inputs so you can customize behavior without editing `main.tf` directly.
- **`outputs.tf`** — Declares what values to display after an apply (e.g., the name and version of a deployed service).
- **Modules** — A module is just a folder of `.tf` files. The root module (`main.tf`) calls the `modules/service` child module to show how code reuse works in Terraform.

---

## Requirements

- **Terraform CLI 1.4 or later** — see installation steps below
- A terminal (Terminal, iTerm, PowerShell, etc.)
- A text editor (VS Code recommended)
- No cloud account needed

### Installing Terraform

**macOS (Homebrew):**
```bash
brew tap hashicorp/tap
brew install hashicorp/tap/terraform
```

**Windows (Chocolatey):**
```powershell
choco install terraform
```

**Linux (apt):**
```bash
sudo apt-get install -y gnupg software-properties-common
wget -O- https://apt.releases.hashicorp.com/gpg | gpg --dearmor | sudo tee /usr/share/keyrings/hashicorp-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
sudo apt update && sudo apt install terraform
```

Verify installation:
```bash
terraform version
# Should print: Terraform v1.x.x
```

---

## Getting Started

Open a terminal and navigate to this folder:

```bash
cd terraform-starter-lab
```

All commands below must be run from inside this folder.

---

## Lab 1: First Apply

This lab walks through the complete Terraform workflow from scratch.

### Step 1 — Initialize

```bash
terraform init
```

**What this does:** Downloads any required providers and sets up the local `.terraform` directory. You must run this once before anything else. Think of it like `npm install` or `pip install`.

You should see output ending with:
```
Terraform has been successfully initialized!
```

### Step 2 — Format

```bash
terraform fmt
```

**What this does:** Automatically fixes indentation and style in your `.tf` files to match the Terraform standard. If files were already formatted correctly, nothing changes. If a file name is printed, it was reformatted.

### Step 3 — Validate

```bash
terraform validate
```

**What this does:** Checks your configuration for syntax errors and logical mistakes *without* connecting to any provider or creating anything. This is a fast, safe check.

You should see:
```
Success! The configuration is valid.
```

### Step 4 — Plan

```bash
terraform plan
```

**What this does:** Shows a preview of exactly what Terraform *would* create, change, or destroy. Nothing is created yet. Read this output carefully before every apply.

Look for the summary line at the bottom:
```
Plan: 2 to add, 0 to change, 0 to destroy.
```

This tells you: 2 new resources will be created, nothing will be modified, nothing will be deleted.

### Step 5 — Apply

```bash
terraform apply
```

**What this does:** Executes the plan and creates the resources. Terraform will show the plan one more time and ask for confirmation.

When prompted, type `yes` and press Enter:
```
Do you want to perform these actions?
  Enter a value: yes
```

> **Tip:** To skip the confirmation prompt (useful in CI/CD pipelines), use `terraform apply -auto-approve`. Avoid this when learning — always review the plan first.

### Step 6 — View Outputs

```bash
terraform output
```

**What this does:** Prints the values declared in `outputs.tf`. You should see the release record and the checkout service details that Terraform created.

---

## Lab 2: Make a Change and Re-Plan

One of Terraform's most important features is **detecting drift** — what is different between your code and the real world?

### Step 1 — Plan with a new variable value

```bash
terraform plan -var="app_version=1.0.1"
```

**What this does:** Passes a new value for the `app_version` variable (overriding the default of `1.0.0`) and shows what *would* change. The `-var` flag lets you override any variable from the command line.

Look at the plan output. You should see `~` (tilde) symbols, which mean **update in-place**:
```
  ~ resource "terraform_data" "release" {
      ~ input = {
          ~ version = "1.0.0" -> "1.0.1"
        }
    }
```

### Step 2 — Apply the change

```bash
terraform apply -var="app_version=1.0.1"
```

Type `yes` to confirm. Terraform will update only what changed.

### Step 3 — Inspect the full state

```bash
terraform show
```

**What this does:** Prints the full contents of the **state file** — Terraform's memory of everything it manages. This is how Terraform knows what currently exists so it can compute future changes.

**Reflect on these questions:**
- What changed between `1.0.0` and `1.0.1`?
- What stayed the same (e.g., the service name)?
- Where is the previous version value stored?

---

## Lab 3: Understand Modules

Modules are how Terraform code is organized and reused. The root `main.tf` calls the `modules/service` child module, just like a function calling another function.

Open `main.tf` and find this block:

```hcl
module "checkout_service" {
  source = "./modules/service"

  name        = var.service_name
  environment = var.environment
  app_version = var.app_version
}
```

This passes three **inputs** into the child module. Open `modules/service/variables.tf` to see what inputs the module expects, and `modules/service/outputs.tf` to see what it returns.

### View the module output

```bash
terraform output checkout_service
```

**Reflect on these questions:**
- What inputs does `modules/service` require?
- What output does it return?
- How does this compare to calling a function with parameters and a return value?
- Why is this useful if you needed 10 services instead of 1?

---

## Lab 4: Inspect State

Terraform stores everything it manages in a **state file** (`terraform.tfstate`). This is how it tracks the difference between what your code says and what actually exists.

### List all tracked resources

```bash
terraform state list
```

You will see each resource Terraform is managing, for example:
```
terraform_data.release
module.checkout_service.terraform_data.service
```

### Inspect a specific resource

```bash
terraform state show terraform_data.release
```

**What this does:** Prints all attributes Terraform has stored for that single resource.

### View outputs as JSON

```bash
terraform output -json
```

**What this does:** Prints all outputs in machine-readable JSON format. This is how CI/CD pipelines and scripts read Terraform output values.

**Reflect on these questions:**
- What data is stored in the state file?
- What would happen if the state file was deleted?
- Why should real Terraform state (pointing to live cloud resources) be stored remotely and kept secure?

---

## Lab 5: Run the Automated Tests

Terraform 1.6+ includes a built-in testing framework. Tests are defined in `.tftest.hcl` files inside the `tests/` folder.

```bash
terraform test
```

**What this does:** Runs the test scenarios defined in `tests/release.tftest.hcl`. Each `run` block applies the configuration with specific variable values and then checks (`assert`) that the outputs match expectations.

Open `tests/release.tftest.hcl` to read the assertions. Notice how the tests:
1. Set specific input values (`environment = "test"`, `app_version = "2.0.0"`)
2. Assert that outputs match exactly what was passed in

You should see:
```
All tests passed!
```

This is the same pattern used in CI/CD pipelines to validate infrastructure code before it is merged or deployed.

---

## Lab 6: Clean Up

When you are done, remove all resources Terraform created:

```bash
terraform destroy
```

Terraform will show you what it plans to delete. Type `yes` to confirm.

You should see:
```
Destroy complete! Resources: 2 destroyed.
```

> **Why this matters:** In a real cloud environment, `terraform destroy` removes actual infrastructure (VMs, databases, load balancers). Always review the destroy plan carefully.

---

## Variables Reference

These variables are defined in `variables.tf` and can be overridden with `-var="name=value"`:

| Variable | Default | Description |
|----------|---------|-------------|
| `service_name` | `checkout` | Base name of the service |
| `environment` | `dev` | Deployment environment (`dev`, `test`, `stage`, `prod`) |
| `app_version` | `1.0.0` | Application version to record |
| `owner` | `platform-training` | Team or person responsible |

Example — running with custom values:
```bash
terraform apply \
  -var="service_name=payments" \
  -var="environment=stage" \
  -var="app_version=2.5.0"
```

---

## Optional: GitHub Actions CI/CD

The same commands you ran manually can be automated in a CI/CD pipeline. A typical Terraform GitHub Actions workflow runs `terraform plan` on every pull request (so reviewers can see the planned changes) and `terraform apply` only when code is merged to `main`.

Example workflow structure (`.github/workflows/terraform.yml`):

```yaml
name: Terraform

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  terraform:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Terraform
        uses: hashicorp/setup-terraform@v3
        with:
          terraform_version: "~1.4"

      - name: Terraform Init
        run: terraform init

      - name: Terraform Format Check
        run: terraform fmt -check

      - name: Terraform Validate
        run: terraform validate

      - name: Terraform Plan
        run: terraform plan

      # Only apply on merge to main, not on PRs
      - name: Terraform Apply
        if: github.ref == 'refs/heads/main' && github.event_name == 'push'
        run: terraform apply -auto-approve
```

**Notice the connection to what you just practiced manually:**
- Every step maps directly to a command you already ran
- `fmt -check` fails the pipeline if code isn't formatted (enforces standards)
- `plan` runs on pull requests so the team sees proposed changes *before* merge
- `apply` only runs on `main` — the same gate pattern as a deployment pipeline


This repo includes `.github/workflows/terraform-checks.yml`.

It runs:

- `terraform fmt -check`
- `terraform init`
- `terraform validate`
- `terraform test`

That ties this Terraform class back to the CI/CD class.
