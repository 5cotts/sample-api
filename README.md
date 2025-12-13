# Sample API Project - Full-Stack Educational Demo

A comprehensive educational full-stack application demonstrating modern API design patterns, clean architecture principles, and full-stack development best practices. This project showcases how to build scalable, maintainable applications with clear separation of concerns.

## 🎯 Project Overview

This is a complete full-stack application consisting of:

- **Backend API**: FastAPI-based REST API with mathematical operations
- **Frontend Web App**: React-based interactive web interface  
- **Command Line Interface**: Direct access to business logic via CLI
- **Docker Deployment**: Full containerization with Docker Compose
- **Comprehensive Testing**: 94+ tests across unit, integration, and API layers
- **Dual Implementation**: Both functional and object-oriented programming paradigms

The project demonstrates **separation of concerns** by implementing the same mathematical business logic accessible through multiple interfaces: REST API, web interface, and command-line tools. It also showcases both **functional** and **object-oriented** programming approaches, with runtime switching between implementations.

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Full-Stack Architecture                   │
├─────────────────────────────────────────────────────────────┤
│  Frontend (React + Vite)     │  Backend (FastAPI + Python)  │
│  ├── Interactive Web UI      │  ├── REST API Endpoints      │
│  ├── Real-time API calls     │  ├── Request/Response Models │
│  ├── Error handling          │  ├── Data validation         │
│  └── Responsive design       │  └── Auto-generated docs     │
├─────────────────────────────────────────────────────────────┤
│               Shared Business Logic Layer                    │
│  ├── Pure mathematical functions (no dependencies)          │
│  ├── Comprehensive input validation                         │
│  ├── Testable and reusable components                       │
│  └── Available via API, CLI, and direct import              │
└─────────────────────────────────────────────────────────────┘
```

## 🚀 Quick Start

### Option 1: Docker Compose (Recommended)

```bash
# Start both frontend and backend services
docker-compose up --build

# Access the application:
# - Frontend: http://localhost:3000
# - Backend API: http://localhost:8000
# - API Docs: http://localhost:8000/docs
```

### Option 2: Local Development

**Backend:**
```bash
cd backend
uv sync --dev

# Use functional implementation (default)
uv run python app.py

# Or use OOP implementation
MATH_OPERATIONS_IMPL=oop uv run python app.py

# API available at http://localhost:8000
```

**Frontend:**
```bash
cd frontend  
npm install
npm run dev
# Web app available at http://localhost:5173
```

## 📁 Project Structure

```
sample-api/
├── backend/                          # FastAPI Backend
│   ├── src/
│   │   ├── math_operations/          # 🧮 Math Operations Package
│   │   │   ├── __init__.py          # Package exports
│   │   │   ├── functional.py        # ⚡ Functional Implementation
│   │   │   └── oop.py              # 🏛️ OOP Implementation
│   │   └── data_parsing.py          # 📊 Data Processing Logic
│   ├── tests/
│   │   ├── unit/                     # ✅ Business Logic Tests
│   │   │   ├── math_operations/     # Tests matching source structure
│   │   │   │   ├── test_functional.py
│   │   │   │   └── test_oop.py
│   │   │   └── test_data_parsing.py
│   │   └── integration/              # 🔗 API & CLI Tests  
│   ├── app.py                        # 🚀 FastAPI Application
│   ├── cli.py                        # 💻 Command Line Interface
│   ├── IMPLEMENTATION_SWITCH.md      # 📖 Implementation Switching Guide
│   ├── pyproject.toml                # 📦 Python Dependencies
│   └── Dockerfile                    # 🐳 Backend Container
├── frontend/                         # React Frontend
│   ├── src/
│   │   ├── components/               # ⚛️ React Components
│   │   ├── services/                 # 🌐 API Integration Layer
│   │   └── App.jsx                   # 📱 Main Application
│   ├── package.json                  # 📦 Node Dependencies
│   └── Dockerfile                    # 🐳 Frontend Container
├── docs/                             # 📖 Documentation
├── docker-compose.yml                # 🐳 Full-Stack Deployment
└── README.md                         # 📋 This file
```

## 🔧 Available Operations

The application provides both **GET** and **POST** endpoints demonstrating different API patterns:

### Mathematical Operations
- **Square Calculation**: Calculate n²
- **Power Calculation**: Calculate base^exponent
- **Factorial**: Calculate n! for integers
- **Fibonacci Sequence**: Generate first N Fibonacci numbers
- **Prime Number Check**: Determine if a number is prime
- **Statistics**: Calculate mean, median, min, max for datasets

### Access Methods
Each operation is available through:
1. **Web Interface**: Interactive React components at `http://localhost:3000`
2. **REST API**: HTTP endpoints at `http://localhost:8000`
3. **Command Line**: Direct CLI access via `python cli.py`

