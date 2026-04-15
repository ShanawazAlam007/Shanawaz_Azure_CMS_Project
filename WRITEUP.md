# Project Writeup: VM vs Azure App Service

## Comparison
This project explored two different deployment strategies: using a Virtual Machine (VM) and using Azure App Service.

### Virtual Machine (Kali Linux)
Deploying the application on a VM (specifically Kali Linux in this case) required significant manual effort. For instance, Python 3.13 necessitated manual installation of specific drivers and dependency fixes to ensure the Flask application and its database connectors worked correctly. The responsibility for OS updates, security patches, and environment configuration lies entirely with the user.

### Azure App Service
Azure App Service provides a managed environment which simplifies the deployment process. It offers pre-configured stacks for Python, automatically handling many of the underlying infrastructure concerns. This allows developers to focus more on the application code rather than environment troubleshooting. The platform-as-a-service (PaaS) model provides built-in scaling, security, and integration with other Azure services like SQL Database and Blob Storage.
