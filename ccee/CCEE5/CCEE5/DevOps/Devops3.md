DevOps
---

| **Topic**                                                   | **Description**                                                                                                                                          | **Key Concepts and Tasks**                                                                                                                                                                                                                                                                                                           |
|-------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Introduction to AWS**                                      | AWS (Amazon Web Services) is a comprehensive cloud computing platform providing a variety of infrastructure services to help with cloud storage, computing, and networking. | - **Cloud Platform**: AWS offers scalable, pay-as-you-go services, making it ideal for developers and businesses.<br> - **Global Reach**: AWS has data centers around the world, providing a global infrastructure.<br> - **Broad Service Offering**: AWS offers a wide range of services including compute, storage, and networking solutions.                                    |
| **Services Provided by AWS**                                 | AWS provides a wide range of services such as EC2, Lambda, and S3 for running applications, managing infrastructure, and storing data.                      | - **EC2 (Elastic Compute Cloud)**: Scalable virtual machines that provide resizable compute capacity.<br> - **Lambda**: Serverless compute service that runs code in response to events.<br> - **S3 (Simple Storage Service)**: Scalable object storage for data storage and retrieval.<br> - **VPC (Virtual Private Cloud)**: Network setup for isolated cloud environments. |
| **Introduction to Virtual Private Cloud (VPC) Setup**        | VPC allows the creation of a private, isolated network within AWS. You can configure subnets, route tables, and network gateways to control traffic.         | - **VPC Overview**: A VPC enables you to launch AWS resources into a virtual network that you define.<br> - **Subnets**: Logical subdivisions of an IP network in a VPC.<br> - **Public & Private Subnets**: Public subnets have direct access to the internet, while private subnets are isolated.<br> - **Security**: Use security groups and network ACLs to control access.                                  |
| **Create AWS EC2 Instance**                                  | EC2 instances are virtual servers that provide computing capacity to run applications on AWS.                                                             | - **Launch EC2 Instance**: Use the AWS Management Console or CLI to create an EC2 instance.<br> - **Select AMI**: Choose the Amazon Machine Image (AMI) to define the OS and environment.<br> - **Configure Instance**: Select instance type, configure storage, and configure security groups.<br> - **Connect to EC2**: Use SSH for Linux instances or RDP for Windows instances to access EC2. |
| **Create AWS Lambda**                                        | AWS Lambda is a serverless compute service that executes your code in response to specific events without provisioning or managing servers.                 | - **Create Lambda Function**: Write a function in the AWS Management Console or upload your code.<br> - **Trigger Lambda**: Set up event sources such as S3 uploads or API Gateway requests to trigger Lambda.<br> - **Deploy Lambda**: AWS Lambda runs your code in response to events and scales automatically without server management.                      |
| **Create AWS S3 Bucket**                                     | AWS S3 provides scalable storage for storing and retrieving any amount of data at any time.                                                                | - **Create S3 Bucket**: In the AWS Management Console, create a new bucket by specifying a name and region.<br> - **Upload Objects**: Upload files (e.g., images, documents) to the S3 bucket.<br> - **Set Permissions**: Control access permissions using bucket policies or IAM roles.<br> - **Static Website Hosting**: S3 can also serve static websites.                               |
| **Create AWS VPC**                                           | A Virtual Private Cloud (VPC) allows the creation of a private network in AWS with full control over IP address range, subnets, routing, and security.      | - **VPC Creation**: Use the VPC wizard to create a new VPC.<br> - **Configure Subnets**: Create public and private subnets with IP address ranges.<br> - **Internet Gateway**: Attach an Internet Gateway to the VPC for internet access in the public subnet.<br> - **Route Tables**: Set up route tables to manage traffic between subnets and the internet.                                   |
| **Create a new VPC (ditiss-lab) with Public & Private Subnets** | Create a VPC named `ditiss-lab` with defined public and private subnets to enable specific network configurations.                                           | - **VPC CIDR Block**: Use 172.20.0.0/16 for the main VPC IP range.<br> - **Public Subnet CIDR Block**: Assign 172.20.5.0/24 for the public subnet.<br> - **Private Subnet CIDR Block**: Assign 172.20.10.0/24 for the private subnet.<br> - **Security Configuration**: Create security groups and NACLs for public and private instances.                              |
| **Create EC2 Instances in Public and Private Subnets**       | Deploy EC2 instances in the public and private subnets and test connectivity between them.                                                                  | - **Launch EC2 in Public Subnet**: Create an EC2 instance in the public subnet (which has internet access).<br> - **Launch EC2 in Private Subnet**: Create an EC2 instance in the private subnet (which does not have internet access).<br> - **Security Group**: Configure security groups to allow specific inbound and outbound traffic.                                        |
| **Install httpd on Private EC2 Instance and Test from Public EC2** | Install Apache HTTP Server on the EC2 instance in the private subnet and test the web service by accessing it from the public EC2 instance.                  | - **Install httpd**: SSH into the private EC2 instance and install the Apache HTTP server (`sudo yum install httpd` for Amazon Linux).<br> - **Start httpd Service**: Start the web server (`sudo service httpd start`).<br> - **Curl from Public EC2**: Use `curl <private_instance_ip>` from the public EC2 instance to test if the HTTP service is accessible from the private instance. |

