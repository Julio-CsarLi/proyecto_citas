# agenda_service/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests  # Librería para hacer peticiones HTTP a otros servicios

app = FastAPI(title="API de Agenda")

# La dirección donde vive nuestro otro microservicio
PACIENTES_SERVICE_URL = "http://pacientes-service:8001/pacientes"

# Modelo de datos que esperamos recibir del usuario
class Cita(BaseModel):
    paciente_id: int
    medico_id: int
    fecha: str

# Simulamos la base de datos de citas
CITAS_DB = []

@app.post("/citas")
def crear_cita(cita: Cita):
    # --- COMUNICACIÓN SÍNCRONA ENTRE MICROSERVICIOS ---
    try:
        # 1. Le preguntamos al Servicio de Pacientes si el ID es válido
        respuesta = requests.get(f"{PACIENTES_SERVICE_URL}/{cita.paciente_id}")
        
        # 2. Si el servicio de pacientes dice que no existe (404), rechazamos la cita
        if respuesta.status_code == 404:
            raise HTTPException(status_code=404, detail="No se puede agendar: El paciente no existe.")
            
    except requests.exceptions.ConnectionError:
        raise HTTPException(status_code=500, detail="El Servicio de Pacientes está caído.")

    # 3. Si todo salió bien, guardamos la cita
    nueva_cita = cita.dict()
    nueva_cita["id_cita"] = len(CITAS_DB) + 1
    nueva_cita["estado"] = "CONFIRMADA"
    
    CITAS_DB.append(nueva_cita)
    return {"mensaje": "Cita agendada exitosamente", "cita": nueva_cita}