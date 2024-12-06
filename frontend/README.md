# Vue 3 + Vite

This template should help get you started developing with Vue 3 in Vite. The template uses Vue 3 `<script setup>` SFCs, check out the [script setup docs](https://v3.vuejs.org/api/sfc-script-setup.html#sfc-script-setup) to learn more.

Learn more about IDE Support for Vue in the [Vue Docs Scaling up Guide](https://vuejs.org/guide/scaling-up/tooling.html#ide-support).

frontend/
├── src/
│   ├── components/
│   │   ├── LaboratoryInformation.vue     # 实验室基本信息组件
│   │   ├── LaboratoryOptimizationForm.vue # 主表单组件
│   │   ├── OptimizationObjectives.vue    # 优化目标组件
│   │   └── PersonnelRequirements.vue     # 人员需求组件
│   ├── types/
│   │   └── types.ts                      # TypeScript 类型定义
│   ├── App.vue                           # 根组件
│   ├── main.js                           # 入口文件
│   ├── index.css                         # Tailwind CSS 导入
│   └── style.css                         # 全局样式
├── tailwind.config.js                    # Tailwind 配置
├── postcss.config.js                     # PostCSS 配置
├── package.json                          # 项目依赖
└── vite.config.js                        # Vite 配置