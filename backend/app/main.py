from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from . import models, schemas, database
from typing import List

app = FastAPI(title="Lab Optimization Survey")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create database tables
models.Base.metadata.create_all(bind=database.engine)

@app.get("/api/form-config")
async def get_form_config():
    """Return form configuration"""
    return {
        "title": "Lab Optimization Survey",
        "fields": [
            {
                "type": "text",
                "label": "Lab Name",
                "name": "lab_name",
                "placeholder": "Enter lab name",
                "required": True
            },
            {
                "type": "select",
                "label": "Optimization Type",
                "name": "optimization_type",
                "options": [
                    {"value": "algorithm", "label": "Algorithm Optimization"},
                    {"value": "hardware", "label": "Hardware Optimization"},
                    {"value": "process", "label": "Process Optimization"}
                ],
                "required": True
            },
            {
                "type": "textarea",
                "label": "Description",
                "name": "description",
                "placeholder": "Describe the optimization details",
                "required": True
            },
            {
                "type": "number",
                "label": "Improvement (%)",
                "name": "improvement",
                "placeholder": "Enter improvement percentage",
                "required": True
            },
            {
                "type": "select",
                "label": "Optimization Goal",
                "name": "objective_type",
                "options": [
                    {"value": "maximize", "label": "Maximize"},
                    {"value": "minimize", "label": "Minimize"}
                ],
                "required": True
            },
            {
                "type": "text",
                "label": "Optimization Target",
                "name": "objective_target",
                "placeholder": "Enter optimization target (e.g., efficiency)",
                "required": True
            },
            {
                "type": "json_editor",
                "label": "Parameters",
                "name": "parameters",
                "placeholder": "Define parameter ranges",
                "required": True,
                "example": {
                    "temperature": {"min": 20, "max": 80, "step": 5},
                    "pressure": {"min": 1, "max": 10, "step": 0.5}
                }
            },
            {
                "type": "json_editor",
                "label": "Constraints",
                "name": "constraints",
                "placeholder": "Define constraints",
                "required": True,
                "example": {
                    "total_flow": {"type": "equality", "value": "x + y = 1"},
                    "temperature": {"type": "inequality", "value": "T <= 100"}
                }
            }
        ]
    }

@app.post("/api/submit-form", response_model=schemas.OptimizationFormResponse)
async def submit_form(form: schemas.OptimizationFormCreate, db: Session = Depends(database.get_db)):
    """Handle form submission"""
    db_form = models.OptimizationForm(
        lab_name=form.lab_name,
        optimization_type=form.optimization_type,
        description=form.description,
        improvement=form.improvement,
        objective=form.objective.dict(),
        parameters=form.parameters.dict(),
        constraints=form.constraints.dict()
    )
    db.add(db_form)
    db.commit()
    db.refresh(db_form)
    return db_form

@app.get("/api/forms", response_model=List[schemas.OptimizationFormResponse])
async def get_forms(db: Session = Depends(database.get_db)):
    """Get all submitted forms"""
    return db.query(models.OptimizationForm).all() 