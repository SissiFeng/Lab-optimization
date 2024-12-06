# Laboratory Optimization Form

A web application for configuring and managing laboratory optimization experiments.

![Project Screenshot](docs/images/screenshot.png)

## Features
- Dynamic form for laboratory experiment configuration
- Personnel requirements management
- Optimization objectives tracking
- JSON data export
- Database storage

## Quick Start

### Using Docker (Recommended)
```bash
# Clone the repository
git clone https://github.com/SissiFeng/Lab-optimization.git
cd Lab-optimization

# Start the application
docker-compose up
```

Access the application at:
- Frontend: http://localhost:5173
- API Documentation: http://localhost:8000/docs

### Manual Setup

1. Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

2. Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Environment Variables

Create `.env` file in backend directory:
```env
DATABASE_URL=postgresql://user:password@localhost/dbname
SECRET_KEY=your-secret-key
DEBUG=True
```

## API Documentation

API documentation is available at `http://localhost:8000/docs` when running the backend server.

## Project Structure
```
.
├── frontend/               # Vue.js frontend
│   ├── src/
│   │   ├── components/    # Vue components
│   │   └── types/        # TypeScript types
│   └── ...
└── backend/               # FastAPI backend
    ├── app/
    │   ├── models.py     # Database models
    │   └── main.py       # API endpoints
    └── ...
```

## Data Storage

The application stores data in two ways:
1. JSON files in `backend/data/optimizations/`
2. PostgreSQL database (when configured)

## Development

See [Development Guide](docs/DEVELOPMENT.md) for detailed information.
