# Postgres and PgAdmin

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
   Open your browser and go to `http://localhost:8080`. Log in using the credentials configured in your `docker-compose.yml` file (e.g., `PGADMIN_DEFAULT_EMAIL` and `PGADMIN_DEFAULT_PASSWORD`).

3. **Add a Server in pgAdmin**:
   - Host: `pgdatabase`
   - Username and password: Use the values from your `docker-compose.yml` file (e.g., `POSTGRES_USER` and `POSTGRES_PASSWORD`).

4. **Run the Ingestion Script**:
   Build and run the container that executes the `ingest_data.py` script:
   ```bash
   docker build -t ingest-script .
   ```
   Here we have tagged the image as ingest-script. The script ask for several variables when you run it:
    ```bash
   docker run -it  --network=docker_sql_default ingest-script  --user=root  --password=root  --host=pgdatabase  --port=5432  --db=ny_taxi --table_name=yellow_taxi_trips --url=${URL}
   ```
    Note that the network name comes from the directory where the `docker-compose.yml` file is.
---

## Resetting the Project

To reset the project, remove all Docker volumes and ensure the database starts fresh:

1. **Stop the Services**:
   ```bash
   docker-compose down
   ```

2. **Remove Docker Volumes**:
   List all volumes:
   ```bash
   docker volume ls
   ```
   Remove the volumes associated with your project:
   ```bash
   docker volume rm $(docker volume ls -q)
   ```
   Alternatively, if you know the specific volume names, remove them individually:
   ```bash
   docker volume rm volume_name_here
   ```
3. **Delete content of the volumes**
    If you want the tables to be empty you will have to delete the contents of directories `ny_taxi_postgres_data` and `data_pgadmin`

4. **Start the Services Again**:


---