This project is a simple calculator application that consists of a React web front-end and a FastAPI back-end using a MySQL database for storage.
The application is containerized using Docker and can be deployed easily.

Deployment
Prerequisites
Make sure you have Docker and Docker Compose installed on your machine.

Docker Installation Guide
Docker Compose Installation Guide
Getting Started
Clone the repository:
```bash
git clone https://github.com/your-username/calculator-app.git
```
Navigate to the project directory:

```bash
cd calculator-app
```
Build and run the application using Docker Compose:

```bash
docker-compose up -d
```
This command will build Docker images, start containers, and configure the network. The application will be available at http://localhost:3000.

Accessing the Application
Web Front-end:

Open your browser and go to http://localhost:3000.
API Documentation:

The FastAPI documentation is available at http://localhost:8000/docs.
Stopping the Project
To stop the application and clean up Docker resources, use the following command:

```bash
docker-compose down
```
