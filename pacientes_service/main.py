# pacientes_service/main.py
from fastapi import FastAPI, HTTPException

app = FastAPI(title="API de Pacientes")

# Simulamos la base de datos de pacientes
PACIENTES_DB = {
    1: {"nombre": "Juan Perez", "email": "juan@gmail.com"},
    2: {"nombre": "Ana Gomez", "email": "ana@hotmail.com"}
}

@app.get("/pacientes/{paciente_id}")
def obtener_paciente(paciente_id: int):
    # Si el paciente existe, devuelve sus datos
    if paciente_id in PACIENTES_DB:
        return PACIENTES_DB[paciente_id]
    
    # Si no existe, devuelve un error 404
    raise HTTPException(status_code=404, detail="Paciente no encontrado")