# Sample API Project - Full Stack# Sample API Project - Full Stack# Sample API Project



An educational Python REST API project with React frontend demonstrating key API design concepts for junior engineers.



## 🎯 Learning ObjectivesAn educational Python REST API project with frontend interface demonstrating key API design concepts for junior engineers.An educational Python REST API project demonstrating key API design concepts for junior engineers.



This project demonstrates several important software engineering concepts:



1. **Separation of Concerns**: Business logic is completely separated from API implementation## 🏗️ Project Structure## 🎯 Learning Objectives

2. **Multiple Interfaces**: Same business logic accessible via REST API, CLI, and web UI

3. **Full Stack Architecture**: Backend API with React frontend client

4. **Comprehensive Testing**: 88+ tests across unit, integration, and frontend layers

5. **API Design**: RESTful endpoints with proper HTTP methods and status codes```This project demonstrates several important software engineering concepts:

6. **Modern Frameworks**: FastAPI backend with React frontend

sample-api/

## 🏗️ Project Structure

├── backend/                    # FastAPI REST API1. **Separation of Concerns**: Business logic is completely separated from API implementation

```

sample-api/│   ├── src/                    # Business logic2. **Multiple Interfaces**: Same business logic accessible via REST API and CLI

├── backend/                         # FastAPI REST API

│   ├── src/│   ├── tests/                  # Comprehensive test suite3. **Comprehensive Testing**: 88 tests across unit, API integration, and CLI integration layers

│   │   └── math_operations.py       # 🧠 Business Logic (Pure Functions)

│   ├── tests/│   ├── app.py                  # FastAPI application4. **Testing Framework**: Uses Python's built-in unittest framework (no external dependencies)

│   │   ├── unit/

│   │   │   └── test_math_operations.py    # ✅ Unit Tests (30 tests)│   ├── cli.py                  # Command-line interface5. **API Design**: RESTful endpoints with proper HTTP methods and status codes

│   │   └── integration/

│   │       ├── test_api_integration.py    # 🔗 API Integration Tests (31 tests)│   └── pyproject.toml          # Python dependencies6. **Modern API Framework**: FastAPI provides automatic documentation, data validation, and type safety

│   │       └── test_cli_integration.py    # 💻 CLI Integration Tests (27 tests)

│   ├── app.py                       # 🚀 FastAPI REST API├── frontend/                   # Web interface (coming soon)

│   ├── cli.py                       # 💻 Command Line Interface

│   └── pyproject.toml               # 📦 Python Dependencies & Configuration└── docker-compose.yml          # Local development setup (coming soon)## 📁 Project Structure

├── frontend/                        # React Web Interface

│   ├── src/```

│   │   ├── components/              # React Components

│   │   │   ├── SquareCalculator.jsx```

│   │   │   ├── PowerCalculator.jsx

│   │   │   ├── FactorialCalculator.jsx## 🎯 Learning Objectivessample-api/

│   │   │   ├── FibonacciGenerator.jsx

│   │   │   ├── PrimeChecker.jsx├── src/

│   │   │   └── StatisticsCalculator.jsx

│   │   ├── services/This project demonstrates several important software engineering concepts:│   └── math_operations.py           # 🧠 Business Logic (Pure Functions)

│   │   │   └── api.js               # API client with error handling

│   │   ├── App.jsx                  # Main React application├── tests/

│   │   └── main.jsx                 # React entry point

│   ├── public/                      # Static assets1. **Separation of Concerns**: Business logic separated from API and frontend│   ├── test_math_operations.py      # ✅ Unit Tests (30 tests)

│   ├── package.json                 # Node.js dependencies

│   └── vite.config.js               # Vite build configuration2. **Multiple Interfaces**: Same business logic accessible via REST API, CLI, and web UI│   ├── test_api_integration.py      # 🔗 API Integration Tests (31 tests)

└── docs/                            # Additional documentation

```3. **Full Stack Architecture**: Backend API with frontend client│   └── test_cli_integration.py      # 💻 CLI Integration Tests (27 tests)



## 🚀 Quick Start4. **Containerization**: Docker setup for local development├── app.py                           # 🚀 FastAPI REST API



### Prerequisites5. **Comprehensive Testing**: 88+ tests across unit, integration, and frontend layers├── cli.py                           # 💻 Command Line Interface



- **Backend**: Python 3.11+ and [uv](https://docs.astral.sh/uv/) package manager├── pyproject.toml                   # 📦 Dependencies & Configuration

- **Frontend**: Node.js 18+ and npm

## 🚀 Quick Start└── README.md                        # 📖 Documentation

### Backend Setup

```

