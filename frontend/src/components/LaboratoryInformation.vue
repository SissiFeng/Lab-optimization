<template>
  <div class="bg-white rounded-lg shadow-sm">
    <div class="flex items-center gap-2 p-4 border-b">
      <BeakerIcon class="h-5 w-5 text-blue-600" />
      <h2 class="text-blue-600 text-lg font-medium">Laboratory Information</h2>
    </div>
    <div class="p-6">
      <div class="grid grid-cols-2 gap-6 mb-6">
        <div>
          <label class="block text-blue-600 text-sm font-medium mb-2">Laboratory Name</label>
          <input
            v-model="labName"
            type="text"
            placeholder="Enter laboratory name"
            class="w-full px-3 py-2 border border-gray-200 rounded-md text-gray-700 focus:outline-none focus:border-blue-500"
          />
        </div>
        <div>
          <label class="block text-blue-600 text-sm font-medium mb-2">Experiment Name</label>
          <input
            v-model="experimentName"
            type="text"
            placeholder="Enter experiment name"
            class="w-full px-3 py-2 border border-gray-200 rounded-md text-gray-700 focus:outline-none focus:border-blue-500"
          />
        </div>
      </div>
      <div class="grid grid-cols-2 gap-6 mb-6">
        <div>
          <label class="block text-blue-600 text-sm font-medium mb-2">Experiment Duration</label>
          <input
            v-model="duration"
            type="text"
            placeholder="e.g., 2 weeks"
            class="w-full px-3 py-2 border border-gray-200 rounded-md text-gray-700 focus:outline-none focus:border-blue-500"
          />
        </div>
        <div>
          <label class="block text-blue-600 text-sm font-medium mb-2">SOP Reference</label>
          <input
            v-model="sop"
            type="text"
            placeholder="e.g., SOP-2024-001"
            class="w-full px-3 py-2 border border-gray-200 rounded-md text-gray-700 focus:outline-none focus:border-blue-500"
          />
        </div>
      </div>
      <div>
        <label class="block text-blue-600 text-sm font-medium mb-2">Required Equipment</label>
        <textarea
          v-model="equipment"
          placeholder="List required equipment (one per line)"
          rows="4"
          class="w-full px-3 py-2 border border-gray-200 rounded-md text-gray-700 focus:outline-none focus:border-blue-500"
        ></textarea>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue';
import { BeakerIcon } from '@heroicons/vue/24/outline';
import type { LaboratoryInfo } from '../types/types';

const props = defineProps<{
  modelValue: LaboratoryInfo
}>();

const emit = defineEmits<{
  (e: 'update:modelValue', value: LaboratoryInfo): void
}>();

const labName = ref(props.modelValue.labName);
const experimentName = ref(props.modelValue.experimentName);
const duration = ref(props.modelValue.duration);
const sop = ref(props.modelValue.sop);
const equipment = ref(props.modelValue.equipment);

watch([labName, experimentName, duration, sop, equipment], () => {
  emit('update:modelValue', {
    labName: labName.value,
    experimentName: experimentName.value,
    duration: duration.value,
    sop: sop.value,
    equipment: equipment.value
  });
}, { deep: true });
</script>
  
  