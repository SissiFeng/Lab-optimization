# Laboratory Optimization Form

A web application for configuring and managing laboratory optimization experiments.

## Features
- Dynamic form for laboratory experiment configuration
- Personnel requirements management
- Optimization objectives tracking
- JSON data export
- Database storage

## Tech Stack
- Frontend: Vue 3 + TypeScript + Tailwind CSS
- Backend: FastAPI + SQLAlchemy + PostgreSQL

## Getting Started

### Option 1: Using Docker (Recommended)

1. Install Docker and Docker Compose
2. Clone the repository:
```bash
git clone https://github.com/SissiFeng/Lab-optimization.git
cd Lab-optimization
```

3. Create and configure environment file:
```bash
cp backend/.env.example backend/.env
# Edit backend/.env with your database settings
```

4. Build and run with Docker:
```bash
docker-compose up --build
```

5. Access the application:
- Frontend: http://localhost:5173
- API Documentation: http://localhost:8000/docs

### Option 2: Manual Installation

#### Prerequisites
- Node.js >= 16
- Python >= 3.8
- PostgreSQL

#### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

#### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Usage

1. Fill in the Laboratory Information:
   - Laboratory Name
   - Experiment Name
   - Duration
   - SOP Reference
   - Required Equipment

2. Specify Personnel Requirements:
   - Requirements
   - Qualifications

3. Add Optimization Objectives:
   - Click "Add Objective" to add multiple objectives
   - For each objective, specify:
     - Name
     - Unit
     - Description
     - Priority

4. Submit the form:
   - Click "Save Form" to submit
   - The data will be saved as JSON and in the database
   - You can view saved forms through the API

## Development

### Project Structure
```
.
├── frontend/               # Vue.js frontend
│   ├── src/
│   │   ├── components/    # Vue components
│   │   ├── types/        # TypeScript types
│   │   └── ...
│   └── ...
└── backend/               # FastAPI backend
    ├── app/
    │   ├── models.py     # Database models
    │   ├── main.py       # API endpoints
    │   └── ...
    └── ...
```

## API Documentation
API documentation is available at `http://localhost:8000/docs` when running the backend server.
