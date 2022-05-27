from os import environ

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routers.v1 import endpoints
from entities.medicaldata import MedicalData

tags_metadata = [
    {
        "name": "get_avg_gross_cost",
        "description": "Average cost of prescriptions (Gross Cost) in the selected period (month resolution)",
    },
    {
        "name": "get_avg_total_items",
        "description": "Average number of products (Total Items) in the selected period (month resolution)",
    },
    {
        "name": "get_nunique_bnf_codes",
        "description": "Number of prescriptions in the selected period (month resolution) according to the code (BNF Code)",
    },
    {
        "name": "get_product_description",
        "description": "Product description (VMP_NM) based on the code (BNF Code)",
    },
]

app = FastAPI(openapi_tags=tags_metadata)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(endpoints.router, prefix="/v1")


@app.on_event("startup")
def startup():

    app.state.medical_data = MedicalData.load_csv_files()

    #  set environment variables for local purposes
    if environ.get("SNOWFLAKE_USER") is None:
        from config import SNOWFLAKE_USER

        environ["SNOWFLAKE_USER"] = SNOWFLAKE_USER

    if environ.get("SNOWFLAKE_PASS") is None:
        from config import SNOWFLAKE_PASS

        environ["SNOWFLAKE_PASS"] = SNOWFLAKE_PASS

    if environ.get("SNOWFLAKE_ACCOUNT") is None:
        from config import SNOWFLAKE_ACCOUNT

        environ["SNOWFLAKE_ACCOUNT"] = SNOWFLAKE_ACCOUNT
