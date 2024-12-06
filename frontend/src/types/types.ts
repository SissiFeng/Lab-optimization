export interface LaboratoryInfo {
  labName: string;
  experimentName: string;
  duration: string;
  sop: string;
  equipment: string;
}

export interface PersonnelRequirement {
  requirements: string;
  qualifications: string;
}

export interface OptimizationObjective {
  name: string;
  unit: string;
  description: string;
  priority: 'high' | 'medium' | 'low';
}

export interface FormData {
  laboratoryInfo: LaboratoryInfo;
  personnelRequirements: PersonnelRequirement;
  objectives: OptimizationObjective[];
} 