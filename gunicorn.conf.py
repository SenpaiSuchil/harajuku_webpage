# gunicorn.conf.py
import multiprocessing

# Dirección donde escucha Gunicorn (dentro del contenedor)
bind = "0.0.0.0:8000"

# Número de workers. La fórmula clásica es (2 * CPUs) + 1
workers = (multiprocessing.cpu_count() * 2) + 1

# Threads por worker (útil si tu app es I/O intensiva)
threads = workers

# Reinicia workers cada N requests para evitar fugas de memoria
max_requests = 1000
max_requests_jitter = 50

# Timeout de un worker (segundos)
timeout = 120

# Logs a stdout/stderr para que Docker los capture
log_file = "-"
accesslog = "-"
errorlog = "-"

# Loglevel
loglevel = "info"