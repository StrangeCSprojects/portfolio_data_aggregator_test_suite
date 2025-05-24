# mock_api.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/portfolio')
def get_portfolio():
    return jsonify({
        "id": "portfolio_001",
        "name": "Retirement Fund",
        "owner": "user_123",
        "total_value": 1250000.00,
        "positions": ["pos_001", "pos_002"]
    })

if __name__ == '__main__':
    app.run(debug=True)