```bash

# Navigate to backend directory### Backend API

cd backend

## 🚀 Quick Start

# Install dependencies

uv sync --dev```bash



# Run the API# Navigate to backend### Prerequisites

uv run python app.py

```cd backend- Python 3.11+ 



The API will be available at:- [uv](https://docs.astral.sh/uv/) package manager

- **API endpoints**: `http://localhost:8000`

- **Interactive docs**: `http://localhost:8000/docs`# Install dependencies

- **OpenAPI schema**: `http://localhost:8000/openapi.json`

uv sync --dev### Installation

### Frontend Setup



```bash

# Navigate to frontend directory# Run the API```bash

cd frontend

uv run python app.py# Clone or download the project

# Install dependencies

npm install```cd sample-api



# Start development server

npm run dev

```The API will be available at:# Install dependencies with uv



The frontend will be available at `http://localhost:5173`- **API endpoints**: `http://localhost:8000`uv add fastapi uvicorn requests



### CLI Usage- **Interactive docs**: `http://localhost:8000/docs`uv add --dev httpx  # For FastAPI TestClient



```bash

# Navigate to backend directory

cd backend### Frontend (Coming Soon)# Or install from pyproject.toml



# Use the command-line interfaceuv sync --dev

uv run python cli.py square 5

uv run python cli.py power 2 8The frontend will provide a web interface to interact with the mathematical operations API.```

uv run python cli.py factorial 5

uv run python cli.py fibonacci 10

uv run python cli.py is_prime 17

uv run python cli.py stats "1,2,3,4,5"```

### Using Docker 🐳

#### Production Setup (Recommended)

```bash
# Build and run both services
docker-compose up --build

# Run in background
docker-compose up -d --build

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

Services will be available at:
- **Frontend**: `http://localhost:3000`
- **Backend API**: `http://localhost:8000`
- **API Docs**: `http://localhost:8000/docs`

#### Development Setup with Docker

```bash
# Run development environment with hot reloading
docker-compose -f docker-compose.dev.yml up --build

# Run specific service
docker-compose -f docker-compose.dev.yml up backend
docker-compose -f docker-compose.dev.yml up frontend-dev
```

#### Docker Commands

```bash
# Rebuild containers
docker-compose build --no-cache

# View running containers
docker-compose ps

# Execute commands in running container
docker-compose exec backend uv run python -m pytest
docker-compose exec frontend-dev npm test

# Clean up
docker-compose down -v --remove-orphans
docker system prune -a
```### Running the API

```



## 🧪 Testing

```bash```bash

### Backend Tests

# Run both frontend and backend# Start the FastAPI development server

```bash

cd backenddocker-compose up --builduv run python app.py



# Run all tests```

uv run python -m pytest tests/ -v

# Alternative: Use uvicorn directly

# Run specific test categories

uv run python -m pytest tests/unit/ -v          # Unit tests only## 📚 API Endpointsuv run uvicorn app:app --reload --host 0.0.0.0 --port 8000

uv run python -m pytest tests/integration/ -v   # Integration tests only

```

# Run with coverage

uv run python -m pytest tests/ --cov=src --cov-report=html### GET Endpoints

```

- `GET /` - API informationThe API will be available at:

### Frontend Tests

- `GET /health` - Health check- **API endpoints**: `http://localhost:8000`

```bash

cd frontend- `GET /square/{number}` - Calculate square- **Interactive docs (Swagger UI)**: `http://localhost:8000/docs`



# Run tests (when implemented)- `GET /factorial/{number}` - Calculate factorial- **Alternative docs (ReDoc)**: `http://localhost:8000/redoc`

npm test

```- `GET /fibonacci/{count}` - Generate Fibonacci sequence



## 🔧 API Endpoints- `GET /prime/{number}` - Check if prime### Running Tests



### Mathematical Operations



| Method | Endpoint | Description | Example |### POST Endpoints```bash

