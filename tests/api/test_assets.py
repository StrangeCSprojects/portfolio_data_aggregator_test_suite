import responses
import requests
from tests.schemas.asset_schema import Asset

@responses.activate
def test_get_assets():
    responses.add(
        responses.GET,
        "https://api.example.com/api/assets",
        json=[
                {
                    "symbol": "AAPL",
                    "last_price": 175.32,
                    "date": "2024-05-01",
                    "exchange": "NASDAQ"
                },
                {
                    "symbol": "GOOG",
                    "last_price": 2900.12,
                    "date": "2024-05-01",
                    "exchange": "NASDAQ"
                }
                ],
        status=200
    )
    
    response = requests.get("https://api.example.com/api/assets")

    assert response.status_code == 200
    data = response.json()

    assert isinstance(data, list)
    assert data[0]["symbol"] == "AAPL"
    assert data[1]["symbol"] == "GOOG"
    assert all("last_price" in asset for asset in data)


@responses.activate
def test_invalid_asset():
    responses.add(
        responses.GET,
        "https://api.example.com/api/assets?symbol=XYZ",
        json={"error": "Asset not found"},
        status=404
    )

    response = requests.get("https://api.example.com/api/assets?symbol=XYZ")
    
    assert response.status_code == 404
    assert response.json()["error"] == "Asset not found"


@responses.activate
def test_get_assets_schema():
    mock_data = [
        {
            "symbol": "AAPL",
            "last_price": 175.32,
            "date": "2024-05-01",
            "exchange": "NASDAQ"
        }
    ]

    responses.add(
        responses.GET,
        "https://api.example.com/api/assets",
        json=mock_data,
        status=200
    )

    response = requests.get("https://api.example.com/api/assets")
    assert response.status_code == 200

    # Validate schema
    for item in response.json():
        validated = Asset(**item)
        assert validated.symbol.isupper()


