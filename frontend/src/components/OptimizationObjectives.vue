<template>
    <div class="border-t-4 border-t-green-500 shadow-lg bg-white rounded-lg overflow-hidden">
      <div class="bg-gradient-to-r from-green-100 to-green-50 px-6 py-4 flex justify-between items-center">
        <h2 class="flex items-center text-green-800 text-xl font-semibold">
          <TargetIcon class="mr-2 h-5 w-5" />
          Optimization Objectives
        </h2>
        <button @click="addObjective" class="bg-white hover:bg-green-50 text-green-600 border border-green-300 px-3 py-1 rounded-md flex items-center text-sm font-medium">
          <PlusIcon class="mr-1 h-4 w-4" />
          Add Objective
        </button>
      </div>
      <div class="space-y-6 p-6">
        <div v-for="(objective, index) in objectives" :key="index" class="rounded-lg border border-green-200 p-4 bg-green-50">
          <div class="flex items-start justify-between">
            <div class="grid flex-1 gap-4">
              <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div class="space-y-2">
                  <label :for="'objective-name-' + index" class="text-green-700 font-medium">Name</label>
                  <input v-model="objective.name" :id="'objective-name-' + index" type="text" placeholder="Enter objective name" 
                         class="w-full px-3 py-2 border border-green-200 rounded-md focus:outline-none focus:border-green-500" />
                </div>
                <div class="space-y-2">
                  <label :for="'objective-unit-' + index" class="text-green-700 font-medium">Unit</label>
                  <input v-model="objective.unit" :id="'objective-unit-' + index" type="text" placeholder="e.g., mg/L, °C" 
                         class="w-full px-3 py-2 border border-green-200 rounded-md focus:outline-none focus:border-green-500" />
                </div>
              </div>
              <div class="space-y-2">
                <label :for="'objective-description-' + index" class="text-green-700 font-medium">Description</label>
                <textarea v-model="objective.description" :id="'objective-description-' + index" placeholder="Describe the optimization objective" 
                          class="w-full px-3 py-2 border border-green-200 rounded-md focus:outline-none focus:border-green-500"></textarea>
              </div>
              <div class="space-y-2">
                <label :for="'objective-priority-' + index" class="text-green-700 font-medium">Priority</label>
                <select v-model="objective.priority" :id="'objective-priority-' + index" 
                        class="w-full px-3 py-2 border border-green-200 rounded-md focus:outline-none focus:border-green-500">
                  <option value="high">High</option>
                  <option value="medium">Medium</option>
                  <option value="low">Low</option>
                </select>
              </div>
            </div>
            <button @click="removeObjective(index)" class="text-green-600 hover:text-green-700 hover:bg-green-100 p-1 rounded-full">
              <XMarkIcon class="h-5 w-5" />
            </button>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup lang="ts">
  import { ref, watch } from 'vue';
  import { TagIcon as TargetIcon, PlusIcon, XMarkIcon } from '@heroicons/vue/24/outline';
  import type { OptimizationObjective } from '../types/types';
  
  const props = defineProps<{
    modelValue: OptimizationObjective[]
  }>();
  
  const emit = defineEmits<{
    (e: 'update:modelValue', value: OptimizationObjective[]): void
  }>();
  
  const objectives = ref<OptimizationObjective[]>(props.modelValue);
  
  watch(objectives, (newValue) => {
    emit('update:modelValue', newValue);
  }, { deep: true });
  
  const addObjective = () => {
    objectives.value.push({ 
      name: '', 
      unit: '', 
      description: '', 
      priority: 'medium' 
    });
  };
  
  const removeObjective = (index: number) => {
    objectives.value.splice(index, 1);
  };
  </script>
  
  