|--------|----------|-------------|---------|

| GET | `/square/{number}` | Calculate square of number | `/square/5` → `25` |- `POST /power` - Calculate base^exponent# Run all tests (unit + integration)

| POST | `/power` | Calculate power | `{"base": 2, "exponent": 8}` → `256` |

| GET | `/factorial/{number}` | Calculate factorial | `/factorial/5` → `120` |- `POST /stats` - Calculate statisticsuv run python -m unittest discover -s tests -p "test_*.py" -v

| GET | `/fibonacci/{n}` | Generate Fibonacci sequence | `/fibonacci/10` → `[0,1,1,2,3,5,8,13,21,34]` |

| GET | `/is_prime/{number}` | Check if number is prime | `/is_prime/17` → `true` |

| POST | `/statistics` | Calculate statistics | `{"numbers": [1,2,3,4,5]}` → `{"mean": 3.0, ...}` |

## 🧪 Running Tests# Run specific test modules

### Utility Endpoints

uv run python -m unittest tests.test_math_operations -v

| Method | Endpoint | Description |

|--------|----------|-------------|```bashuv run python -m unittest tests.test_api_integration -v

| GET | `/health` | Health check |

| GET | `/docs` | Interactive API documentation |cd backenduv run python -m unittest tests.test_cli_integration -v

| GET | `/openapi.json` | OpenAPI schema |



## 📝 Example Usage

# Run all tests# Run tests without verbose output

### cURL Examples

uv run python -m unittest discover -s tests -p "test_*.py" -vuv run python -m unittest discover -s tests -p "test_*.py"

```bash

# Square calculation```

curl "http://localhost:8000/square/5"

# Run specific test categories

# Power calculation

curl -X POST "http://localhost:8000/power" \uv run python -m unittest tests.unit.test_math_operations -v     # Unit tests### Using the CLI

  -H "Content-Type: application/json" \

  -d '{"base": 2, "exponent": 8}'uv run python -m unittest tests.integration.test_api_integration -v  # API tests



# Factorial calculationuv run python -m unittest tests.integration.test_cli_integration -v  # CLI tests```bash

curl "http://localhost:8000/factorial/5"

```# Test business logic directly via command line

# Fibonacci sequence

curl "http://localhost:8000/fibonacci/10"uv run python cli.py square 5



# Prime check## 🛠️ Developmentuv run python cli.py power 2 8

curl "http://localhost:8000/is_prime/17"

uv run python cli.py factorial 5

# Statistics calculation

curl -X POST "http://localhost:8000/statistics" \### Code Qualityuv run python cli.py fibonacci 10

  -H "Content-Type: application/json" \

  -d '{"numbers": [1, 2, 3, 4, 5]}'uv run python cli.py prime 17

```

```bashuv run python cli.py stats 1 2 3 4 5

### Python Client Example

cd backend```

```python

import requests



# Base URL# Format code## 🌐 API Endpoints

BASE_URL = "http://localhost:8000"

uv run black src/ tests/ app.py cli.py

# Square calculation

response = requests.get(f"{BASE_URL}/square/5")### GET Endpoints

print(f"Square of 5: {response.json()}")

# Sort imports  

# Power calculation

response = requests.post(f"{BASE_URL}/power", uv run isort src/ tests/ app.py cli.py#### Root Information

                        json={"base": 2, "exponent": 8})

print(f"2^8 = {response.json()}")```bash



# Statistics calculation# Type checkingcurl http://localhost:8000/

response = requests.post(f"{BASE_URL}/statistics",

                        json={"numbers": [1, 2, 3, 4, 5]})uv run mypy src/# Response: API info with available endpoints and documentation links

print(f"Statistics: {response.json()}")

``````



## 🎨 Frontend Features# Linting



The React frontend provides an interactive interface for all mathematical operations:uv run flake8 src/ tests/ app.py cli.py#### Health Check



- **Square Calculator**: Input a number to calculate its square``````bash

- **Power Calculator**: Calculate base raised to an exponent

- **Factorial Calculator**: Calculate factorial of a numbercurl http://localhost:8000/health

- **Fibonacci Generator**: Generate Fibonacci sequence up to n terms

- **Prime Checker**: Check if a number is prime### CLI Usage# Response: {"status": "healthy", "service": "math-operations-api"}

