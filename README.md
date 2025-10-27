# Sample API Project - Full-Stack Educational Demo

A comprehensive educational full-stack application demonstrating modern API design patterns, clean architecture principles, and full-stack development best practices. This project showcases how to build scalable, maintainable applications with clear separation of concerns.

## 🎯 Project Overview

This is a complete full-stack application consisting of:

- **Backend API**: FastAPI-based REST API with mathematical operations
- **Frontend Web App**: React-based interactive web interface  
- **Command Line Interface**: Direct access to business logic via CLI
- **Docker Deployment**: Full containerization with Docker Compose
- **Comprehensive Testing**: 88+ tests across unit, integration, and API layers

The project demonstrates **separation of concerns** by implementing the same mathematical business logic accessible through multiple interfaces: REST API, web interface, and command-line tools.

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
uv run python app.py
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
│   │   └── math_operations.py        # 🧠 Core Business Logic
│   ├── tests/
│   │   ├── unit/                     # ✅ Business Logic Tests
│   │   └── integration/              # 🔗 API & CLI Tests  
│   ├── app.py                        # 🚀 FastAPI Application
│   ├── cli.py                        # 💻 Command Line Interface
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

## 🌐 API Documentation

- **Interactive Docs (Swagger UI)**: http://localhost:8000/docs
- **Alternative Docs (ReDoc)**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/health

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

# Run all 88 tests
uv run python -m unittest discover -s tests -p "test_*.py" -v

# Run specific test categories
uv run python -m unittest tests.unit.test_math_operations -v           # Unit tests (30)
uv run python -m unittest tests.integration.test_api_integration -v    # API tests (31)  
uv run python -m unittest tests.integration.test_cli_integration -v    # CLI tests (27)
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
- **pytest/unittest**: Comprehensive testing framework
- **Black, isort, mypy**: Code formatting and quality tools

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

### 3. **Modern Full-Stack Architecture**
- RESTful API design with proper HTTP methods and status codes
- Interactive frontend with real-time API communication
- Containerized deployment with service orchestration
- Comprehensive error handling and user feedback

### 4. **Testing Best Practices**
- **Unit Tests**: Fast, focused tests of business logic functions
- **Integration Tests**: HTTP endpoint testing with FastAPI TestClient
- **CLI Integration Tests**: Command-line interface testing via subprocess
- 88+ tests providing comprehensive coverage across all application layers

### 5. **Production-Ready Patterns**
- Docker containerization for consistent deployment
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
- Add CI/CD pipelines (GitHub Actions)
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

*This project serves as a comprehensive example of modern full-stack development, demonstrating how to build scalable, maintainable applications with clear architectural boundaries and comprehensive testing.*