### Implementation Paradigms
The project includes two implementations of the same business logic:
- **Functional Implementation**: Pure functions with no side effects (default)
- **Object-Oriented Implementation**: Class-based design with instance methods

Switch between implementations using the `MATH_OPERATIONS_IMPL` environment variable:
- `MATH_OPERATIONS_IMPL=functional` (default) - Uses functional programming approach
- `MATH_OPERATIONS_IMPL=oop` - Uses object-oriented programming approach

See [backend/IMPLEMENTATION_SWITCH.md](backend/IMPLEMENTATION_SWITCH.md) for detailed usage instructions.

## 🌐 API Documentation

- **Interactive Docs (Swagger UI)**: http://localhost:8000/docs
- **Alternative Docs (ReDoc)**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/health (shows active implementation: functional or object-oriented)

### Example API Usage

```bash
# GET endpoints
curl http://localhost:8000/square/5
curl http://localhost:8000/fibonacci/10
curl http://localhost:8000/prime/17

# POST endpoints  
curl -X POST http://localhost:8000/power \
  -H "Content-Type: application/json" \
  -d '{"base": 2, "exponent": 8}'

curl -X POST http://localhost:8000/stats \
  -H "Content-Type: application/json" \
  -d '{"numbers": [1, 2, 3, 4, 5]}'
```

## 💻 Command Line Interface

Direct access to business logic without the API layer:

```bash
cd backend

# Mathematical operations via CLI
uv run python cli.py square 5
uv run python cli.py power 2 8  
uv run python cli.py factorial 5
uv run python cli.py fibonacci 10
uv run python cli.py prime 17
uv run python cli.py stats 1 2 3 4 5
```

## 🧪 Testing

The project includes comprehensive testing across multiple layers:

```bash
cd backend

# Run all 94+ tests
uv run python -m unittest discover -s tests -p "test_*.py" -v

# Run specific test categories
uv run python -m unittest tests.unit.math_operations.test_functional -v  # Functional unit tests (30)
uv run python -m unittest tests.unit.math_operations.test_oop -v        # OOP unit tests (34)
uv run python -m unittest tests.integration.test_api_integration -v      # API tests (31)  
uv run python -m unittest tests.integration.test_cli_integration -v      # CLI tests (27)
```

### Test Coverage
- **Functional Implementation Tests**: 30 unit tests covering all mathematical operations
- **OOP Implementation Tests**: 34 unit tests including class instantiation and method testing
- **Integration Tests**: 58 tests covering API endpoints and CLI commands
- **Total**: 94+ tests ensuring both implementations work correctly

## 🔍 Code Quality & Linting

The project uses multiple tools to maintain code quality:
- **black**, **isort**, **mypy**: Configured in `backend/pyproject.toml`
- **flake8**: Configured in `backend/.flake8`

### Formatting
```bash
cd backend

# Format code with black
uv run black .

# Sort imports with isort
uv run isort .
```

### Type Checking
```bash
cd backend

# Run mypy type checking
uv run mypy src/
```

### Linting
```bash
cd backend

# Run flake8 style linting
uv run flake8 src/ app.py cli.py

# Or lint entire directory (excludes .venv, __pycache__, etc.)
uv run flake8 .
```

### Run All Checks
```bash
cd backend

# Format code
uv run black .

# Sort imports
uv run isort .

# Type checking
uv run mypy src/

# Linting
uv run flake8 .
```

All tools are configured to work together:
- **black**: Code formatter (88 character line length)
- **isort**: Import sorter (configured to work with black)
- **mypy**: Static type checker (strict mode)
- **flake8**: Style guide enforcement

