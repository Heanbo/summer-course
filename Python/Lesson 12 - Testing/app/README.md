# Library Management System - Testing Exercise

A simple library management system built to practice unit and integration testing with Python's pytest framework.

## System Overview

This application consists of three main components:

1. **Book Module** (`book.py`) - Manages individual book data and validation
2. **Library Module** (`library.py`) - Handles collection management and operations
3. **Analytics Module** (`analytics.py`) - Provides statistics and reporting

## Setup

1. Navigate to the app directory:
```bash
cd app
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

Run the demo to see the system in action:
```bash
python demo.py
```

## Running Tests

Run all tests with coverage:
```bash
# On Windows PowerShell:
$env:PYTHONPATH="." ; pytest

# On Linux/Mac:
PYTHONPATH=. pytest
```

View the HTML coverage report:
```bash
# Report is generated in htmlcov/ directory
# Open htmlcov/index.html in a browser
```

## Project Structure

```
app/
├── book.py                 # Book class and utility functions
├── library.py              # Library management class
├── analytics.py            # Analytics and reporting class
├── demo.py                 # Demo script
├── requirements.txt        # Python dependencies
├── pytest.ini             # Pytest configuration
└── tests/
    ├── __init__.py
    ├── conftest.py         # Pytest fixtures
    ├── test_book.py        # Book unit tests
    ├── test_library.py     # Library unit tests
    ├── test_analytics.py   # Analytics tests
    └── test_integration.py # Integration tests
```

## Testing Goals

### Hands-On #1: Unit Testing
1. Check initial code coverage
2. Add unit tests to functions with 0% coverage
3. Bring total coverage to 80%+

### Hands-On #2: Integration Testing
1. Write tests that verify multiple components working together
2. Use fixtures to create test data
3. Test realistic workflows (add books → check them out → generate analytics)