---

### **Steps to Implement the Tasks:**

#### 1. **Create AWS EC2 Instance**:
   - **Step 1**: Go to the EC2 dashboard in AWS Console.
   - **Step 2**: Click on "Launch Instance".
   - **Step 3**: Select an Amazon Machine Image (AMI) and an instance type (e.g., t2.micro).
   - **Step 4**: Configure instance details (e.g., VPC, subnet, IAM role).
   - **Step 5**: Add storage (optional).
   - **Step 6**: Configure security group (allow SSH for Linux instances or RDP for Windows).
   - **Step 7**: Review and launch the instance.

#### 2. **Create AWS Lambda**:
   - **Step 1**: Go to the Lambda dashboard in AWS Console.
   - **Step 2**: Click on "Create Function".
   - **Step 3**: Choose the runtime (e.g., Node.js, Python).
   - **Step 4**: Write the function code or upload a ZIP file.
   - **Step 5**: Set the trigger (e.g., S3 event, API Gateway).
   - **Step 6**: Configure function permissions.
   - **Step 7**: Test the Lambda function using the test events.

#### 3. **Create AWS S3 Bucket**:
   - **Step 1**: Go to the S3 dashboard in AWS Console.
   - **Step 2**: Click on "Create Bucket".
   - **Step 3**: Provide a unique bucket name and select the region.
   - **Step 4**: Configure settings (e.g., versioning, logging).
   - **Step 5**: Set permissions (e.g., public access).
   - **Step 6**: Upload files to the bucket.

#### 4. **Create AWS VPC**:
   - **Step 1**: Go to the VPC dashboard in AWS Console.
   - **Step 2**: Click on "Create VPC" and specify the CIDR block (172.20.0.0/16).
   - **Step 3**: Create subnets within the VPC (Public subnet: 172.20.5.0/24, Private subnet: 172.20.10.0/24).
   - **Step 4**: Attach an Internet Gateway to the VPC for public internet access.
   - **Step 5**: Configure route tables and associate them with the subnets.

#### 5. **Deploy EC2 Instances in Public and Private Subnets**:
   - **Step 1**: Launch two EC2 instances as described above.
   - **Step 2**: One in the public subnet (with public IP) and one in the private subnet (without public IP).
   - **Step 3**: Configure security groups for each instance (e.g., allow HTTP/SSH in the public instance).
   
#### 6. **Test HTTP Service**:
   - **Step 1**: SSH into the private EC2 instance and install the `httpd` service (`sudo yum install httpd`).
   - **Step 2**: Start the service (`sudo service httpd start`).
   - **Step 3**: From the public EC2 instance, use `curl <private_instance_ip>` to test if the service is reachable from the public instance.

---

### **Conclusion**:
This summary and tasks outline how to use AWS to create, configure, and deploy a variety of resources, including **EC2**, **Lambda**, **S3**, and **VPC**. Setting up a VPC with both public and private subnets and deploying EC2 instances into those subnets allows for testing connectivity and web service configuration (HTTPD). Using these AWS resources, you can create scalable, secure cloud environments for application deployment.

---
---



### **Detailed Table of Concepts and Tasks**