## 🔄 CI/CD Pipeline

The project includes a GitHub Actions CI pipeline that automatically runs on every push and pull request to verify code quality and build success.

### What the CI Pipeline Checks

1. **Docker Builds**: Verifies that both backend and frontend Docker images build successfully
   - Backend Docker image compilation
   - Frontend Docker image compilation

2. **Backend Linting**: Enforces code quality standards for Python code
   - `black` - Code formatting check
   - `isort` - Import sorting validation
   - `flake8` - Style guide enforcement
   - `mypy` - Type checking

3. **Frontend Linting**: Ensures JavaScript/React code quality
   - ESLint with React-specific rules

4. **Backend Unit Tests**: Verifies all unit tests pass
   - Runs all tests in `backend/tests/unit/`

### CI Status

The CI pipeline runs automatically on:
- Every push to any branch
- All pull requests to `main`

All checks must pass before code can be merged, ensuring consistent code quality across the project.

### Local CI Verification

You can run the same checks locally before pushing:

```bash
# Backend checks
cd backend
uv run black --check .
uv run isort --check-only .
uv run flake8 src/ app.py cli.py
uv run mypy src/
uv run python -m unittest discover -s tests/unit -p 'test_*.py' -v

# Frontend checks
cd frontend
npm ci
npm run lint
```

## 🛠️ Technology Stack

### Backend
- **FastAPI**: Modern Python web framework with automatic API documentation
- **Pydantic**: Data validation and settings management using Python type hints
- **Uvicorn**: ASGI web server for Python
- **Python 3.11+**: Latest Python features and performance improvements

### Frontend  
- **React 18**: Modern React with functional components and hooks
- **Vite**: Fast build tool and development server
- **Axios**: Promise-based HTTP client for API communication
- **Vanilla CSS**: Custom styling for educational clarity (no UI frameworks)

### Development & Deployment
- **uv**: Fast Python package manager
- **Docker & Docker Compose**: Containerization and orchestration
- **GitHub Actions**: CI/CD pipeline for automated testing and linting
- **pytest/unittest**: Comprehensive testing framework
- **Black, isort, mypy, flake8**: Code formatting and quality tools
- **ESLint**: JavaScript/React code linting

## 📚 Educational Value

This project demonstrates key software engineering concepts:

### 1. **Separation of Concerns**
- Business logic isolated in pure functions
- API layer acts as thin interface to business logic  
- Frontend focused solely on user interface and experience
- Each layer can be developed, tested, and deployed independently

### 2. **Multiple Interface Patterns**
- Same business logic accessible via REST API, web UI, and CLI
- Demonstrates how interfaces are separate from core functionality
- Shows flexibility and reusability of well-designed business logic

### 2a. **Programming Paradigm Comparison**
- **Functional Programming**: Pure functions with no side effects, easily testable
- **Object-Oriented Programming**: Class-based design with encapsulation and extensibility
- **Runtime Switching**: Environment variable allows switching between implementations
- Both implementations provide identical functionality, demonstrating paradigm equivalence

### 3. **Modern Full-Stack Architecture**
- RESTful API design with proper HTTP methods and status codes
- Interactive frontend with real-time API communication
- Containerized deployment with service orchestration
- Comprehensive error handling and user feedback

### 4. **Testing Best Practices**
- **Unit Tests**: Fast, focused tests of business logic functions (both functional and OOP)
- **Integration Tests**: HTTP endpoint testing with FastAPI TestClient
- **CLI Integration Tests**: Command-line interface testing via subprocess
- 94+ tests providing comprehensive coverage across all application layers and both implementations

### 5. **Production-Ready Patterns**
- Docker containerization for consistent deployment
- CI/CD pipeline with automated testing and linting
- Health checks and monitoring endpoints
- CORS configuration for cross-origin requests
- Comprehensive error handling and logging
- API documentation generation

## 🚢 Deployment

### Development
```bash
# Development with hot-reload
docker-compose -f docker-compose.dev.yml up --build
```

### Production
```bash
# Production deployment
docker-compose up --build -d

# Check service health
docker-compose ps
curl http://localhost:8000/health
curl http://localhost:3000/health
```

## 🤝 Contributing & Learning

