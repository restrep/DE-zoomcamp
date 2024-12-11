# Postgres and PgAdmin

# Project Setup and Reset Instructions

This guide explains how to run the project, reset it by deleting all Docker volumes, and ensure the PostgreSQL database starts with no tables.

## Prerequisites

Ensure you have the following installed:
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

---

## Running the Project

1. **Start the Services**:
   Run the following command in the project directory (where the `docker-compose.yml` file is located):
   ```bash
   docker-compose up -d
   ```
   This starts the `pgdatabase` (PostgreSQL) and `pgadmin` services.

2. **Access pgAdmin**:
   Open your browser and go to `http://localhost:5050`. Log in using the credentials configured in your `docker-compose.yml` file (e.g., `PGADMIN_DEFAULT_EMAIL` and `PGADMIN_DEFAULT_PASSWORD`).

3. **Add a Server in pgAdmin**:
   - Host: `pgdatabase`
   - Username and password: Use the values from your `docker-compose.yml` file (e.g., `POSTGRES_USER` and `POSTGRES_PASSWORD`).

4. **Run the Ingestion Script**:
   Build and run the container that executes the `ingest_data.py` script:
   ```bash
   docker build -t ingest-script .
   docker run --network=project_default ingest-script
   ```
   Replace `project_default` with the name of the Docker network if different.

---