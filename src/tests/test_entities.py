"""Tests"""
from os import environ

from src.entities.medicaldata import MedicalData
from src.entities.snowflakedata import SnowflakeDataConnector

if environ.get('SNOWFLAKE_USER') is not None:
    SNOWFLAKE_USER=environ.get('SNOWFLAKE_USER')
else:
    from config import SNOWFLAKE_USER

if environ.get('SNOWFLAKE_PASS') is not None:
    SNOWFLAKE_PASS=environ.get('SNOWFLAKE_PASS')
else:
    from config import SNOWFLAKE_PASS

if environ.get('SNOWFLAKE_ACCOUNT') is not None:
    SNOWFLAKE_ACCOUNT=environ.get('SNOWFLAKE_ACCOUNT')
else:
    from config import SNOWFLAKE_ACCOUNT


md = MedicalData.load_csv_files()
sf_conn = SnowflakeDataConnector(SNOWFLAKE_USER,SNOWFLAKE_PASS,SNOWFLAKE_ACCOUNT)

def test_dummy():
    assert 1==1

def test_medical_data_existence():
    assert len(md.df) != 0
    assert len(md.bnf_code_vmp_nm) != 0
    assert md.bnf_code_vmp_nm.get('0107010Z0BCAAAE') == 'Generic Anusol cream'

def test_avg_gross_cost():
    assert md.avg_gross_cost(2) > 0
    assert md.avg_gross_cost(10) == 0

def test_avg_total_items():
    assert md.avg_total_items(2) > 0
    assert md.avg_total_items(10) == 0

def test_nunique_bnf_codes():
    assert md.nunique_bnf_codes(1) > 0
    assert md.nunique_bnf_codes(10) == 0

def test_get_product_description():
    assert md.product_description('23354103785') == 'Colostomy bags'



def test_snowflake_connection():
    assert sf_conn.get_data_one_result("select 0") == 0

def test_snowflake_query():
    assert sf_conn.get_data_one_result("select avg(gross_cost) as avg_cost from kinesso_task.public.csv") > 0

def test_wrong_query():
    assert sf_conn.get_data_one_result("wrong query") == "Connector could not retrieve any data. Chceck your query"



