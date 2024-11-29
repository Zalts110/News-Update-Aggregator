# Use an official Python runtime as the base image
FROM python:3.9-slim

RUN apt-get update && apt-get install -y wget unzip \
    && apt-get clean

# Install Dapr CLI
RUN wget -q https://github.com/dapr/cli/releases/download/v1.11.0/dapr_linux_amd64.tar.gz \
    && tar -xvf dapr_linux_amd64.tar.gz \
    && mv dapr /usr/local/bin \
    && rm dapr_linux_amd64.tar.gz

RUN dapr init --runtime-version 1.11.0 --slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY . /app/

RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that the service will run on
EXPOSE 5002

# Set the environment variable for Dapr
ENV DAPR_HTTP_PORT=3500

# Run the application using Dapr
CMD ["dapr", "run", "--app-id", "notification_service", "--app-port", "5002", "--resources-path", "./components", "--log-level", "debug", "--", "python", "app.py"]
