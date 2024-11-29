FROM python:3.11-slim

RUN apt-get update && apt-get install -y wget unzip \
    && apt-get clean

# Install Dapr CLI
RUN wget -q https://github.com/dapr/cli/releases/download/v1.11.0/dapr_linux_amd64.tar.gz \
    && tar -xvf dapr_linux_amd64.tar.gz \
    && mv dapr /usr/local/bin \
    && rm dapr_linux_amd64.tar.gz

RUN dapr init --runtime-version 1.11.0 --slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

# Step 7: Run the application using Dapr
CMD ["dapr", "run", "--app-id", "user_service", "--app-port", "5000", "--", "python", "app.py"]
