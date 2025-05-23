# tests/fixtures/mock_data.py

portfolio_valid = {
    "id": "portfolio_001",
    "name": "Retirement Fund",
    "owner": "user_123",
    "total_value": 1250000.00,
    "positions": ["pos_001", "pos_002"]
}

portfolio_empty = {
    "id": "portfolio_002",
    "name": "Empty Portfolio",
    "owner": "user_124",
    "total_value": 0.0,
    "positions": []
}

portfolio_missing_owner = {
    "id": "portfolio_003",
    "name": "Broken Portfolio",
    "total_value": 1000.0,
    "positions": ["pos_003"]
}

portfolio_invalid_value = {
    "id": "portfolio_004",
    "name": "Corrupted Portfolio",
    "owner": "user_125",
    "total_value": "not_a_number",
    "positions": ["pos_004"]
}
