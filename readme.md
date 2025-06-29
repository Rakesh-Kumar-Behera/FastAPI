#### To create a Virtual Environment
`python -m vnev <environment_name>`
#### to Activate virtual environment

`venv\Scripts\Activate`

Setup

1. Install Docker
2. Create account on Docker Hub
- Step 1 - Create a Dockerfile
- Step 2 - Build the docker image `docker build -t username/insurance-premium-api .`
- Step 3 - Login to Docker Hub `docker login`
- Step 4 - Push the image to Docker Hub `docker push username/insurance-premium-api`
- Step 5 - Pull the docker image
- Step 6 - Run the docker image locally `docker run -d -p 8000:8000 username/insurance-premium-api`

AWS Steps

1. create an EC2 instance
2. Connect to the EC2 instance
3. Run the following commands
     - a. `sudo apt-get update`
     - b. `sudo apt-get install -y docker.io`
     - с. `sudo systemctl start docker`
     - d. `sudo systemctl enable docker`
     - e. `sudo usermod -aG docker $USER`
     - f. `exit`
4. Restart a new connection to EC2 instance
5. Run the following commands
     - a. `docker pull username/insurance-premium-api:latest`
     - b. `docker run -p 8000:8000 username/insurance-premium-api`