- **Statistics Calculator**: Calculate mean, median, mode, and standard deviation

```

## 🏗️ Architecture Decisions

```bash

### Backend Architecture

- **FastAPI**: Modern, fast web framework with automatic API documentationcd backend#### Interactive Documentation

- **Pydantic**: Data validation and serialization

- **Pure Functions**: Business logic in `math_operations.py` has no dependencies```bash

- **Separation of Concerns**: API layer (`app.py`) separate from business logic

- **Multiple Interfaces**: Same logic accessible via REST API and CLI# Test business logic directly# Open in browser for interactive API testing



### Frontend Architectureuv run python cli.py square 5open http://localhost:8000/docs

- **React 18**: Modern functional components with hooks

- **Vite**: Fast build tool and development serveruv run python cli.py power 2 8```

- **Axios**: HTTP client with error handling

- **Component-Based**: Each operation has its own componentuv run python cli.py factorial 5

- **API Service Layer**: Centralized API communication logic

uv run python cli.py fibonacci 10#### Calculate Square

### Testing Strategy

- **Unit Tests**: Test pure business logic functionsuv run python cli.py prime 17```bash

- **Integration Tests**: Test API endpoints and CLI interface

- **Error Handling**: Comprehensive error scenarios covereduv run python cli.py stats 1 2 3 4 5curl http://localhost:8000/square/5



## 🚀 Development Workflow```# Response: {"operation": "square", "input": 5, "result": 25, "success": true}



1. **Start Backend**: `cd backend && uv run python app.py`

2. **Start Frontend**: `cd frontend && npm run dev`

3. **Run Tests**: `cd backend && uv run python -m pytest tests/ -v`## 📖 Documentationcurl http://localhost:8000/square/2.5

4. **View API Docs**: Visit `http://localhost:8000/docs`

5. **Use Frontend**: Visit `http://localhost:5173`# Response: {"operation": "square", "input": 2.5, "result": 6.25, "success": true}



## 📚 Learning Resources- **Backend API**: See `backend/` directory for detailed API documentation```



This project is designed for educational purposes. Key concepts demonstrated:- **Agent Instructions**: See `.github/agent-instructions.md` for project template instructions



- **RESTful API Design**: Proper HTTP methods, status codes, and response formats#### Calculate Factorial

- **Data Validation**: Input validation and error handling

- **Testing Strategies**: Unit, integration, and API testing## 🎓 Educational Focus```bash

- **Documentation**: Auto-generated API docs with FastAPI

- **Frontend Integration**: React components consuming REST APIcurl http://localhost:8000/factorial/5

- **Modern Development**: Contemporary tools and best practices

This project serves as a practical example for teaching:# Response: {"operation": "factorial", "input": 5, "result": 120, "success": true}

## 🤝 Contributing

```

This is an educational project. Feel free to:

- Add new mathematical operations1. **API Design Principles**: RESTful endpoints, proper HTTP methods, status codes

- Improve error handling

- Add more comprehensive tests2. **Separation of Concerns**: Business logic independent of interfaces#### Generate Fibonacci Sequence

- Enhance the frontend UI

- Add Docker configuration3. **Testing Strategies**: Unit tests for logic, integration tests for APIs```bash



## 📄 License4. **Full Stack Development**: Backend API with frontend clientcurl http://localhost:8000/fibonacci/8



This project is for educational purposes. Use freely for learning and teaching API concepts.5. **Modern Development Practices**: Docker, type hints, automated testing# Response: {"operation": "fibonacci", "count": 8, "sequence": [0, 1, 1, 2, 3, 5, 8, 13], "success": true}

```

---

#### Check Prime Number

*This project is designed for educational purposes to teach full-stack development concepts to junior developers.*```bash
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
uv run python -m unittest tests.test_math_operations -v      # Unit tests
uv run python -m unittest tests.test_api_integration -v      # API tests  
uv run python -m unittest tests.test_cli_integration -v      # CLI tests

# Format code
uv run black src/ tests/ app.py cli.py

# Sort imports
uv run isort src/ tests/ app.py cli.py

# Type checking
uv run mypy src/

# Test individual files directly
uv run python tests/test_math_operations.py
uv run python tests/test_api_integration.py
uv run python tests/test_cli_integration.py
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