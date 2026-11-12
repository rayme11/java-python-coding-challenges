# Module 1: Infrastructure as Code (Terraform + Bicep + Azure)

> **Objective:** Learn to provision and manage Azure infrastructure using Infrastructure as Code (IaC) principles. This module covers Azure Resource Manager (ARM), Terraform, and Bicep for reproducible infrastructure deployment.

---

## 🎯 Learning Objectives

By completing this module, you will be able to:
- [ ] Initialize Terraform and configure Azure provider
- [ ] Create resource groups, virtual networks, and storage accounts via Terraform
- [ ] Deploy Azure resources using Bicep (Microsoft's native IaC)
- [ ] Manage state files and remote state storage
- [ ] Destroy resources cleanly to avoid cost leakage
- [ ] Understand state locking and team collaboration patterns

---

## 📋 Theory: Infrastructure as Code (IaC)

**Why IaC?**
- **Consistency:** Same environment every time (dev, test, prod)
- **Version Control:** Infrastructure changes tracked in Git
- **Repeatability:** Recreate entire environments in minutes
- **Documentation:** Code IS documentation
- **Cost Control:** Tear down resources when not needed

**Terraform vs Bicep vs ARM:**
| Feature | Terraform | Bicep | ARM JSON |
|---------|-----------|-------|----------|
| Cloud Agnostic | ✅ Yes | ❌ Azure only | ❌ Azure only |
| State Management | ✅ Built-in | ❌ None (declarative) | ❌ None |
| Learning Curve | Medium | Low | High |
| Azure Native | No | Yes (transpiles to ARM) | Yes |
| Community Modules | Extensive | Limited | Limited |

---

## 🛠️ Step 1: Initialize Terraform

### Initialize Terraform with Azure Provider

```bash
cd ai/sre-engineering/module-1-iac

# Initialize Terraform working directory
terraform init

# Verify Terraform version
terraform --version

# List available providers
terraform providers
```

### Create Azure Resource Group via Terraform

**File:** `main.tf`

```hcl
terraform {
  required_version = ">= 1.5.0"
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }
}

provider "azurerm" {
  features {}
}

# Resource Group
resource "azurerm_resource_group" "qe_rg" {
  name     = "rg-qe-lab-${var.environment}"
  location = var.location
  tags = {
    environment = var.environment
    managed_by  = "terraform"
    project     = "qe-automation-lab"
  }
}

# Output the resource group ID
output "resource_group_id" {
  value = azurerm_resource_group.qe_rg.id
}

output "resource_group_name" {
  value = azurerm_resource_group.qe_rg.name
}
```

**File:** `variables.tf`

```hcl
variable "environment" {
  description = "Environment name (dev, test, prod)"
  type        = string
  default     = "dev"
}

variable "location" {
  description = "Azure region for resources"
  type        = string
  default     = "eastus"
}

variable "resource_group_name" {
  description = "Name of the resource group"
  type        = string
  default     = "rg-qe-lab"
}
```

**File:** `outputs.tf`

```hcl
output "rg_name" {
  value = azurerm_resource_group.qe_rg.name
  description = "Name of the resource group"
}

output "rg_id" {
  value = azurerm_resource_group.qe_rg.id
  description = "Full ID of the resource group"
}
```

**File:** `terraform.tfvars`

```hcl
environment = "dev"
location    = "eastus"
```

---

## 🚀 Step 2: Deploy Infrastructure

### Initialize and Plan

```bash
cd ai/sre-engineering/module-1-iac

# Initialize Terraform (downloads providers)
terraform init

# Validate configuration syntax
terraform validate

# Show execution plan (dry run)
terraform plan -out=tfplan

# View the plan in human-readable format
terraform show tfplan
```

### Apply Changes

```bash
# Apply the plan to create resources
terraform apply tfplan

# Or apply directly without plan file
terraform apply -auto-approve

# Verify resources were created
terraform show
```

### Verify Resources Created

```bash
# List resource groups in Azure
az group list --query "[].{name:name, location:location, provisioningState:properties.provisioningState}" --output table

# Find our specific resource group
az group show --name rg-qe-lab-dev --query "{name:name, location:location, id:id}"
```

---

## 🚀 Step 3: Create Virtual Network

**File:** `modules/virtual-network/main.tf`

```hcl
variable "resource_group_name" {
  type = string
}

variable "vnet_name" {
  type = string
}

variable "address_space" {
  type = list(string)
  default = ["10.0.0.0/16"]
}

variable "subnet_name" {
  type = string
}

variable "subnet_prefix" {
  type = string
  default = "10.0.1.0/24"
}

resource "azurerm_virtual_network" "qe_vnet" {
  name                = var.vnet_name
  location            = azurerm_resource_group.qe_rg.location
  resource_group_name = var.resource_group_name
  address_space       = var.address_space

  tags = {
    environment = var.environment
    managed_by  = "terraform"
  }
}

resource "azurerm_subnet" "qe_subnet" {
  name                 = var.subnet_name
  resource_group_name  = var.resource_group_name
  virtual_network_name = azurerm_virtual_network.qe_vnet.name
  address_prefixes     = [var.subnet_prefix]

  delegation {
    name = "app-service-delegation"
    service {
      name = "Microsoft.Web/serverFarms"
    }
  }

  depends_on = [azurerm_virtual_network.qe_vnet]
}

output "vnet_id" {
  value = azurerm_virtual_network.qe_vnet.id
}

output "subnet_id" {
  value = azurerm_subnet.qe_subnet.id
}
```

**File:** `modules/virtual-network/variables.tf`

```hcl
variable "resource_group_name" {
  type = string
}

variable "vnet_name" {
  type = string
}

variable "address_space" {
  type = list(string)
}

variable "subnet_name" {
  type = string
}

variable "subnet_prefix" {
  type = string
}
```

---

## 🚀 Step 3: Deploy Virtual Network via Terraform

```bash
# From the module-1-iac directory

# Update main.tf to include VNet module
cat >> main.tf << 'EOF'

# Virtual Network Module
module "vnet" {
  source       = "./modules/virtual-network"
  resource_group_name = azurerm_resource_group.qe_rg.name
  vnet_name      = "vnet-qe-${var.environment}"
  address_space  = ["10.0.0.0/16"]
  subnet_name    = "snet-qe-${var.environment}"
  subnet_prefix  = "10.0.1.0/24"
}

output "vnet_id" {
  value = module.vnet.vnet_id
}

output "subnet_id" {
  value = module.vnet.subnet_id
}
EOF

# Plan and apply
terraform plan -out=tfplan-vnet
terraform apply tfplan-vnet

# Verify VNet was created
az network vnet list --query "[].{name:name, location:location, addressSpace:addressSpace}" --output table
```

---

## 🚀 Step 4: Create Storage Account

**File:** `modules/storage-account/main.tf`

```hcl
variable "resource_group_name" {
  type = string
}

variable "storage_account_name" {
  type = string
}

variable "location" {
  type = string
}

variable "sku" {
  type = string
  default = "Standard_LRS"
}

variable "kind" {
  type = string
  default = "StorageV2"
}

resource "azurerm_storage_account" "qe_storage" {
  name                     = var.storage_account_name
  resource_group_name      = var.resource_group_name
  location                 = var.location
  account_tier             = var.sku
  account_kind             = var.kind
  enable_https_traffic_only = true
  min_tls_version          = "TLS1.2"

  tags = {
    environment = var.environment
    managed_by  = "terraform"
  }
}

output "storage_account_name" {
  value = azurerm_storage_account.qe_storage.name
}

output "storage_account_id" {
  value = azurerm_storage_account.qe_storage.id
}

output "primary_connection_string" {
  value     = azurerm_storage_account.qe_storage.primary_connection_string
  sensitive = true
}
```

---

## 🚀 Step 5: Destroy Infrastructure (Cost Control)

**Always destroy resources when done learning to avoid charges.**

```bash
# Plan the destruction
terraform plan -destroy

# Destroy all resources
terraform destroy -auto-approve

# Verify all resources are gone
az group list --query "[?name=='rg-qe-lab-dev']" --output table
# Should return empty array if successfully deleted
```

---

## 🧪 Verification Checklist

- [ ] `terraform init` completed successfully
*   `terraform validate` passed without errors
*   `terraform plan` showed expected resources
*   `terraform apply` created resources successfully
*   Azure Portal shows resources created
*   `terraform destroy` removed all resources
*   No orphaned resources in Azure Portal

---

## 🔗 Next Steps

Once Phase 1 is complete, proceed to **Module 2: Containers** to learn Docker and Kubernetes deployment.

```bash
cd ../module-2-containers && cat README.md
```
