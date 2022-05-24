"""Application routing"""

from fastapi import APIRouter, Request
from typing import Optional


router = APIRouter()


@router.get("/get_avg_gross_cost")
def get_avg_gross_cots(request: Request, month: int) -> Optional[float]:
    medical_data = request.app.state.medical_data
    return medical_data.avg_gross_cost(month)


@router.get("/get_avg_total_items")
def get_avg_total_items(request: Request, month: int) -> Optional[float]:
    medical_data = request.app.state.medical_data
    return medical_data.avg_total_items(month)


@router.get("/get_nunique_bnf_codes")
def get_nunique_bnf_codes(request: Request, month: int) -> Optional[int]:
    medical_data = request.app.state.medical_data
    return medical_data.nunique_bnf_codes(month)


@router.get("/get_product_description")
def get_product_description(request: Request, bnf_code: str) -> str:
    medical_data = request.app.state.medical_data
    return medical_data.product_description(bnf_code)
