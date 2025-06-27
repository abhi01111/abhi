Scenarios DevOpa
---

### **Scenario 1: Terraform Setup for AWS EC2**
**Question:**  
You have been assigned the task to provision a set of EC2 instances in AWS for a web application. The configuration must include the following:
- EC2 instances should be provisioned in two different subnets (one public and one private).
- Security groups should be attached to the instances.
- Use Terraform to automate the creation of these resources.  
How would you approach this task using Terraform, and what are the key configuration files you would need?

**Expected Answer:**
- **Steps:**
  1. **Install Terraform** and configure AWS credentials (`aws configure`).
  2. Create a Terraform configuration that defines:
     - **VPC** with two subnets: one public and one private.
     - **Security Groups**: Create separate security groups for the web servers (e.g., allowing HTTP/HTTPS for public instances).
     - **EC2 Instances**: Provision EC2 instances in the respective subnets.
  3. Organize configurations into separate files like `main.tf`, `variables.tf`, and `outputs.tf`.

- **Example Configuration:**
  ```hcl
  provider "aws" {
    region = "us-west-2"
  }

  resource "aws_vpc" "main" {
    cidr_block = "172.16.0.0/16"
  }

  resource "aws_subnet" "public" {
    vpc_id     = aws_vpc.main.id
    cidr_block = "172.16.1.0/24"
    availability_zone = "us-west-2a"
    map_public_ip_on_launch = true
  }

  resource "aws_subnet" "private" {
    vpc_id     = aws_vpc.main.id
    cidr_block = "172.16.2.0/24"
    availability_zone = "us-west-2b"
  }

  resource "aws_security_group" "web_sg" {
    name        = "web_sg"
    description = "Allow HTTP and SSH"
    ingress {
      from_port   = 80
      to_port     = 80
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
    }
    ingress {
      from_port   = 22
      to_port     = 22
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
    }
  }

  resource "aws_instance" "web_instance" {
    ami           = "ami-0c55b159cbfafe1f0"
    instance_type = "t2.micro"
    subnet_id     = aws_subnet.public.id
    security_groups = [aws_security_group.web_sg.name]
  }
  ```

---

### **Scenario 2: Remote Backend Configuration**
**Question:**  
Your team is collaborating on a Terraform project, and you need to configure a **remote backend** to store Terraform's state file (to prevent conflicts in a shared environment). Your organization uses AWS S3 for storage and DynamoDB for state locking.  
How would you configure Terraform to use AWS S3 as a remote backend for state management, and what would be the benefits of using this setup?

**Expected Answer:**
- **Steps:**
  1. **Configure Remote Backend** using AWS S3 and DynamoDB for state locking.
  2. Create an S3 bucket and a DynamoDB table for the state.
  3. Update `backend` configuration in the Terraform configuration file.

- **Example Configuration:**
  ```hcl
  terraform {
    backend "s3" {
      bucket = "my-terraform-state"
      key    = "terraform/statefile.tfstate"
      region = "us-west-2"
      dynamodb_table = "terraform-state-lock"
      encrypt = true
    }
  }
  ```

- **Benefits of this setup:**
  - **Collaborative workflows**: Multiple team members can apply changes without overriding each other's work.
  - **State locking**: Prevents concurrent modifications by locking the state in DynamoDB.
  - **Remote storage**: The state file is securely stored in AWS S3, ensuring durability and accessibility.

---

### **Scenario 3: Handling Secret Management**
**Question:**  
You are tasked with deploying a web application to AWS using Terraform. The application requires database credentials, API keys, and other sensitive data, which should not be exposed in the Terraform configuration files. How would you handle the secret management in this scenario?

**Expected Answer:**
- **Steps:**
  1. Use **Terraform variables** to store sensitive data.
  2. Use **AWS Secrets Manager** or **HashiCorp Vault** to securely store and manage secrets.
  3. Refer to secrets in Terraform without hardcoding sensitive information.

