from fastapi import APIRouter, Request


router = APIRouter()




@router.get("/get_avg_gross_cost")
def get_avg_gross_cots(request: Request, month: int):
    medical_data = request.app.state.medical_data
    return medical_data.avg_gross_cost(month)

@router.get("/get_avg_total_items")
def get_avg_total_items():
    pass

@router.get("/get_nunique_bnf_codes")
def get_nunique_bnf_codes():
    pass

@router.get("/get_product_description")
def get_product_description():
    pass