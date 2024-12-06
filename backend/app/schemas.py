from pydantic import BaseModel, Field
from typing import Dict, Optional
from datetime import datetime

class Parameter(BaseModel):
    min: float
    max: float
    step: float = 0.1

class Constraint(BaseModel):
    type: str
    value: str

class OptimizationConfig(BaseModel):
    type: str = Field(..., pattern="^(maximize|minimize)$")
    target: str

class OptimizationFormCreate(BaseModel):
    lab_name: str
    optimization_type: str
    description: str
    improvement: float
    objective: OptimizationConfig
    parameters: Dict[str, Parameter]
    constraints: Dict[str, Constraint]

class OptimizationFormResponse(OptimizationFormCreate):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True 