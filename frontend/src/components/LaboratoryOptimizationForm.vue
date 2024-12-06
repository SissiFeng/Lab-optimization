<template>
  <div class="max-w-7xl mx-auto px-4 py-8">
    <div class="text-center mb-8">
      <h1 class="text-3xl font-bold text-gray-900 mb-2">Laboratory Optimization Form</h1>
      <p class="text-blue-600">Configure your laboratory optimization parameters and constraints.</p>
    </div>
    
    <div class="space-y-6">
      <LaboratoryInformation v-model="formData.laboratoryInfo" />
      <PersonnelRequirements v-model="formData.personnelRequirements" />
      <OptimizationObjectives v-model="formData.objectives" />

      <div class="flex justify-end">
        <button 
          @click="saveForm"
          class="bg-blue-600 hover:bg-blue-700 text-white px-6 py-2 rounded-md text-sm font-medium transition-colors"
        >
          Save Form
        </button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive } from 'vue';
import type { FormData } from '../types/types';
import LaboratoryInformation from './LaboratoryInformation.vue';
import PersonnelRequirements from './PersonnelRequirements.vue';
import OptimizationObjectives from './OptimizationObjectives.vue';

const formData = reactive<FormData>({
  laboratoryInfo: {
    labName: '',
    experimentName: '',
    duration: '',
    sop: '',
    equipment: ''
  },
  personnelRequirements: {
    requirements: '',
    qualifications: ''
  },
  objectives: []
});

const saveForm = async () => {
  try {
    console.log('Form data:', formData);
    const response = await fetch('/api/optimization', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(formData)
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const result = await response.json();
    console.log('Save successful:', result);
    alert('Form saved successfully!');
  } catch (error) {
    console.error('Error saving form:', error);
    alert('Failed to save form. Please try again.');
  }
};
</script>
  
  