- **Example Configuration for AWS Secrets Manager:**
  ```hcl
  resource "aws_secretsmanager_secret" "db_password" {
    name        = "db_password"
    description = "Database password for the web application"
  }

  resource "aws_secretsmanager_secret_version" "db_password_version" {
    secret_id     = aws_secretsmanager_secret.db_password.id
    secret_string = "{\"username\":\"admin\",\"password\":\"${var.db_password}\"}"
  }
  ```

- Use **Terraform variables** for sensitive data:
  ```hcl
  variable "db_password" {
    type      = string
    sensitive = true
  }
  ```

- **Advantages:**
  - Sensitive data is never hardcoded in the configuration files.
  - Secrets are securely stored and accessed during infrastructure provisioning.

---

### **Scenario 4: Scaling Infrastructure Using Modules**
**Question:**  
Your application requires scaling to multiple regions. You need to provision EC2 instances in two different regions, each within a separate VPC. How can you use Terraform modules to make this process reusable and scalable?

**Expected Answer:**
- **Steps:**
  1. Define a **module** for provisioning resources like EC2, VPC, and Subnets.
  2. Reuse the module to provision resources in multiple regions by passing region-specific variables.

- **Example:**
  - **Module Directory Structure**:
    ```
    modules/
      ec2_instance/
        main.tf
        variables.tf
        outputs.tf
  ```

  - **Module Configuration**:
    ```hcl
    resource "aws_vpc" "main" {
      cidr_block = "172.16.0.0/16"
    }

    resource "aws_instance" "web" {
      ami           = "ami-0c55b159cbfafe1f0"
      instance_type = "t2.micro"
      subnet_id     = aws_subnet.subnet.id
    }
    ```

  - **Using the Module for Multi-Region Scaling**:
    ```hcl
    module "ec2_instance_region_1" {
      source      = "./modules/ec2_instance"
      region      = "us-west-2"
      ami_id      = "ami-0c55b159cbfafe1f0"
      instance_type = "t2.micro"
    }

    module "ec2_instance_region_2" {
      source      = "./modules/ec2_instance"
      region      = "us-east-1"
      ami_id      = "ami-0c55b159cbfafe1f0"
      instance_type = "t2.micro"
    }
    ```

- **Benefits:**
  - **Scalability**: You can easily scale to multiple regions by reusing the same module.
  - **Reusability**: The module ensures consistency across deployments and simplifies the management of multiple environments.

---

### **Scenario 5: Handling Terraform State and Environment Configurations**
**Question:**  
You have different environments for your application: **Development**, **Staging**, and **Production**. Each environment has its own set of resources, such as VPCs, EC2 instances, and RDS databases. How would you manage Terraform state and configurations for these environments in a way that is scalable and maintainable?

**Expected Answer:**
- **Steps:**
  1. **Separate Environment Configuration**: Maintain different directories or workspaces for each environment (e.g., `dev/`, `staging/`, `prod/`).
  2. Use **workspaces** to manage different state files for each environment.
  3. Organize configurations by creating reusable modules that can be shared across environments.

- **Example:**
  ```bash
  terraform workspace new dev
  terraform workspace new staging
  terraform workspace new prod
  ```

  - For each workspace, the `terraform.tfstate` will be maintained separately, ensuring there is no conflict between environments.

- **Benefits:**
  - **Isolation of environments**: Each environment has its own state and configuration.
  - **Scalability**: New environments can be added easily by creating new workspaces or directories.
  - **Consistency**: Using modules ensures that the infrastructure is the same across environments.

---


---

### **Scenario 6: Managing AWS Security Groups with Terraform**
**Question:**  
You need to create a security group for an EC2 instance in AWS. This security group should allow SSH (port 22) access only from a specific IP address and HTTP (port 80) access from any source. Additionally, you should create an auto-scaling group where new EC2 instances will use this security group. How would you approach this using Terraform?

