# Frontend
FROM node:16 as frontend-builder
WORKDIR /app/frontend
COPY frontend/package*.json ./
RUN npm install
COPY frontend .
RUN npm run build

# Backend
FROM python:3.8-slim
WORKDIR /app
COPY backend/requirements.txt .
RUN pip install -r requirements.txt
COPY backend .
COPY --from=frontend-builder /app/frontend/dist ./static

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"] 