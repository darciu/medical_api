from src.entities.medicaldata import MedicalData
import math

md = MedicalData.load_csv_files()


def test_dummy():
    assert 1==1


def test_medical_data_existence():
    assert len(md.df) != 0
    assert len(md.bnf_code_vmp_nm) != 0
    assert md.bnf_code_vmp_nm.get('0107010Z0BCAAAE') == 'Generic Anusol cream'


def test_avg_gross_cost():
    assert md.avg_gross_cost(2) > 0
    assert math.isnan(md.avg_gross_cost(10))

def test_avg_total_items():
    assert md.avg_total_items(2) > 0
    assert math.isnan(md.avg_total_items(10))

def test_nunique_bnf_codes():
    assert md.nunique_bnf_codes(1) > 0
    assert md.nunique_bnf_codes(10) == 0

def test_get_product_description():
    assert md.get_product_description('23354103785') == 'Colostomy bags'
