
from fastapi import APIRouter, HTTPException
from app.services.xero_service import fetch_balance_sheet

router = APIRouter()

@router.get("/balance-sheet", summary="Fetch Balance Sheet Report")
async def get_balance_sheet():
    """
    Fetches the Balance Sheet Report from Xero API.
    """
    try:
        balance_sheet = await fetch_balance_sheet()
        return balance_sheet
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
