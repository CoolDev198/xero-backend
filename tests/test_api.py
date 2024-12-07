
import pytest

def test_api_endpoint():
    assert True  # Replace with actual test logic for API endpoints

from unittest.mock import patch
from fastapi.testclient import TestClient
from app.main import app  # Import your FastAPI app instance

client = TestClient(app)

@patch("app.services.xero_service.fetch_balance_sheet")
def test_get_balance_sheet(mock_fetch):
    # Mock Xero response
    mock_fetch.return_value = {
        "Status": "OK",
        "Reports": [
            {
                "ReportID": "BalanceSheet",
                "ReportName": "Balance Sheet",
                "ReportType": "BalanceSheet",
                "ReportTitles": [
                    "Balance Sheet",
                    "Demo Org",
                    "As at 06 December 2024"
                ],
                "ReportDate": "06 December 2024",
                "UpdatedDateUTC": "/Date(1733501920519)/",
                "Fields": [],
                "Rows": [
                    {
                        "RowType": "Header",
                        "Cells": [
                            {"Value": ""},
                            {"Value": "06 December 2024"},
                            {"Value": "07 December 2023"}
                        ]
                    },
                    {
                        "RowType": "Section",
                        "Title": "Assets",
                        "Rows": []
                    }
                ]
            }
        ]
    }

    # Call the endpoint
    response = client.get("/balance-sheet")

    # Assertions
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    assert "Reports" in response.json(), "Response is missing 'Reports' key"
    assert response.json()["Reports"][0]["ReportID"] == "BalanceSheet", "ReportID mismatch"
    assert response.json()["Reports"][0]["Rows"][1]["Title"] == "Assets", "Row title mismatch"
