<template>
  <div class="json-editor-container">
    <MonacoEditor
      v-model:value="internalValue"
      :options="options"
      theme="vs-light"
      language="json"
      @change="handleChange"
      height="300"
    />
    <div v-if="error" class="error-message">
      {{ error }}
    </div>
  </div>
</template>

<script>
import MonacoEditor from 'monaco-editor-vue3'

export default {
  name: 'JsonEditor',
  components: {
    MonacoEditor
  },
  props: {
    modelValue: {
      type: [Object, String],
      default: () => ({})
    },
    example: {
      type: Object,
      default: () => ({})
    }
  },
  data() {
    return {
      internalValue: '',
      error: null,
      options: {
        minimap: { enabled: false },
        lineNumbers: 'on',
        scrollBeyondLastLine: false,
        automaticLayout: true,
        fontSize: 14
      }
    }
  },
  watch: {
    modelValue: {
      immediate: true,
      handler(newVal) {
        if (typeof newVal === 'object') {
          this.internalValue = JSON.stringify(newVal, null, 2)
        } else {
          this.internalValue = newVal || JSON.stringify(this.example, null, 2)
        }
      }
    }
  },
  methods: {
    handleChange(value) {
      try {
        const parsed = JSON.parse(value)
        this.error = null
        this.$emit('update:modelValue', parsed)
      } catch (e) {
        this.error = 'Invalid JSON format'
      }
    }
  }
}
</script>

<style scoped>
.json-editor-container {
  height: 300px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.error-message {
  color: red;
  margin-top: 4px;
  font-size: 12px;
}
</style> 