**Expected Answer:**
- **Steps:**
  1. **Create the security group** with inbound rules for SSH (restricted to specific IP) and HTTP (open to all).
  2. **Provision EC2 instances** using an Auto Scaling Group, ensuring the instances use the created security group.

- **Example Configuration:**
  ```hcl
  resource "aws_security_group" "web_sg" {
    name        = "web_sg"
    description = "Allow HTTP and SSH"
    
    ingress {
      from_port   = 22
      to_port     = 22
      protocol    = "tcp"
      cidr_blocks = ["203.0.113.5/32"]  # Replace with your IP
    }

    ingress {
      from_port   = 80
      to_port     = 80
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
    }
    
    egress {
      from_port   = 0
      to_port     = 0
      protocol    = "-1"
      cidr_blocks = ["0.0.0.0/0"]
    }
  }

  resource "aws_launch_configuration" "web_launch" {
    name          = "web_launch_config"
    image_id      = "ami-0c55b159cbfafe1f0"
    instance_type = "t2.micro"
    security_groups = [aws_security_group.web_sg.name]
  }

  resource "aws_autoscaling_group" "web_asg" {
    desired_capacity     = 2
    max_size             = 5
    min_size             = 1
    vpc_zone_identifier  = [aws_subnet.public.id]
    launch_configuration = aws_launch_configuration.web_launch.id
  }
  ```

- **Explanation:**
  - **Security Group**: Allows SSH from a specific IP and HTTP from any source.
  - **Auto Scaling Group**: Uses the security group and launch configuration for EC2 instances.

---

### **Scenario 7: Managing Terraform Variables for Multi-Environment Deployments**
**Question:**  
You have to deploy resources to multiple environments (Development, Staging, and Production), and each environment needs different instance types and other parameters (e.g., VPC CIDR block, region). How would you manage environment-specific configurations in Terraform?

**Expected Answer:**
- **Steps:**
  1. Use **variables** for dynamic values such as instance types and VPC CIDR blocks.
  2. Create **separate variable files** for each environment (e.g., `dev.tfvars`, `prod.tfvars`).
  3. Use `terraform apply -var-file="dev.tfvars"` or `terraform apply -var-file="prod.tfvars"` for environment-specific deployment.

- **Example:**
  - **Variable Definition (variables.tf)**:
    ```hcl
    variable "region" {
      type    = string
      default = "us-west-2"
    }

    variable "instance_type" {
      type    = string
      default = "t2.micro"
    }

    variable "vpc_cidr_block" {
      type    = string
      default = "172.16.0.0/16"
    }
    ```

  - **Environment-Specific Variables (dev.tfvars)**:
    ```hcl
    region        = "us-west-2"
    instance_type = "t2.micro"
    vpc_cidr_block = "172.16.0.0/16"
    ```

  - **Environment-Specific Variables (prod.tfvars)**:
    ```hcl
    region        = "us-east-1"
    instance_type = "t3.large"
    vpc_cidr_block = "10.0.0.0/16"
    ```

- **Command to Apply for Dev Environment:**
  ```bash
  terraform apply -var-file="dev.tfvars"
  ```

---

### **Scenario 8: Managing Multiple Cloud Providers in Terraform**
**Question:**  
You are tasked with provisioning resources across multiple cloud providers, such as AWS and Azure. How would you configure Terraform to manage both AWS and Azure resources in a single configuration file, and what are the considerations for working with multiple providers?

**Expected Answer:**
- **Steps:**
  1. **Configure multiple providers** by specifying each provider's credentials and settings.
  2. Use **provider aliases** to differentiate between resources from different providers.
  3. Provision resources on AWS and Azure in a single configuration file by referring to each provider using its alias.

- **Example Configuration:**
  ```hcl
  provider "aws" {
    region = "us-west-2"
  }

  provider "azurerm" {
    features {}
  }

  resource "aws_instance" "web" {
    ami           = "ami-0c55b159cbfafe1f0"
    instance_type = "t2.micro"
  }

  resource "azurerm_virtual_machine" "linux_vm" {
    name                = "example-vm"
    location            = "East US"
    resource_group_name = "example-resources"
    network_interface_ids = [
      azurerm_network_interface.example.id
    ]
    vm_size             = "Standard_DS1_v2"
  }
  ```

