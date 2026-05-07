# Usa una versión ligera de Python oficial
FROM python:3.9-slim

# Crea una carpeta dentro del contenedor llamada /app
WORKDIR /app

# Copia tu archivo de dependencias al contenedor
COPY requirements.txt .

# Instala las librerías (FastAPI, uvicorn, requests)
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el código de tu carpeta al contenedor
COPY . .

# Comando para encender el servidor (nota que agregamos --host 0.0.0.0)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]