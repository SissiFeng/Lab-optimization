from sqlalchemy import Column, Integer, String, JSON, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class Optimization(Base):
    __tablename__ = "optimizations"
    
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    laboratory_info = Column(JSON)
    personnel_requirements = Column(JSON)
    file_path = Column(String)
    
    objectives = relationship("OptimizationObjective", back_populates="optimization")

class OptimizationObjective(Base):
    __tablename__ = "optimization_objectives"
    
    id = Column(Integer, primary_key=True)
    optimization_id = Column(Integer, ForeignKey("optimizations.id"))
    name = Column(String)
    unit = Column(String)
    description = Column(String)
    priority = Column(String)
    
    optimization = relationship("Optimization", back_populates="objectives") 