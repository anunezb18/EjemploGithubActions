# Imagen base
FROM python:3.11-slim

# Evita archivos .pyc y forzar salida sin buffer
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Directorio de trabajo
WORKDIR /app

# Copia todo el proyecto
COPY . .

# Actualiza pip e instala dependencias si existe requirements.txt
RUN python -m pip install --upgrade pip && \
    if [ -f requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi

# Puerto expuesto (opcional)
# EXPOSE 8000

# Comando por defecto: ejecuta el script principal
CMD ["python", "-