from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routers.v1 import endpoints
from entities.medicaldata import MedicalData


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(endpoints.router, prefix='/v1')

@app.on_event("startup")
def startup():
    
    app.state.medical_data = MedicalData.load_csv_files()
