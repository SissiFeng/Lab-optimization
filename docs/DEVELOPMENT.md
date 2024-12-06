# Development Guide

## Prerequisites
- Node.js >= 16
- Python >= 3.8
- PostgreSQL
- Docker (optional)

## Setup Development Environment

### Frontend Development
```bash
cd frontend
npm install
npm run dev
```

### Backend Development
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Project Structure

### Frontend
- `src/components/` - Vue components
- `src/types/` - TypeScript type definitions
- `src/App.vue` - Root component
- `src/main.js` - Entry point

### Backend
- `app/main.py` - FastAPI application and routes
- `app/models.py` - Database models
- `app/database.py` - Database configuration
- `app/schemas.py` - Pydantic models

## Database

### Setup PostgreSQL
1. Install PostgreSQL
2. Create database
3. Update `.env` file with database credentials

### Migrations
Currently using SQLAlchemy models directly. Migrations to be added in future updates.

## API Documentation

FastAPI automatically generates API documentation:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Testing

To be implemented:
- Frontend: Vue Test Utils + Vitest
- Backend: pytest 