# Personalized News Update Aggregator

This application aggregates news and updates based on user preferences. It provides a personalized news feed and delivers updates via email.

## Features

- Fetches news from a single API source.
- Delivers personalized updates via email based on user preferences.
- Microservice-based architecture with Dapr for service communication.
- Dockerized for easy deployment.

## Architecture

The system is built using microservices with the following components:

- **Orchestrator Service**: Handles orchestration and management of the news aggregation process.
- **User Service**: Manages user profiles, preferences, and interactions.
- **News Aggregation Service**: Fetches and processes news articles from an external API.
- **Notification Service**: Sends email updates to users.
- **MongoDB**: Stores user data and preferences.
- **RabbitMQ**: Used for pub/sub messaging between services.

The services are containerized using Docker Compose for streamlined deployment.

## Prerequisites

- Docker and Docker Compose installed on your machine.

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/your-repository-url.git
    cd personalized-news-aggregator
    ```

2. Build and start the Docker containers:
    ```bash
    docker-compose up --build
    ```

3. Access the RabbitMQ management UI (if needed) at `http://localhost:15672` using the credentials:
   - Username: `guest`
   - Password: `guest`

## Configuration

- The application uses environment variables for configuration. You can update these in the `docker-compose.yml` file:
  - MongoDB root username and password.
  - RabbitMQ username and password.

## Usage

- Users can set their preferences via the User Service.
- News articles are fetched by the News Aggregation Service at regular intervals.
- Summarized updates are sent via email through the Notification Service.

## Components Directory

Each service has its own directory with the following structure:

- `/components`: Dapr component configurations for pub/sub, state store, etc.
- `/app`: Application source code and dependencies.

## Key Endpoints

- **User Service**: `/users` (manage user profiles)
- **News Aggregation Service**: `/news` (fetch and view news articles)
- **Notification Service**: `/notification/send` (trigger email notifications)

## Future Enhancements

- Add support for additional news APIs.
- Implement Telegram-based notifications.
- Enhance summarization capabilities.

---

Developed using Dapr, Flask, and Docker. Contributions are welcome!
"""

