# Sample API Project

An educational Python REST API project demonstrating key API design concepts for junior engineers.

## 🎯 Learning Objectives

This project demonstrates several important software engineering concepts:

1. **Separation of Concerns**: Business logic is completely separated from API implementation
2. **Multiple Interfaces**: Same business logic accessible via REST API and CLI
3. **Comprehensive Testing**: 88 tests across unit, API integration, and CLI integration layers
4. **Testing Framework**: Uses Python's built-in unittest framework (no external dependencies)
5. **API Design**: RESTful endpoints with proper HTTP methods and status codes
6. **Modern API Framework**: FastAPI provides automatic documentation, data validation, and type safety

## 📁 Project Structure

```
sample-api/
├── src/
│   └── math_operations.py           # 🧠 Business Logic (Pure Functions)
├── tests/
│   ├── unit/
│   │   └── test_math_operations.py  # ✅ Unit Tests (30 tests)
│   └── integration/
│       ├── test_api_integration.py  # 🔗 API Integration Tests (31 tests)
│       └── test_cli_integration.py  # 💻 CLI Integration Tests (27 tests)
├── app.py                           # 🚀 FastAPI REST API
├── cli.py                           # 💻 Command Line Interface
├── pyproject.toml                   # 📦 Dependencies & Configuration
└── README.md                        # 📖 Documentation
```

## 🚀 Quick Start

