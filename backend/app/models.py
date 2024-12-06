from sqlalchemy import Column, Integer, String, JSON, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class OptimizationForm(Base):
    __tablename__ = "optimization_forms"

    id = Column(Integer, primary_key=True, index=True)
    lab_name = Column(String, index=True)
    optimization_type = Column(String)
    description = Column(String)
    improvement = Column(Float)
    
    # JSON fields for optimization configuration
    objective = Column(JSON)  # {type: "maximize/minimize", target: "target_name"}
    parameters = Column(JSON)  # {param_name: {min: value, max: value, step: value}}
    constraints = Column(JSON)  # {constraint_name: {type: "equality/inequality", value: expression}}
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow) 