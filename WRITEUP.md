# Project Writeup: CMS Deployment Analysis

This document provides a detailed comparison between two primary deployment strategies for our CMS application: Azure Virtual Machines (IaaS) and Azure App Service (PaaS).

## Comparative Analysis

The following table summarizes the key differences across four critical analysis points for both solutions.

| Analysis Point | Virtual Machine (VM) | Azure App Service |
| :--- | :--- | :--- |
| **Costs** | **Lower direct infrastructure cost but higher operational overhead.** You pay for the provisioned resources 24/7. Significant costs are hidden in manual labor for OS patching, security, and maintenance. | **Predictable, tiered pricing.** While the service cost might be slightly higher for equivalent compute, it eliminates the operational costs of managing the underlying server and OS. |
| **Scalability** | **Manual or complex.** Vertical scaling requires downtime. Horizontal scaling requires setting up Virtual Machine Scale Sets (VMSS) and Load Balancers manually, which is time-consuming to configure. | **Built-in and automated.** Supports both vertical and horizontal scaling with a few clicks. Auto-scaling rules can be set to automatically handle traffic spikes without manual intervention. |
| **Availability** | **User-managed.** High availability (99.9%+) requires manual configuration of Availability Sets or Zones and Load Balancers. A single VM has a lower SLA compared to managed services. | **High availability by default.** Azure manages the underlying infrastructure to ensure 99.95% availability. It handles hardware failures and platform updates automatically with minimal to no downtime. |
| **Workflow** | **High control, high effort.** Requires manual installation of Python, web servers (Nginx/Gunicorn), and database drivers. Developers must manage OS updates and security configurations. | **Streamlined and code-focused.** Uses a PaaS model where the environment is pre-configured for Python/Flask. Supports easy CI/CD integration (GitHub Actions, Azure DevOps) and automated deployment slots. |

## Chosen Solution: Azure App Service

For the deployment of this CMS application, **Azure App Service** is the recommended solution.

### Justification
I have chosen Azure App Service because it allows the development team to focus entirely on application logic rather than infrastructure management, significantly reducing the "Time to Market." Its built-in auto-scaling and high availability ensure the CMS remains responsive under varying loads without the manual configuration complexity required by a Virtual Machine. Additionally, the seamless integration with Azure SQL and Blob Storage provides a more cohesive and secure ecosystem for a modern web application.

## Scenarios for Reconsidering the Decision

While Azure App Service is ideal for standard web applications, certain circumstances would necessitate a shift toward a **Virtual Machine (VM)** approach.

### Why the Decision Might Change
A transition to a VM-based solution would be required if the CMS application needed low-level OS access, custom kernel modules, or specific third-party software that is not supported by the managed App Service environment. If the organization requires strict control over the underlying infrastructure for legacy compatibility or specific regulatory compliance that mandates physical isolation and custom security hardening at the OS level, a VM becomes the only viable option.

### Impact on Application and Infrastructure
| Requirement | Azure App Service (Current) | Virtual Machine (Alternative) |
| :--- | :--- | :--- |
| **Infrastructure Control** | Limited to app-level settings and scaling. | Full root/admin access to the OS and networking. |
| **App Requirements** | Standard Python/Flask stacks. | Any custom runtime or legacy binary dependencies. |
| **Maintenance Needs** | Managed by Azure (Security/OS patching). | Manual management of all updates and security patches. |

### Infrastructure vs. Application Needs
Choosing a VM would fundamentally change how the application is managed; the focus would shift from deploying code to maintaining the health and security of the entire server stack. To suit these requirements, I would need to implement robust Infrastructure as Code (IaC) tools like Terraform or Ansible to automate the manual setup processes. Additionally, the application architecture might need to be adjusted to include manual load-balancing logic and health probes that are otherwise handled natively by the App Service platform.
