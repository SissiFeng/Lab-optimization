# Vue 3 + Vite

This template should help get you started developing with Vue 3 in Vite. The template uses Vue 3 `<script setup>` SFCs, check out the [script setup docs](https://v3.vuejs.org/api/sfc-script-setup.html#sfc-script-setup) to learn more.

Learn more about IDE Support for Vue in the [Vue Docs Scaling up Guide](https://vuejs.org/guide/scaling-up/tooling.html#ide-support).

frontend/
├── src/
│   ├── components/
│   │   ├── LaboratoryInformation.vue     # Laboratory Information Component
│   │   ├── LaboratoryOptimizationForm.vue # Main Form Component
│   │   ├── OptimizationObjectives.vue    # Optimization Objectives Component
│   │   └── PersonnelRequirements.vue     # Personnel Requirements Component
│   ├── types/
│   │   └── types.ts                      # TypeScript Type Definitions
│   ├── App.vue                           # Root Component
│   ├── main.js                           # Entry File
│   ├── index.css                         # Tailwind CSS Import
│   └── style.css                         # Global Styles
├── tailwind.config.js                    # Tailwind Configuration
├── postcss.config.js                     # PostCSS Configuration
├── package.json                          # Project Dependencies
└── vite.config.js                        # Vite Configuration