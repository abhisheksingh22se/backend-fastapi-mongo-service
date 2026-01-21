# 🏥 FastAPI MongoDB - Hospital Patient API

A simple CRUD application using **FastAPI** with **MongoDB** as the backend database, containerized using **Docker** and orchestrated with **Docker Compose**. Includes a minimal UI for layman access and optional integration with **Mongo Express**.

---

## 🚀 Features

- Create and retrieve patient records
- Built with FastAPI for high-performance REST APIs
- MongoDB for document-based data storage
- Uses Pydantic v2 for data validation
- Minimal frontend using Jinja2 templating
- Mongo Express for GUI-based MongoDB visualization
- Docker Compose for multi-container orchestration
- Persistent data storage using Docker volumes
- Environment variable support using `.env`
- Fully containerized and CI/CD ready

---

## 📁 Project Structure
```text
fastapi-mongo/
├── app/
│   ├── __init__.py
│   ├── main.py               # FastAPI app routes
│   ├── models.py             # Pydantic models
│   ├── database.py           # MongoDB connection
│   ├── templates/            # HTML templates (e.g., index.html)
│   ├── static/               # (Optional) CSS/JS assets
│   └── .env                  # MongoDB connection string
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## 🛠️ Setup Instructions

### 🔧 Local Setup (With Virtual Environment)

```bash
git clone git@github.com:abhisheksingh22se/my-project.git
cd my-project/fastapi-mongo
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload 
```
Visit: http://localhost:8000

---

## 🧪 API Endpoints

| Method | Endpoint       | Description                 |
|--------|----------------|-----------------------------|
| GET    | `/`            | Welcome message             |
| POST   | `/patients`    | Create new patient entry    |
| GET    | `/patients`    | Get all patient entries     |

Use Swagger UI to interact with the API:  
👉 [`http://localhost:8000/docs`](http://localhost:8000/docs)

---

## 🔐 Environment Variables

Create a `.env` file in the root directory:
```text
MONGO_URL=mongodb://admin:password@mongodb:27017/
MONGO_DB=hospital
```
Update this to match your MongoDB connection string — whether it's local, in Docker, or hosted.

---

## 🐳 Docker Compose Setup

### Step 1: Create `.env` file
Inside fastapi-mongo/.env:
```bash
MONGO_URL=mongodb://admin:password@mongodb:27017/
MONGO_DB=hospital
```

### Step 2: Build and Run
```bash
docker-compose up --build
```
* FastAPI: http://localhost:8000
* Mongo Express: http://localhost:8081

### Step 3: Tear Down (Optional)
```bash
docker-compose down -v
```
This will also remove persistent MongoDB data stored in Docker volume.

---

## 📦 Requirements
Install all dependencies:
```bash
pip install -r requirements.txt
```
---

## 🧰 Tech Stack

FastAPI – API framework
MongoDB – NoSQL database
Mongo Express – Web GUI for MongoDB
Uvicorn – ASGI server
Pydantic v2 – Data validation
Docker – Containerization
Docker Compose – Multi-container orchestration
Jinja2 – Templating for minimal UI
python-dotenv – Environment variable management

---

## 🧠 Future Improvements
* Add form validation in UI
* Implement update/delete routes
* Add authentication support
* Deploy to cloud (AWS EC2/ECS or Azure)