- **Considerations:**
  - **Provider Aliases**: Use provider aliases if the same provider needs to be used with different configurations.
  - **Resource Isolation**: Ensure that resources from different cloud providers do not conflict, especially when managing networking.

---

### **Scenario 9: Disaster Recovery Setup with Terraform**
**Question:**  
You need to configure a disaster recovery plan for an application deployed in AWS. The plan involves creating a backup of critical resources (like EC2 instances, RDS databases) in a different region using Terraform. How would you approach this task using Terraform?

**Expected Answer:**
- **Steps:**
  1. **Replicate Resources**: Use Terraform to replicate critical resources like EC2, RDS, and S3 in a secondary region.
  2. **Data Backup**: Use Terraform to automate the backup of EC2 volumes and RDS snapshots to another region.
  3. **State Management**: Manage Terraform states for both regions, possibly using different workspaces or backend configurations.

- **Example Configuration:**
  ```hcl
  resource "aws_instance" "primary" {
    ami           = "ami-0c55b159cbfafe1f0"
    instance_type = "t2.micro"
    region        = "us-west-2"  # Primary Region
  }

  resource "aws_instance" "secondary" {
    ami           = "ami-0c55b159cbfafe1f0"
    instance_type = "t2.micro"
    region        = "us-east-1"  # Secondary Region for DR
  }

  resource "aws_rds_instance" "primary_db" {
    instance_class = "db.t2.micro"
    engine         = "mysql"
    region         = "us-west-2"
  }

  resource "aws_rds_instance" "secondary_db" {
    instance_class = "db.t2.micro"
    engine         = "mysql"
    region         = "us-east-1"
  }
  ```

- **Considerations:**
  - Ensure **cross-region replication** for resources like S3 buckets.
  - Use **AWS RDS snapshots** to backup the database to a secondary region.
  - Ensure **state consistency** and prevent manual overrides by utilizing Terraform workspaces or separate state files for different regions.

---

### **Scenario 10: Terraform in CI/CD Pipelines**
**Question:**  
You are working in a DevOps team where Terraform is integrated into the CI/CD pipeline to manage infrastructure deployment. The CI/CD tool used is Jenkins. How would you set up a Jenkins pipeline to automatically apply Terraform changes upon a commit to a Git repository?

**Expected Answer:**
- **Steps:**
  1. **Install Terraform** on Jenkins nodes.
  2. Create a Jenkins pipeline that automates the process of:
     - Checking out the latest code from GitHub.
     - Initializing Terraform (`terraform init`).
     - Applying the Terraform configuration (`terraform apply`).
  3. Use environment variables and Jenkins secrets to securely handle AWS credentials and other sensitive data.
  4. Implement **Terraform plan** step to review changes before applying.

- **Example Jenkins Pipeline (Jenkinsfile):**
  ```groovy
  pipeline {
    agent any
    environment {
      AWS_ACCESS_KEY_ID = credentials('aws-access-key-id')
      AWS_SECRET_ACCESS_KEY = credentials('aws-secret-access-key')
    }
    stages {
      stage('Checkout') {
        steps {
          git 'https://github.com/my-repo/terraform-infra.git'
        }
      }
      stage('Terraform Init') {
        steps {
          sh 'terraform init'
        }
      }
      stage('Terraform Plan') {
        steps {
          sh 'terraform plan'
        }
      }
      stage('Terraform Apply') {
        steps {
          sh 'terraform apply -auto-approve'
        }
      }
    }
  }
  ```

- **Considerations:**
  - Use **Terraform plan** to review changes before applying.
  - Ensure **AWS credentials** are securely managed in Jenkins using the `credentials` block.
  - Enable **state management** in a shared backend like AWS S3 to avoid conflicts.

---

