import responses
import requests
from tests.schemas.portfolio_schema import Portfolio

@responses.activate
def test_get_portfolio_schema():
    mock_data = {
        "id": "portfolio_001",
        "name": "Retirement Fund",
        "owner": "user_123",
        "total_value": 1250000.00,
        "positions": ["pos_001", "pos_002"]
    }

    responses.add(
        responses.GET,
        "https://api.example.com/api/portfolio",
        json=mock_data,
        status=200
    )

    response = requests.get("https://api.example.com/api/portfolio")
    assert response.status_code == 200

    # Validate schema
    validated = Portfolio(**response.json())
    assert validated.owner == "user_123"
    assert isinstance(validated.total_value, float)
    assert all(isinstance(pos, str) for pos in validated.positions)
