FROM python:3.11-slim

# Evita archivos .pyc y logs con buffer
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Dependencias primero (aprovecha cache de capas)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del proyecto
COPY . .

# Crea un usuario no-root y dale ownership de /app
RUN useradd -r -u 1001 appuser && chown -R appuser:appuser /app
USER appuser

EXPOSE 8000

# Arranca con Gunicorn usando el archivo de config
CMD ["gunicorn", "-c", "gunicorn.conf.py", "app:app"]
CMD ["python", "app.py"]