from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import json
from datetime import datetime
import os

app = FastAPI()

# Data model definitions
class LaboratoryInfo(BaseModel):
    labName: str
    experimentName: str
    duration: str
    sop: str
    equipment: str

class PersonnelRequirement(BaseModel):
    requirements: str
    qualifications: str

class OptimizationObjective(BaseModel):
    name: str
    unit: str
    description: str
    priority: str

class OptimizationForm(BaseModel):
    laboratoryInfo: LaboratoryInfo
    personnelRequirements: PersonnelRequirement
    objectives: List[OptimizationObjective]

@app.post("/api/optimization")
async def create_optimization(form: OptimizationForm):
    try:
        # Generate unique filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"optimization_{timestamp}.json"
        
        # Ensure directory exists
        os.makedirs("data/optimizations", exist_ok=True)
        
        # Save as JSON file
        file_path = f"data/optimizations/{filename}"
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(form.dict(), f, ensure_ascii=False, indent=2)
            
        # TODO: Save to database
        # save_to_database(form)
            
        return {
            "status": "success",
            "message": "Optimization form saved successfully",
            "file": filename
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 获取所有优化记录
@app.get("/api/optimizations")
async def get_optimizations():
    try:
        optimizations = []
        directory = "data/optimizations"
        
        if os.path.exists(directory):
            for filename in os.listdir(directory):
                if filename.endswith(".json"):
                    with open(os.path.join(directory, filename), "r", encoding="utf-8") as f:
                        data = json.load(f)
                        optimizations.append({
                            "id": filename.replace("optimization_", "").replace(".json", ""),
                            "data": data
                        })
                        
        return optimizations
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 获取单个优化记录
@app.get("/api/optimization/{optimization_id}")
async def get_optimization(optimization_id: str):
    try:
        file_path = f"data/optimizations/optimization_{optimization_id}.json"
        
        if not os.path.exists(file_path):
            raise HTTPException(status_code=404, detail="Optimization not found")
            
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 