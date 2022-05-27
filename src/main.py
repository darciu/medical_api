from os import environ

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routers.v1 import endpoints
from entities.medicaldata import MedicalData
import logging


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(endpoints.router, prefix='/v1')

@app.on_event("startup")
def startup():
    
    app.state.medical_data = MedicalData.load_csv_files()

    #  set environment variables for local purposes
    if environ.get('SNOWFLAKE_USER') is None:
        from config import SNOWFLAKE_USER
        environ["SNOWFLAKE_USER"] = SNOWFLAKE_USER
        
    if environ.get('SNOWFLAKE_PASS') is None:
        from config import SNOWFLAKE_PASS
        environ["SNOWFLAKE_PASS"] = SNOWFLAKE_PASS

    if environ.get('SNOWFLAKE_ACCOUNT') is None:
        from config import SNOWFLAKE_ACCOUNT
        environ["SNOWFLAKE_ACCOUNT"] = SNOWFLAKE_ACCOUNT

    