This project is designed for educational purposes. Key areas for exploration:

### Backend Enhancements
- Add authentication (JWT tokens, API keys)
- Implement caching (Redis)
- Add database integration (PostgreSQL)
- Implement rate limiting
- Add comprehensive logging

### Frontend Improvements  
- Add routing (React Router)
- Implement state management (Context API, Redux)
- Add TypeScript for type safety
- Implement testing (Jest, React Testing Library)
- Add UI component library (Material-UI, Tailwind)

### DevOps & Infrastructure
- ✅ CI/CD pipelines (GitHub Actions) - Implemented
- Implement monitoring (Prometheus, Grafana)
- Add load balancing (Nginx)
- Database migrations and seeding
- Environment-specific configurations

## 📄 License

This is an educational project designed to demonstrate full-stack development concepts and API design patterns.

---

## 🎓 Learning Resources

- **FastAPI Documentation**: https://fastapi.tiangolo.com/
- **React Documentation**: https://react.dev/
- **Docker Documentation**: https://docs.docker.com/
- **API Design Best Practices**: REST principles, HTTP status codes, error handling
- **Full-Stack Architecture**: Separation of concerns, service communication, deployment strategies

## 🤖 AI-Assisted Development with Cursor

This project is optimized for AI-assisted development using [Cursor IDE](https://cursor.sh/). The project structure includes AGENTS.md files that provide context-aware instructions to AI agents.

### AGENTS.md Structure

The project uses a hierarchical AGENTS.md system:
- **Root [AGENTS.md](AGENTS.md)**: Overview and navigation for the entire project
- **Backend [backend/AGENTS.md](backend/AGENTS.md)**: Backend-specific template instructions
- **Frontend [frontend/AGENTS.md](frontend/AGENTS.md)**: Frontend patterns and architecture
- **Components [frontend/src/components/AGENTS.md](frontend/src/components/AGENTS.md)**: Component development guidelines

### How It Works

When working in a specific directory, Cursor (and other AI tools) automatically reference the nearest AGENTS.md file:
- Working in `backend/` → Uses `backend/AGENTS.md` for backend-specific context
- Working in `frontend/src/components/` → Uses component-specific guidelines
- Working at project root → Uses global instructions from root `AGENTS.md`

### Custom Cursor Commands

The project includes custom commands in `.cursor/commands/`:

- **`/commit-message`**: Generate conventional commit messages following project standards
- **`/pr-summary`**: Generate PR descriptions with conventional commit format
- **`/setup-repo`**: Generate repository setup guide based on AGENTS.md files

### Benefits

- **Context-Aware Assistance**: AI agents understand project structure and patterns based on current directory
- **Consistent Patterns**: AGENTS.md files ensure AI follows established patterns and conventions
- **Template-Friendly**: Easy to adapt the project structure for new domains while maintaining patterns
- **Better Code Generation**: AI agents generate code that matches project architecture and style

### Getting Started with Cursor

1. Open the project in Cursor IDE
2. Navigate to any directory - Cursor will automatically reference the relevant AGENTS.md
3. Use `@AGENTS.md` in chat to explicitly reference instructions
4. Try the custom commands (`/commit-message`, `/pr-summary`, `/setup-repo`) for common tasks

The AGENTS.md system enables more accurate and context-aware AI assistance throughout the development process.

## 📚 Additional Documentation

- **Using as a Template**: See [AGENTS.md](AGENTS.md) for template instructions and customization guide
- **Backend Template Guide**: See [backend/AGENTS.md](backend/AGENTS.md) for complete backend template
- **Implementation Switching**: See [backend/IMPLEMENTATION_SWITCH.md](backend/IMPLEMENTATION_SWITCH.md) for details on switching between functional and OOP implementations
- **Frontend Patterns**: See [frontend/AGENTS.md](frontend/AGENTS.md) for React application patterns
- **Component Guidelines**: See [frontend/src/components/AGENTS.md](frontend/src/components/AGENTS.md) for component patterns
- **Template Documentation**: See [docs/template/](docs/template/) for detailed template files

*This project serves as a comprehensive example of modern full-stack development, demonstrating how to build scalable, maintainable applications with clear architectural boundaries and comprehensive testing.*