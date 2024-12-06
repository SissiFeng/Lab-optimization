<template>
  <div class="form-container">
    <h2>Laboratory Optimization Configuration</h2>
    <form @submit.prevent="submitForm" class="survey-form">
      <!-- Basic Information -->
      <div class="form-field">
        <label for="lab_name">Laboratory Name</label>
        <input
          type="text"
          id="lab_name"
          v-model="formData.lab_name"
          required
          class="form-input"
        />
      </div>

      <div class="form-field">
        <label for="optimization_type">Optimization Type</label>
        <input
          type="text"
          id="optimization_type"
          v-model="formData.optimization_type"
          required
          class="form-input"
        />
      </div>

      <div class="form-field">
        <label for="description">Description</label>
        <textarea
          id="description"
          v-model="formData.description"
          required
          class="form-textarea"
        ></textarea>
      </div>

      <div class="form-field">
        <label for="improvement">Expected Improvement (%)</label>
        <input
          type="number"
          id="improvement"
          v-model.number="formData.improvement"
          required
          class="form-input"
        />
      </div>

      <!-- Objective Configuration -->
      <div class="form-field">
        <label for="objective_type">Objective Type</label>
        <select
          id="objective_type"
          v-model="formData.objective_type"
          required
          class="form-select"
        >
          <option value="maximize">Maximize</option>
          <option value="minimize">Minimize</option>
        </select>
      </div>

      <div class="form-field">
        <label for="objective_target">Optimization Target</label>
        <input
          type="text"
          id="objective_target"
          v-model="formData.objective_target"
          required
          class="form-input"
        />
      </div>

      <!-- Parameters JSON Editor -->
      <div class="form-field">
        <label>Parameters Configuration</label>
        <JsonEditor
          v-model="formData.parameters"
          :example="parametersExample"
        />
      </div>

      <!-- Constraints JSON Editor -->
      <div class="form-field">
        <label>Constraints</label>
        <JsonEditor
          v-model="formData.constraints"
          :example="constraintsExample"
        />
      </div>

      <button type="submit" class="submit-button">Submit</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
import JsonEditor from './JsonEditor.vue'

export default {
  name: 'DynamicForm',
  components: {
    JsonEditor
  },
  data() {
    return {
      formData: {
        lab_name: '',
        optimization_type: '',
        description: '',
        improvement: 0,
        objective_type: 'maximize',
        objective_target: '',
        parameters: {},
        constraints: {}
      },
      parametersExample: {
        "Ni": { "min": 0, "max": 1, "step": 0.1 },
        "Fe": { "min": 0, "max": 1, "step": 0.1 }
      },
      constraintsExample: {
        "total_fraction": { "type": "equality", "value": "sum([Ni,Fe]) == 1" },
        "temperature": { "type": "inequality", "value": "T <= 60" }
      }
    }
  },
  methods: {
    async submitForm() {
      try {
        const formDataToSubmit = {
          lab_name: this.formData.lab_name,
          optimization_type: this.formData.optimization_type,
          description: this.formData.description,
          improvement: this.formData.improvement,
          objective: {
            type: this.formData.objective_type,
            target: this.formData.objective_target
          },
          parameters: this.formData.parameters,
          constraints: this.formData.constraints
        }

        const response = await axios.post('http://localhost:8000/api/submit-form', formDataToSubmit)
        alert('Submission successful!')
        console.log('Response:', response.data)
      } catch (error) {
        console.error('Submission failed:', error)
        alert('Submission failed. Please check console for details.')
      }
    }
  }
}
</script>

<style scoped>
.form-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

.form-field {
  margin-bottom: 20px;
}

label {
  display: block;
  margin-bottom: 8px;
  font-weight: bold;
}

.form-input,
.form-select,
.form-textarea {
  width: 100%;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 14px;
}

.form-textarea {
  min-height: 100px;
  resize: vertical;
}

.submit-button {
  background-color: #1976d2;
  color: white;
  padding: 12px 24px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
  margin-top: 20px;
}

.submit-button:hover {
  background-color: #1565c0;
}
</style> 