| **Topic**                                                       | **Description**                                                                                                                                                    | **Key Concepts and Tasks**                                                                                                                                                                                                                                                                                                                                                                      |
|-----------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Version Control System (VCS)**                                | A version control system is a tool that helps developers manage changes to the source code and track project history. Git is a popular VCS.                           | - **Git**: A distributed version control system to manage code repositories.<br> - **Commit History**: Track changes and collaborate with teams.<br> - **Branching & Merging**: Helps with parallel development.<br> - **GitHub/Bitbucket/GitLab**: Platforms to host repositories.                                                                                                                                                                                                                           |
| **Infrastructure as Code (IaC)**                                | IaC is a method of managing and provisioning infrastructure using code instead of manual processes.                                                              | - **Terraform**: A tool to define infrastructure using configuration files.<br> - **AWS CloudFormation**: Another IaC tool for AWS resources.<br> - **Declarative vs Imperative**: Declarative defines the desired state, while imperative defines a sequence of actions.<br> - **Automation**: Automates deployment, scaling, and management of cloud infrastructure.                                                                                                                                                      |
| **Containerization with Docker**                                | Docker is a tool designed to create, deploy, and run applications in containers. Containers are lightweight, portable, and self-sufficient.                        | - **Docker Images**: Portable application templates.<br> - **Docker Containers**: Running instances of images.<br> - **Dockerfile**: Script used to build a Docker image.<br> - **Docker Compose**: A tool to define and manage multi-container Docker applications.<br> - **Docker Hub**: Public registry for storing Docker images.                                                                                                                                                    |
| **Container Orchestration: Kubernetes, Docker Swarm**           | These are tools for managing, scaling, and automating the deployment of containers across clusters of machines.                                                   | - **Kubernetes**: A robust platform for container orchestration, capable of automating deployment, scaling, and management.<br> - **Docker Swarm**: Docker's native clustering and orchestration tool for Docker containers.<br> - **K8s Nodes**: Master nodes and worker nodes.<br> - **Pods**: Smallest deployable unit in Kubernetes.<br> - **ReplicaSets**: Manage multiple replicas of containers.                                                                                                                                                                      |
| **Microservices Deployment**                                   | Microservices architecture involves breaking down applications into smaller, independent services that can be developed and deployed independently.               | - **Containers for Microservices**: Docker containers are ideal for deploying microservices.<br> - **Independent Scaling**: Each microservice can be scaled independently.<br> - **Service Communication**: Microservices communicate via APIs (REST, gRPC).<br> - **CI/CD Pipelines**: Continuous integration and deployment pipelines help automate the deployment of microservices.                                                                                                               |
| **Task: Create a Docker Image Using NGINX and Push to Docker Hub** | The task involves building an NGINX Docker image, pushing it to Docker Hub, and managing it via Docker Swarm with scaling replicas.                                  | - **Create Dockerfile for NGINX**: Create a basic Dockerfile that pulls from the official NGINX image.<br> - **Modify index.html**: Create or modify the `index.html` file for the web service.<br> - **Build Docker Image**: `docker build -t nginx-image .`.<br> - **Push Image to Docker Hub**: `docker push username/nginx-image`.<br> - **Create Docker Swarm Service**: `docker service create --name nginx-service --replicas 1 nginx-image`.<br> - **Scale Service**: Scale replicas to 10 using `docker service scale nginx-service=10`. <br> - **Update Service**: Modify `index.html` in the Docker image, push it to Docker Hub, and update the service with the new image using `docker service update --image nginx-image`. |
| **Configure Kubernetes with Master and Worker Nodes**          | Setting up a Kubernetes cluster with one master node and multiple worker nodes for container orchestration.                                                      | - **Kubernetes Master Node**: The central control point for the cluster, managing the API server, scheduler, controller manager, etc.<br> - **Kubernetes Worker Nodes**: Nodes that run applications (containers), managed by the master node.<br> - **Cluster Setup**: Use `kubeadm` or `minikube` to set up the cluster.<br> - **kubectl Commands**: Manage the cluster and deploy applications.<br> - **Create and Join Worker Nodes**: Use `kubeadm join` to add worker nodes to the master node. |

---

### **Steps for Practical Tasks**

#### 1. **Create a New Docker Image Using NGINX and Push to Docker Hub**:
   - **Step 1**: Create a new directory for the NGINX Docker image project and navigate to it:
     ```bash
     mkdir nginx-docker
     cd nginx-docker
     ```
   - **Step 2**: Create a `Dockerfile` with the following content:
     ```dockerfile
     FROM nginx
     COPY index.html /usr/share/nginx/html/index.html
     ```
   - **Step 3**: Create an `index.html` file:
     ```html
     <html>
         <head><title>My NGINX Web Page</title></head>
         <body><h1>Welcome to NGINX!</h1></body>
     </html>
     ```
   - **Step 4**: Build the Docker image:
     ```bash
     docker build -t yourdockerhubusername/nginx-image .
     ```
   - **Step 5**: Push the image to Docker Hub:
     ```bash
     docker push yourdockerhubusername/nginx-image
     ```

