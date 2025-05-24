# Portfolio Data Aggregator Test Suite

This project simulates a backend test suite for validating portfolio and asset data APIs. 
It demonstrates real-world quality assurance practices using Pytest, schema validation with Pydantic,
mocking with `responses`, and performance testing with Locust.

---

## 📌 Features

- ✅ Automated testing of `/api/portfolio` and `/api/assets` endpoints
- ✅ Schema validation using Pydantic models
- ✅ Edge case testing (missing fields, invalid types, empty portfolios)
- ✅ CI integration with GitHub Actions
- ✅ Test coverage reporting with `pytest-cov`
- ✅ Reusable fixtures and structured test suite
- ✅ Performance testing using Locust

---

## 🧪 How to Run Tests

```bash
# Activate your virtual environment
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Run tests with coverage report
pytest --cov=tests --cov-report=html
```

Open the report at `htmlcov/index.html`

---

## ⚙️ Run Performance Test (Locust)

Start a mock API:
```bash
python mock_api.py
```

Run Locust:
```bash
locust -f locustfile.py
```

Visit: [http://localhost:8089](http://localhost:8089)

---

## 🚀 GitHub Actions CI

A GitHub Actions workflow (`.github/workflows/python-ci.yml`) automatically installs dependencies, runs tests, and uploads coverage reports on every push or PR.

---

## 📁 Project Structure

```
tests/
├── api/                 # Endpoint test files
├── fixtures/            # Mock data fixtures
├── schemas/             # Pydantic schemas
├── conftest.py          # (Reserved for shared fixtures)
.github/
└── workflows/
    └── python-ci.yml    # CI pipeline

mock_api.py              # Local Flask mock server
locustfile.py            # Load testing config
requirements.txt         # Dependencies
TEST_STRATEGY.md         # Testing approach
```

---

## 📊 Test Coverage & Performance

- Run `pytest --cov` to get code coverage
- Run Locust headless with `--csv=reports/perf_test` to generate `.csv` reports
- Write summary in `reports/perf_summary.md`

---

## 🧠 Author Notes

This test suite was built to simulate the kind of backend quality assurance infrastructure used by companies. It's structured, test-driven, and performance-aware.