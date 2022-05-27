"""Application routing"""
from os import environ

from fastapi import APIRouter, Request, Query
from typing import Optional


from entities.snowflakedata import SnowflakeDataConnector


router = APIRouter()


@router.get("/get_avg_gross_cost", tags=["get_avg_gross_cost"])
def get_avg_gross_cots(
    request: Request,
    month: int,
    data_source: str = Query("local", enum=["local", "remote"]),
) -> Optional[float]:
    if data_source == "local":
        medical_data = request.app.state.medical_data
        return medical_data.avg_gross_cost(month)
    elif data_source == "remote":
        sf_conn = SnowflakeDataConnector(
            environ.get("SNOWFLAKE_USER"),
            environ.get("SNOWFLAKE_PASS"),
            environ.get("SNOWFLAKE_ACCOUNT"),
        )
        query = f"select avg(gross_cost) as avg_cost from kinesso_task.public.csv where month = {month}"
        return sf_conn.get_data_one_result(query)


@router.get("/get_avg_total_items", tags=["get_avg_total_items"])
def get_avg_total_items(
    request: Request,
    month: int,
    data_source: str = Query("local", enum=["local", "remote"]),
) -> Optional[float]:
    if data_source == "local":
        medical_data = request.app.state.medical_data
        return medical_data.avg_total_items(month)
    elif data_source == "remote":
        sf_conn = SnowflakeDataConnector(
            environ.get("SNOWFLAKE_USER"),
            environ.get("SNOWFLAKE_PASS"),
            environ.get("SNOWFLAKE_ACCOUNT"),
        )
        query = f"select avg(total_items) as avg_total_items from kinesso_task.public.csv where month = {month}"
        return sf_conn.get_data_one_result(query)


@router.get("/get_nunique_bnf_codes", tags=["get_nunique_bnf_codes"])
def get_nunique_bnf_codes(
    request: Request,
    month: int,
    data_source: str = Query("local", enum=["local", "remote"]),
) -> Optional[int]:
    if data_source == "local":
        medical_data = request.app.state.medical_data
        return medical_data.nunique_bnf_codes(month)
    elif data_source == "remote":
        sf_conn = SnowflakeDataConnector(
            environ.get("SNOWFLAKE_USER"),
            environ.get("SNOWFLAKE_PASS"),
            environ.get("SNOWFLAKE_ACCOUNT"),
        )
        query = f"select count(distinct bnf_code) from kinesso_task.public.csv where month = {month}"
        return sf_conn.get_data_one_result(query)


@router.get("/get_product_description", tags=["get_product_description"])
def get_product_description(
    request: Request,
    bnf_code: str,
    data_source: str = Query("local", enum=["local", "remote"]),
) -> str:
    if data_source == "local":
        medical_data = request.app.state.medical_data
        return medical_data.product_description(bnf_code)
    elif data_source == "remote":
        sf_conn = SnowflakeDataConnector(
            environ.get("SNOWFLAKE_USER"),
            environ.get("SNOWFLAKE_PASS"),
            environ.get("SNOWFLAKE_ACCOUNT"),
        )
        query = f"select distinct(vmp_nm) from kinesso_task.public.csv where bnf_code = '{bnf_code}'"
        return sf_conn.get_data_one_result(query)