#### 2. **Create a Docker Swarm Service and Scale Replicas**:
   - **Step 1**: Initialize Docker Swarm mode (on the manager node):
     ```bash
     docker swarm init
     ```
   - **Step 2**: Create a service with one replica:
     ```bash
     docker service create --name nginx-service --replicas 1 yourdockerhubusername/nginx-image
     ```
   - **Step 3**: Scale the service to 10 replicas:
     ```bash
     docker service scale nginx-service=10
     ```
   - **Step 4**: Scale down to 2 replicas:
     ```bash
     docker service scale nginx-service=2
     ```

#### 3. **Update the Docker Service with a New Image**:
   - **Step 1**: Modify `index.html` (e.g., change the content):
     ```html
     <html>
         <head><title>Updated NGINX Page</title></head>
         <body><h1>Updated NGINX Web Page</h1></body>
     </html>
     ```
   - **Step 2**: Rebuild the Docker image:
     ```bash
     docker build -t yourdockerhubusername/nginx-image .
     ```
   - **Step 3**: Push the updated image to Docker Hub:
     ```bash
     docker push yourdockerhubusername/nginx-image
     ```
   - **Step 4**: Update the service to use the new image:
     ```bash
     docker service update --image yourdockerhubusername/nginx-image nginx-service
     ```

#### 4. **Configure Kubernetes with Master and Worker Nodes**:
   - **Step 1**: Install Kubernetes using `kubeadm` (on master node):
     ```bash
     sudo apt-get update && sudo apt-get install -y kubeadm kubelet kubectl
     sudo kubeadm init --pod-network-cidr=10.244.0.0/16
     ```
   - **Step 2**: Set up kubeconfig for kubectl:
     ```bash
     mkdir -p $HOME/.kube
     sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
     sudo chown $(id -u):$(id -g) $HOME/.kube/config
     ```
   - **Step 3**: Install a pod network (e.g., Flannel):
     ```bash
     kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml
     ```
   - **Step 4**: Join worker nodes to the master node using the command provided after `kubeadm init`:
     ```bash
     kubeadm join <master-node-ip>:6443 --token <token> --discovery-token-ca-cert-hash <hash>
     ```

---

### **Conclusion**:
This summary includes all major concepts, practical steps, and tools required to understand and implement **Version Control Systems**, **Infrastructure as Code**, **Containerization with Docker**, **Container Orchestration**, and **Microservices Deployment**. By following the steps, you can create and manage Docker containers, scale services using Docker Swarm, and configure a Kubernetes cluster for container orchestration. These practices are essential for modern cloud-native application deployment and management.

---
---

### **Detailed Notes on Ansible and Configuration Management**

Ansible is a popular open-source automation tool used for configuration management, application deployment, and task automation. The following sections cover key concepts and tasks related to setting up Ansible, writing playbooks, managing inventory, and utilizing roles for greater reusability.

---

### **1. Introduction to Ansible and Configuration Management**
- **Configuration Management**: This involves managing and automating the setup, maintenance, and deployment of systems and software.
  - **Ansible** is used to automate IT infrastructure management, ensuring consistency across servers.
  - Unlike traditional configuration management tools, Ansible is agentless, meaning no agent is needed on the target nodes.
  - It uses **SSH** for communication with the nodes and operates in a declarative manner to describe desired states.

---

