<template>
  <div class="bg-white rounded-lg shadow-sm">
    <div class="flex items-center gap-2 p-4 border-b">
      <UsersIcon class="h-5 w-5 text-purple-600" />
      <h2 class="text-purple-600 text-lg font-medium">Personnel Requirements</h2>
    </div>
    <div class="p-6">
      <div class="grid grid-cols-2 gap-6">
        <div>
          <label class="block text-purple-600 text-sm font-medium mb-2">Requirements</label>
          <textarea
            v-model="requirements"
            placeholder="Describe personnel requirements"
            rows="4"
            class="w-full px-3 py-2 border border-gray-200 rounded-md text-gray-700 focus:outline-none focus:border-purple-500"
          ></textarea>
        </div>
        <div>
          <label class="block text-purple-600 text-sm font-medium mb-2">Qualifications</label>
          <textarea
            v-model="qualifications"
            placeholder="List required qualifications"
            rows="4"
            class="w-full px-3 py-2 border border-gray-200 rounded-md text-gray-700 focus:outline-none focus:border-purple-500"
          ></textarea>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue';
import { UsersIcon } from '@heroicons/vue/24/outline';
import type { PersonnelRequirement } from '../types/types';

const props = defineProps<{
  modelValue: PersonnelRequirement
}>();

const emit = defineEmits<{
  (e: 'update:modelValue', value: PersonnelRequirement): void
}>();

const requirements = ref(props.modelValue.requirements);
const qualifications = ref(props.modelValue.qualifications);

watch([requirements, qualifications], () => {
  emit('update:modelValue', {
    requirements: requirements.value,
    qualifications: qualifications.value
  });
}, { deep: true });
</script>
  
  