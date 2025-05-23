import responses
import requests
import pytest
from pydantic import ValidationError
from tests.schemas.portfolio_schema import Portfolio
from tests.fixtures.mock_data import portfolio_valid, portfolio_empty, portfolio_missing_owner, portfolio_invalid_value

@responses.activate
def test_get_portfolio_schema():
    mock_data = portfolio_valid

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
    assert isinstance(validated.total_value, int)
    assert all(isinstance(pos, str) for pos in validated.positions)

@responses.activate
def test_empty_portfolio():
    mock_data = portfolio_empty

    responses.add(
        responses.GET,
        "https://api.example.com/api/portfolio",
        json=mock_data,
        status=200
    )

    response = requests.get("https://api.example.com/api/portfolio")
    assert response.status_code == 200

    validated = Portfolio(**response.json())
    assert validated.positions == []


def test_portfolio_missing_owner():
    broken_data = portfolio_missing_owner
    with pytest.raises(ValidationError):
        Portfolio(**broken_data)


def test_portfolio_total_value_invalid_type():
    broken_data = portfolio_invalid_value

    with pytest.raises(ValidationError):
        Portfolio(**broken_data)