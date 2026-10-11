# Imagen base oficial de Python (versión ligera)
FROM python:3.11-slim

# Evita que Python escriba archivos .pyc y permita logs en tiempo real
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos primero el requirements para aprovechar el cache de Docker
COPY requirements.txt .

# Instalamos las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto del proyecto
COPY . .

# Exponemos el puerto 5000 (el que usa Flask por defecto)
EXPOSE 5000

# Comando para ejecutar la app
CMD ["python", "app.py"]