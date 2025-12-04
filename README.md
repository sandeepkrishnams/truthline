# Truthline

A full-stack application with React frontend and FastAPI backend.

## Project Structure

```
truthline/
├── backend/          # FastAPI backend
├── frontend/         # React + TypeScript frontend
├── docker-compose.yml # Docker Compose configuration
└── README.md         # This file
```

## Quick Start with Docker (Recommended)

The easiest way to get started is using Docker Compose:

```bash
# Start all services (PostgreSQL, Redis, Backend, Frontend)
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

Services will be available at:
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs
- **PostgreSQL**: localhost:5432
- **Redis**: localhost:6379

For detailed Docker instructions, see [DOCKER.md](./DOCKER.md).

## Getting Started (Local Development)

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Copy `.env.example` to `.env` and update with your values:
```bash
cp .env.example .env
```

5. Run the development server:
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

The app will be available at `http://localhost:5173`

## Development

- Backend runs on port `8000`
- Frontend runs on port `5173`
- Frontend is configured to proxy API requests to the backend

## Technologies

- **Backend**: FastAPI, Python, Uvicorn, SQLAlchemy, PostgreSQL, Redis
- **Frontend**: React, TypeScript, Vite
- **Infrastructure**: Docker, Docker Compose, Nginx

