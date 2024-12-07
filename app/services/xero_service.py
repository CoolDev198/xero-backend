
import httpx

BASE_URL = "http://localhost:3001/api.xro/2.0/Reports/BalanceSheet"

async def fetch_balance_sheet():
    """
    Fetches the Balance Sheet Report from the Xero API.
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(BASE_URL)
        response.raise_for_status()
        return response.json()
