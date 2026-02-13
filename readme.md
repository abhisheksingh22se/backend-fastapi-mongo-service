# 🚀 Scalable Data Management API (FastAPI + MongoDB)

A high-performance, asynchronous REST API designed for high-throughput data ingestion and management. This project demonstrates a production-grade architecture using **FastAPI** for non-blocking I/O, **MongoDB** for flexible document storage, and **Docker** for containerized deployment.

While currently configured for **Healthcare Patient Records**, the architecture is domain-agnostic and optimized for concurrent write operations.

---

## 🏗️ Key Technical Features

### 1. High-Throughput Asynchronous I/O
- Leverages Python's `async`/`await` syntax with the **Motor** driver to handle concurrent requests without blocking the event loop.
- Significantly outperforms traditional synchronous frameworks in I/O-bound tasks.

### 2. Self-Healing Infrastructure
- **Docker Healthchecks**: The API container creates a dependency on the Database container's health status.
- **Auto-Recovery**: Prevents the API from crashing or serving errors until the database is back online (`condition: service_healthy`).

### 3. Strict Schema Validation (Data Integrity)
- Implements **Pydantic v2** models to enforce strict typing and validation rules.
- Malformed data is rejected before it ever reaches the database layer.

### 4. Optimized Containerization (DevSecOps)
- Uses **Multi-Stage Docker Builds** to separate build dependencies from the runtime environment.
- **Result:** Reduces final image size by ~60% and minimizes the security attack surface.

---

## 🛠️ Tech Stack

- **Framework**: Python FastAPI (Asynchronous) 
- **Database**: MongoDB (NoSQL) 
- **Validation**: Pydantic v2 
- **Containerization**: Docker & Docker Compose
- **Visualization**: Mongo Express & Jinja2 Templates

---

## 📁 Architecture Structure

```text
scalable-api/
├── app/
│   ├── models.py           # Pydantic data schemas (Strict Validation)
│   ├── database.py         # Async MongoDB connection (Motor)
│   ├── templates/          # Jinja2 Dashboard Templates
│   └── main.py             # Application entry point
├── Dockerfile              # Multi-stage build definition
├── docker-compose.yml      # Orchestration with Healthchecks
└── requirements.txt
```

---

## 🛠️ Setup Instructions

### 1. Environment Variables

Create a `.env` file in the root directory:
```text
MONGO_URL=mongodb://admin:password@mongodb:27017/
MONGO_DB=hospital
MONGO_USER=admin
MONGO_PASSWORD=password
```
Update this to match your MongoDB connection string — whether it's local, in Docker, or hosted.

### 2. Run with Docker Compose
This spins up the API, MongoDB, and Mongo Express in a private network.
```bash
docker-compose up --build -d
```

### 3. Verify Deployment
* API Dashboard: http://localhost:8000
* API Documentation (Swagger UI): http://localhost:8000/docs
* Database GUI (Mongo Express): http://localhost:8081

## 🧪 API Endpoints

| Method | Endpoint  | Type   | Description                                                  |
|--------|-----------|--------|--------------------------------------------------------------|
| GET    | `/`       | Async  | Renders the real-time data dashboard with system status.     |
| POST   | `/add`    | Async  | Ingests new patient records with strict Pydantic validation. |
| GET    | `/docs`   | Static | Swagger UI for interactive API testing.                      |

---

## 📸 Proof of Concepts (Technical Evidence)

This section provides visual verification of the architectural claims made in the project documentation and resume.

### 1. Self-Healing & Service Orchestration
* **Feature:** Docker Healthchecks & `depends_on` conditions.
* **Evidence:** The screenshot below shows the API container in a `waiting` state until the MongoDB health check returns `healthy`, preventing connection-refused exceptions during startup.

![Self Healing Evidence](screenshots/healthcheck_proof.png)

### 2. Strict Schema Validation (Pydantic v2)
* **Feature:** Data Integrity Layer.
* **Evidence:** Verification of the API rejecting malformed JSON payloads (e.g., age > 150 or invalid gender strings) with a `422 Unprocessable Entity` response, ensuring only "clean" data hits the persistence layer.

![Validation Error](screenshots/validation_error.png)

### 3. Asynchronous Data Persistence
* **Feature:** Non-blocking MongoDB operations via Motor.
* **Evidence:** A view of the **Mongo Express GUI** confirming successful document insertion and persistence within the `hospital` database collection.

![Data Persistence](screenshots/mongo_express_data.png)

### 4. Optimized Multi-Stage Build
* **Feature:** Reduced Attack Surface & Image Size.
* **Evidence:** Terminal output of `docker images` showing the production image size reduced by ~60% compared to a standard single-stage build.

![Docker Image Size](screenshots/docker_image_size.png)
