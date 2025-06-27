Devops
---

---

LMR

---


### **Last-Minute Revision Chart for DevOps and Cloud Technologies**

| **Topic**                              | **Key Points**                                                                                   | **Example/Command** |
|----------------------------------------|-------------------------------------------------------------------------------------------------|---------------------|
| **Introduction to DevOps**             | DevOps is a set of practices that combine software development and IT operations. It aims to shorten the systems development life cycle and provide continuous delivery. | -                   |
| **DevOps Phases**                      | Continuous Development, Continuous Integration, Continuous Testing, Continuous Deployment, Continuous Monitoring. | -                   |
| **CI/CD Pipeline**                     | Automates the steps to deliver code changes, from commit to production. Typically involves **Git**, **Jenkins**, **Docker**, and **Terraform**. | Jenkins pipeline configuration: `stages { build { steps { sh 'docker build . . .'}}}` |
| **CAMS Model (Culture, Automation, Measurement, Sharing)** | Core principles of DevOps: - Culture of collaboration <br> - Automation of repetitive tasks <br> - Measuring performance <br> - Sharing knowledge | - |
| **Immutable Deployment**               | Deployment strategy where infrastructure and applications are versioned and replaced instead of modified. | - |
| **Containerization with Docker**       | Encapsulating applications and their dependencies into containers for easier portability and scalability. | `docker run -d --name web5 -p 8000:80 nginx` |
| **Container Orchestration (Kubernetes/Docker Swarm)** | Tools for managing large-scale deployments of containers, automating scaling, self-healing, and load balancing. | `kubectl apply -f deployment.yaml` <br> `docker swarm init` |
| **Infrastructure as Code (IaC)**       | Managing infrastructure with code rather than manual processes, ensuring reproducibility and automation. Tools: **Terraform**, **Ansible**, **Puppet**, **Chef**. | `terraform apply` |
| **Cloud Providers**                    | Key services from AWS, Azure, GCP like EC2, Lambda, S3, VPC, etc. | AWS EC2: `aws ec2 run-instances --image-id ami-12345678 --instance-type t2.micro` |
| **Terraform Setup**                    | Tool for automating cloud provisioning via declarative configuration files. Requires providers like AWS, Azure, etc. | `terraform init` <br> `terraform plan` |
| **Terraform State Management**         | Tracks the state of infrastructure resources. Use remote backends for collaboration. | `terraform state list` <br> `terraform state show` |
| **Terraform Modules**                  | Reusable configurations for commonly used infrastructure patterns. | `module "vpc" { source = "./vpc" cidr_block = "10.0.0.0/16" }` |
| **Version Control (Git, GitHub)**      | Tool for tracking and managing code changes. GitHub offers cloud-based repositories. | `git clone <repo-url>` <br> `git push` |
| **Git Workflow (Basic)**               | Common workflow involves cloning repositories, making commits, and pushing changes. | `git commit -m "message"` <br> `git push origin main` |
| **Jenkins Setup**                      | Jenkins automates tasks in the CI/CD pipeline. It integrates with version control, containers, and testing tools. | Jenkinsfile: `stages { build { steps { sh 'docker build .'}}}` |
| **CI/CD Pipeline Example (Git, Jenkins, Docker)** | Automate testing, building, and deploying applications using Jenkins, Docker, and Git. | Jenkinsfile example for Docker deployment: `docker build -t my-app .` |
| **Introduction to Agile**              | Agile focuses on iterative development, where requirements and solutions evolve through collaboration. | Scrum/Kanban, Scrum Sprints |
| **Agile Methodologies (Scrum, Kanban)** | Scrum involves time-boxed iterations (Sprints) while Kanban focuses on continuous delivery. | -                   |
| **Lean**                               | Focus on minimizing waste, optimizing processes, and maximizing value delivered to the customer. | -                   |
| **Lean and Agile in DevOps**           | Agile and Lean methodologies align with DevOps to enable faster, more efficient delivery. | -                   |
| **Microservices Architecture**         | Break down applications into small, loosely coupled services that are independently deployable and scalable. | -                   |
| **Cloud VPC Setup (AWS Example)**      | VPC (Virtual Private Cloud) allows you to launch AWS resources in a defined virtual network. | `aws ec2 create-vpc --cidr-block 172.20.0.0/16` |
| **AWS EC2 Setup**                      | Launch EC2 instances to run applications. | `aws ec2 run-instances --image-id ami-12345678 --instance-type t2.micro` |
| **AWS S3**                             | Object storage service for scalable storage. | `aws s3 cp file.txt s3://my-bucket/` |
| **AWS Lambda**                         | Run serverless functions in the cloud. | `aws lambda invoke --function-name my-function out.txt` |
| **AWS VPC Configuration**              | Set up subnets, route tables, and security groups in AWS for networking. | `aws ec2 create-subnet --vpc-id vpc-abc123 --cidr-block 172.20.10.0/24` |
| **Docker and Dockerfile**              | Build and run containers, encapsulate applications in isolated environments. | `docker build -t my-app .` |
| **Docker Swarm**                       | Cluster management tool for Docker containers. | `docker swarm init` <br> `docker service create --name web nginx` |
| **Kubernetes Setup**                   | Kubernetes orchestrates containerized applications across multiple nodes. | `kubectl create deployment nginx --image=nginx` |
| **Ansible Setup**                      | Automates infrastructure provisioning, configuration management, and application deployment. | `ansible-playbook -i inventory setup.yml` |
| **Ansible Playbooks**                  | Define configurations and tasks to be executed on remote hosts in YAML format. | `- name: Install Apache <br>  apt: name=apache2 state=present` |
| **Cloud API Integration**              | Use APIs to interact programmatically with cloud services (e.g., AWS, Azure). | AWS SDK example: `aws.s3.putObject()` |
| **Cloud Data Center/Disaster Recovery**| Implement disaster recovery plans in the cloud, e.g., multi-region setup. | -                   |
| **High Availability and Auto-Scaling** | Automatically adjust resources (EC2 instances, databases) based on demand. | `aws autoscaling create-auto-scaling-group` |
| **Monitoring with Nagios**             | Monitor servers, network services, and applications. | `check_ping -H 192.168.1.1` |
| **Prometheus and Grafana**             | Collect metrics and visualize system performance. | `prometheus.yml` <br> `grafana` dashboard setup |
| **Auto-scaling, Auto-healing**         | Auto-scaling groups and health checks ensure application availability. | AWS Auto-Scaling: `aws autoscaling create-auto-scaling-group` |
| **Continuous Integration with Jenkins**| Automate building, testing, and deployment of code with Jenkins pipelines. | Jenkinsfile setup: `sh 'docker build'` |
| **Terraform for Cloud Infrastructure** | Provision, manage, and automate cloud resources (AWS, Azure, GCP). | `terraform apply` |
| **Terraform Remote State**             | Manage Terraform state remotely (e.g., using S3). | `backend "s3" { bucket = "my-tf-state" key = "terraform.tfstate" region = "us-west-2" }` |
| **Agile and DevOps Collaboration**     | Agile sprints, Scrum boards, and Kanban work well with the iterative nature of DevOps. | Scrum, Kanban boards |
| **Microservices Deployment**          | Microservices architecture involves creating independent services that are deployed separately. | -                   |

---

### **Last-Minute Tips**
- **Practice Commands**: Run `terraform apply`, `docker build`, `kubectl` commands to get comfortable.
- **Understand Core Concepts**: Be clear on the purpose of each DevOps tool (CI/CD, Jenkins, Docker, Kubernetes, Terraform).
- **Focus on Automation**: Emphasize the importance of automation in all areas: infrastructure (Terraform), deployment (Jenkins, Docker), and configuration (Ansible).
- **Real-Time Scenarios**: Think through how cloud services, container orchestration, and monitoring tools work together in a real-world DevOps pipeline.
- **Keep Calm & Stay Confident**: Focus on your strengths—whether it's infrastructure automation, containers, or cloud management.

---