### Prerequisites
- Python 3.11+ 
- [uv](https://docs.astral.sh/uv/) package manager

### Installation

```bash
# Clone or download the project
cd sample-api

# Install dependencies with uv
uv add fastapi uvicorn requests
uv add --dev httpx  # For FastAPI TestClient

# Or install from pyproject.toml
uv sync --dev
```

### Running the API

```bash
# Start the FastAPI development server
uv run python app.py

# Alternative: Use uvicorn directly
uv run uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at:
- **API endpoints**: `http://localhost:8000`
- **Interactive docs (Swagger UI)**: `http://localhost:8000/docs`
- **Alternative docs (ReDoc)**: `http://localhost:8000/redoc`

### Running Tests

```bash
# Run all tests (unit + integration)
uv run python -m unittest discover -s tests -p "test_*.py" -v

# Run specific test modules
uv run python -m unittest tests.unit.test_math_operations -v
uv run python -m unittest tests.integration.test_api_integration -v
uv run python -m unittest tests.integration.test_cli_integration -v

# Run tests without verbose output
uv run python -m unittest discover -s tests -p "test_*.py"
```

### Using the CLI

```bash
# Test business logic directly via command line
uv run python cli.py square 5
uv run python cli.py power 2 8
uv run python cli.py factorial 5
uv run python cli.py fibonacci 10
uv run python cli.py prime 17
uv run python cli.py stats 1 2 3 4 5
```

## 🌐 API Endpoints

### GET Endpoints

#### Root Information
```bash
curl http://localhost:8000/
# Response: API info with available endpoints and documentation links
```

#### Health Check
```bash
curl http://localhost:8000/health
# Response: {"status": "healthy", "service": "math-operations-api"}
```

#### Interactive Documentation
```bash
# Open in browser for interactive API testing
open http://localhost:8000/docs
```

#### Calculate Square
```bash
curl http://localhost:8000/square/5
# Response: {"operation": "square", "input": 5, "result": 25, "success": true}

curl http://localhost:8000/square/2.5
# Response: {"operation": "square", "input": 2.5, "result": 6.25, "success": true}
```

#### Calculate Factorial
```bash
curl http://localhost:8000/factorial/5
# Response: {"operation": "factorial", "input": 5, "result": 120, "success": true}
```

#### Generate Fibonacci Sequence
```bash
curl http://localhost:8000/fibonacci/8
# Response: {"operation": "fibonacci", "count": 8, "sequence": [0, 1, 1, 2, 3, 5, 8, 13], "success": true}
```

#### Check Prime Number
```bash
curl http://localhost:8000/prime/17
# Response: {"operation": "is_prime", "input": 17, "is_prime": true, "success": true}

curl http://localhost:8000/prime/15
# Response: {"operation": "is_prime", "input": 15, "is_prime": false, "success": true}
```

### POST Endpoints

#### Calculate Power
```bash
curl -X POST http://localhost:8000/power \
  -H "Content-Type: application/json" \
  -d '{"base": 2, "exponent": 8}'
# Response: {"operation": "power", "base": 2, "exponent": 8, "result": 256, "success": true}
```

#### Calculate Statistics
```bash
curl -X POST http://localhost:8000/stats \
  -H "Content-Type: application/json" \
  -d '{"numbers": [1, 2, 3, 4, 5]}'
# Response: {
#   "operation": "calculate_stats",
#   "input_numbers": [1, 2, 3, 4, 5],
#   "statistics": {
#     "count": 5,
#     "mean": 3.0,
#     "median": 3,
#     "min": 1,
#     "max": 5,
#     "sum": 15
#   },
#   "success": true
# }
```

## � Why FastAPI?

This project uses **FastAPI** instead of Flask to demonstrate modern API development:

### Automatic Documentation
- **Swagger UI**: Interactive API documentation at `/docs`
- **ReDoc**: Alternative documentation at `/redoc`
- **OpenAPI Schema**: Automatically generated API specification

### Data Validation
- **Pydantic Models**: Automatic request AND response validation
- **Type Safety**: Python type hints provide IDE support and runtime validation
- **Schema Generation**: Automatic OpenAPI schema with detailed field descriptions
- **Error Messages**: Clear, detailed validation error responses

### Developer Experience
- **Auto-completion**: Full IDE support with type hints
- **Hot Reload**: Automatic server restart on code changes
- **Performance**: Built on Starlette and Uvicorn for high performance

### Example: Request & Response Validation
```python
class PowerRequest(BaseModel):
    base: Union[int, float] = Field(..., description="The base number")
    exponent: Union[int, float] = Field(..., description="The exponent")

class PowerResponse(MathOperationResponse):
    base: Union[int, float] = Field(..., description="The base number")
    exponent: Union[int, float] = Field(..., description="The exponent")
    result: Union[int, float] = Field(..., description="The power result")

@app.post("/power", response_model=PowerResponse)
async def api_power(request: PowerRequest) -> PowerResponse:
    # FastAPI automatically validates request AND response
    # Type hints provide full IDE support and runtime validation
    result = power(request.base, request.exponent)
    return PowerResponse(
        operation="power",
        base=request.base,
        exponent=request.exponent,
        result=result
    )
```

## �🔧 Architecture Principles

### 1. Separation of Business Logic from API

**❌ Bad Example** (Business logic mixed with API):
```python
@app.route('/square/<int:number>')
def square_endpoint(number):
    result = number * number  # Business logic in API layer
    return {"result": result}
```

**✅ Good Example** (Our approach):
```python
# Business Logic (src/math_operations.py)
def square(number):
    """Pure business logic function"""
    return number ** 2

# API Layer (app.py)
@app.route('/square/<number>')
def api_square(number):
    """API endpoint delegates to business logic"""
    result = square(float(number))
    return {"result": result}
```

### 2. Multiple Interfaces to Same Logic

The same `square()` function is used by:
- REST API endpoint: `GET /square/5`
- CLI command: `python cli.py square 5`
- Unit tests: `test_square_positive_integer()`

### 3. Testable Business Logic

Because business logic is separated:
- Tests are fast (no HTTP requests needed)
- Tests are focused (only testing mathematical logic)
- Tests are reliable (no network dependencies)

## 🧪 Testing Philosophy

This project includes **88 comprehensive tests** using Python's built-in **unittest framework**:

### Unit Tests (30 tests) - Business Logic Focus

```python
class TestSquareFunction(unittest.TestCase):
    def test_square_positive_integer(self):
        """Test the mathematical operation directly"""
        self.assertEqual(square(5), 25)  # Fast, focused, reliable
        self.assertEqual(square(10), 100)
        self.assertEqual(square(1), 1)
```

### API Integration Tests (31 tests) - HTTP Endpoint Testing

```python
class TestGETEndpoints(unittest.TestCase):
    def test_square_positive_integer(self):
        """Test API endpoint with HTTP requests"""
        response = client.get("/square/5")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["result"], 25)
```

### CLI Integration Tests (27 tests) - Command Line Testing

```python
class TestSquareCommand(unittest.TestCase):
    def test_square_positive_integer(self):
        """Test CLI commands via subprocess"""
        result = self.run_cli_command("square", "5")
        self.assertEqual(result.returncode, 0)
        self.assertIn("Result: 25", result.stdout)
```

## 📚 Key Learning Points

### 1. APIs are Interfaces, Not Business Logic
- APIs should be thin layers that expose business functionality
- The real value is in the business logic, not the API wrapper
- Business logic should be usable without the API

### 2. Separation Enables Reusability
- Same logic works via REST API, CLI, batch jobs, etc.
- Easy to change interfaces without touching business logic
- Business logic can be tested independently

### 3. Error Handling at Multiple Layers
- **Business Logic**: Validates inputs, raises exceptions
- **API Layer**: Catches exceptions, returns appropriate HTTP status codes
- **Client**: Handles HTTP errors gracefully

### 4. Comprehensive Testing Strategy
- **Unit Tests (30)**: Test business logic functions directly using unittest
- **API Integration Tests (31)**: Test HTTP endpoints with FastAPI TestClient  
- **CLI Integration Tests (27)**: Test command-line interface via subprocess
- **Total Coverage**: 88 tests covering all application layers

## 🧪 Why unittest Framework?

This project uses Python's built-in **unittest framework** instead of external testing libraries:

### ✅ Benefits of unittest
- **Built-in**: No external dependencies required
- **Standard**: Official Python testing framework 
- **Mature**: Well-documented with extensive features
- **IDE Support**: Better integration with many development tools
- **Self-contained**: Tests run without additional packages
- **Familiar**: Standard approach most Python developers know

### 🔄 Test Organization
The unittest framework provides excellent organization with:
- **Test Classes**: Group related tests using `unittest.TestCase`
- **Setup/Teardown**: Built-in methods for test preparation and cleanup
- **Rich Assertions**: Comprehensive assertion methods (`assertEqual`, `assertIn`, etc.)
- **Test Discovery**: Automatic test collection with `python -m unittest discover`

### 📊 Comprehensive Test Coverage
```bash
# All 88 tests covering three testing layers:
uv run python -m unittest discover -s tests -p "test_*.py"

# Output:
# ..................................................................
# ----------------------------------------------------------------------
# Ran 88 tests in 0.783s
# OK
```

## 🚀 Next Steps for Learning

1. **Add Authentication**: Implement API keys or JWT tokens
2. **Add Rate Limiting**: Prevent API abuse
3. **Add Logging**: Track API usage and errors
4. **Add Input Validation**: Validate request schemas
5. **Add Database**: Store calculation history
6. **Add Caching**: Cache expensive calculations
7. **Add Documentation**: Generate API docs with Swagger/OpenAPI

## 🛠️ Development Commands

```bash
# Install development dependencies
uv add --dev httpx black isort mypy

# Run all 88 tests
uv run python -m unittest discover -s tests -p "test_*.py" -v

# Run specific test categories
uv run python -m unittest tests.unit.test_math_operations -v           # Unit tests
uv run python -m unittest tests.integration.test_api_integration -v    # API tests  
uv run python -m unittest tests.integration.test_cli_integration -v    # CLI tests

# Format code
uv run black src/ tests/ app.py cli.py

# Sort imports
uv run isort src/ tests/ app.py cli.py

# Type checking
uv run mypy src/

# Test individual files directly
uv run python tests/unit/test_math_operations.py
uv run python tests/integration/test_api_integration.py
uv run python tests/integration/test_cli_integration.py
```

## 📝 Notes for Blog Post

This project serves as a practical example for explaining:

1. **Why separate business logic from APIs**: Enables multiple interfaces, easier testing, better reusability
2. **How to structure API projects**: Clear separation of concerns with focused modules  
3. **Testing best practices**: Test business logic directly, not through HTTP
4. **API design principles**: RESTful endpoints, proper status codes, consistent response formats

The project demonstrates that **APIs are interfaces to business value, not the business value itself**.

---

*This project is designed for educational purposes to teach API design concepts to junior developers.*