### **2. Setting Up Ansible Environment**
#### **Install Ansible**
- **Prerequisites**: Ensure Python is installed on the machine.
- Install Ansible using `pip` (Python's package manager):
  ```bash
  pip install ansible
  ```
  Or on Ubuntu/Debian:
  ```bash
  sudo apt update
  sudo apt install ansible
  ```

#### **Configure SSH Keys for Passwordless Authentication**
- Ansible requires SSH access to remote nodes. Set up SSH key-based authentication:
  1. **Generate SSH Keys**:
     ```bash
     ssh-keygen -t rsa -b 4096
     ```
  2. **Copy SSH Public Key to Remote Nodes**:
     ```bash
     ssh-copy-id user@target-node
     ```
  3. **Test SSH Access**:
     ```bash
     ssh user@target-node
     ```

#### **Verify Ansible Setup**
- Once Ansible is installed and SSH keys are configured, you can verify the setup by running the `ping` module:
  ```bash
  ansible all -m ping
  ```
  This command will attempt to ping all nodes in your Ansible inventory, verifying that Ansible can communicate with them over SSH.

---

### **3. Ansible Playbooks and YAML Basics**
#### **What is a Playbook?**
- **Playbooks** are the core of Ansible’s automation. They define a series of tasks to be executed on remote nodes.
- **YAML** (YAML Ain't Markup Language) is used to write playbooks, providing a readable and human-friendly syntax.

#### **Structure of a Playbook**
- A playbook consists of **plays**, where each play targets a group of hosts and defines the tasks.
  ```yaml
  ---
  - name: Install and Start Apache Web Server
    hosts: webservers
    become: yes
    tasks:
      - name: Install Apache
        apt:
          name: apache2
          state: present
      - name: Start Apache service
        service:
          name: apache2
          state: started
  ```

#### **Basic Components of a Playbook**
1. **name**: Descriptive name of the play.
2. **hosts**: The group of nodes (from inventory) on which tasks will run.
3. **tasks**: A list of tasks to be performed.
4. **become**: Used to run tasks with elevated privileges (e.g., `sudo`).
5. **modules**: The actions to be taken, like `apt` for package management, `service` for managing services.

---

### **4. Writing and Executing Ansible Playbooks**
#### **Create a Playbook to Install a Web Server (Apache or Nginx)**
- Example of an Ansible playbook to install and start Apache:
  ```yaml
  ---
  - name: Install and Start Apache Web Server
    hosts: webservers
    become: yes
    tasks:
      - name: Install Apache
        apt:
          name: apache2
          state: present
      - name: Start Apache service
        service:
          name: apache2
          state: started
  ```
  This playbook installs Apache (`apache2` package) and ensures that the service is started.

#### **Verify the Setup**
- After running the playbook, verify that the Apache web server is running:
  1. **Run the Playbook**:
     ```bash
     ansible-playbook install_apache.yml
     ```
  2. **Access the Web Server**:
     Open a browser and enter the IP address of the server. You should see the default Apache web page if the server is correctly configured.

---

### **5. Managing Ansible Inventory**
#### **What is an Inventory?**
- The **inventory** file is where you define the target nodes (hosts) that Ansible will manage. The inventory can be static or dynamic.

#### **Static Inventory**
- A static inventory is a simple file that lists hostnames or IP addresses:
  ```ini
  [webservers]
  webserver1.example.com
  webserver2.example.com

  [dbservers]
  dbserver1.example.com
  ```
- You can organize hosts into groups like `webservers` or `dbservers`.

#### **Dynamic Inventory**
- For more advanced environments, dynamic inventories are used to retrieve host details from external sources (e.g., AWS, Azure, etc.). Ansible supports dynamic inventories via scripts or plugins.

---

### **6. Ansible Roles and Reusability**
#### **What are Roles?**
- **Roles** in Ansible are used to organize playbooks and tasks. They allow tasks, handlers, variables, templates, and files to be grouped and reused across multiple playbooks.
- Roles help in breaking down large playbooks into smaller, modular components.

#### **Create a Role for Database Installation**
1. **Directory Structure for Role**:
   ```bash
   roles/
   └── dbserver/
       ├── tasks/
       │   └── main.yml
       ├── handlers/
       │   └── main.yml
       ├── defaults/
       │   └── main.yml
       └── vars/
           └── main.yml
   ```

2. **Tasks in the Role**:
   - In `roles/dbserver/tasks/main.yml`, you can define tasks to install and configure a database (e.g., MySQL):
     ```yaml
     ---
     - name: Install MySQL Server
       apt:
         name: mysql-server
         state: present
     - name: Start MySQL Service
       service:
         name: mysql
         state: started
     ```

3. **Using the Role in a Playbook**:
   - In your main playbook, use the role like this:
     ```yaml
     ---
     - name: Install and Configure Database Server
       hosts: dbservers
       become: yes
       roles:
         - dbserver
     ```

4. **Apply the Playbook**:
   - To apply the role to your target nodes, use the following command:
     ```bash
     ansible-playbook install_db.yml
     ```

#### **Benefits of Roles and Reusability**
- **Modularization**: Roles enable you to separate tasks logically and reuse them across different playbooks.
- **Maintainability**: Easier to update or modify configurations, as roles encapsulate specific functionalities.
- **Consistency**: Helps ensure uniform configuration across multiple environments or nodes.

---

### **Conclusion**
Ansible is a powerful tool for automating infrastructure and application management. By setting up Ansible, writing playbooks, managing inventory, and utilizing roles, you can streamline tasks and improve scalability, maintainability, and efficiency. The steps mentioned above provide the foundation to get started with Ansible, allowing you to manage servers, deploy applications, and ensure consistent configurations across environments.

---

### **Summary of Key Steps**
1. **Set Up Ansible**: Install Ansible and configure SSH keys for communication.
2. **Create Playbooks**: Write YAML-based playbooks to automate tasks like installing software.
3. **Manage Inventory**: Define target nodes in an inventory file.
4. **Use Roles**: Break down tasks into reusable roles for better modularity and scalability.
