# Interview Readiness Checklist

## ✅ Pre-Interview Setup Verification

This document helps you verify that your environment is ready for the AI Live Coding interview.

### Prerequisites Check

Run these commands to verify your environment:

```bash
# Python version (should be 3.11+)
python3 --version  # or python --version

# uv package manager (should be installed)
which uv

# Node.js version (should be 18+)
node --version

# Docker (optional, but useful)
docker --version

# Docker Compose (optional)
docker-compose --version
```

### Quick Environment Test

```bash
# Navigate to project root
cd /Users/scott/Documents/Code/sample-api

# Test backend dependencies
cd backend
uv sync --dev
uv run python -m unittest discover -s tests/unit -p "test_*.py" -v

# Test frontend dependencies
cd ../frontend
npm install
npm run lint
```

### Quick Start Options

**Option 1: Local Development (Recommended for Interview)**
```bash
# Terminal 1: Backend
cd backend
uv run python app.py
# API runs at http://localhost:8000

# Terminal 2: Frontend (if needed)
cd frontend
npm run dev
# Frontend runs at http://localhost:5173
```

**Option 2: Docker (Alternative)**
```bash
# Full stack with Docker
docker-compose up --build

# Or development mode with hot-reload
docker-compose -f docker-compose.dev.yml up --build
```

## 🎯 Interview Scenario Preparation

### Key Features Already Available

1. **Data Processing Capabilities** ✅
   - CSV parsing (`backend/src/data_parsing.py`)
   - JSON parsing
   - DataFrame operations (merge, filter, aggregate)
   - Sample datasets in `backend/data/`

2. **API Infrastructure** ✅
   - FastAPI with auto-documentation at `/docs`
   - Health check endpoint
   - CORS configured
   - Request/response validation with Pydantic

3. **Testing Framework** ✅
   - Unit tests for business logic
   - Integration tests for API
   - 88+ existing tests as examples

4. **Clean Architecture** ✅
   - Business logic separated from API layer
   - Easy to add new endpoints
   - Clear patterns to follow

### Expected Interview Workflow

When given a dataset and prompt:

1. **Explore the Dataset** (5-10 min)
   ```python
   from src.data_parsing import load_csv, dataframe_summary
   df = load_csv("path/to/dataset.csv")
   summary = dataframe_summary(df)
   print(summary)
   ```

2. **Add Business Logic** (15-20 min)
   - Create functions in `backend/src/` (e.g., `data_processing.py`)
   - Follow existing patterns from `math_operations.py`
   - Add unit tests

3. **Expose via API** (10-15 min)
   - Add endpoint in `backend/app.py`
   - Use existing patterns (GET/POST, Pydantic models)
   - Test via `/docs` interface

4. **Optional: Frontend Component** (5-10 min)
   - Create component following `frontend/src/components/` patterns
   - Update `App.jsx` if needed

### Quick Reference: Adding a New Feature

**Step 1: Business Logic**
```python
# backend/src/your_module.py
def your_function(input_data):
    # Pure function, no side effects
    # Validates input
    # Returns result
    pass
```

**Step 2: API Endpoint**
```python
# backend/app.py
@app.post("/your-endpoint", response_model=YourResponse)
async def api_your_function(request: YourRequest):
    result = your_function(request.data)
    return YourResponse(result=result)
```

**Step 3: Test**
```python
# backend/tests/unit/test_your_module.py
class TestYourFunction(unittest.TestCase):
    def test_basic_case(self):
        result = your_function(valid_input)
        self.assertEqual(result, expected)
```

## 📊 Dataset Workflow Examples

### Loading and Exploring Data

```python
from pathlib import Path
from src.data_parsing import load_csv, dataframe_summary, filter_dataframe

# Load dataset
data_dir = Path("backend/data")
df = load_csv(data_dir / "your_dataset.csv")

# Explore
summary = dataframe_summary(df)
print(f"Rows: {summary['row_count']}")
print(f"Columns: {summary['columns']}")

# Filter
filtered = filter_dataframe(df, "column_name", ">", 100)

# Aggregate
from src.data_parsing import aggregate_dataframe
stats = aggregate_dataframe(
    df,
    group_by="category",
    aggregations={"value": ["mean", "sum", "count"]}
)
```

### Adding Dataset Endpoint

```python
# backend/app.py
from src.data_parsing import load_csv, dataframe_summary

@app.get("/dataset/summary")
async def get_dataset_summary():
    df = load_csv("backend/data/your_dataset.csv")
    return dataframe_summary(df)
```

## 🚀 Interview Day Checklist

### Before Starting

- [ ] Verify all prerequisites installed
- [ ] Test that backend starts: `cd backend && uv run python app.py`
- [ ] Verify API docs accessible: http://localhost:8000/docs
- [ ] Have AI tool ready (Cursor, ChatGPT, Claude, etc.)
- [ ] Know where sample datasets are: `backend/data/`

### During Interview

- [ ] Start with understanding the dataset (use `dataframe_summary`)
- [ ] Ask clarifying questions about requirements
- [ ] Write tests as you build (TDD approach shows good practice)
- [ ] Use AI tools for boilerplate, but explain your logic
- [ ] Test your endpoints via `/docs` interface
- [ ] Communicate your approach and decisions

### Key Patterns to Remember

1. **Business Logic First**: Always implement in `src/` before exposing via API
2. **Validation**: Use Pydantic models for request/response validation
3. **Error Handling**: Follow existing patterns with HTTPException
4. **Testing**: Unit tests for logic, integration tests for endpoints
5. **Documentation**: FastAPI auto-generates docs at `/docs`

## 🔧 Troubleshooting

### Backend won't start
```bash
cd backend
uv sync --dev
uv run python app.py
```

### Import errors
```bash
cd backend
export PYTHONPATH=/Users/scott/Documents/Code/sample-api/backend:$PYTHONPATH
uv run python app.py
```

### Frontend can't connect to API
- Check backend is running on port 8000
- Verify CORS_ORIGINS includes your frontend URL
- Check browser console for errors

### Docker issues
```bash
# Rebuild containers
docker-compose down
docker-compose up --build
```

## 💡 Tips for Interview Success

1. **Use AI Tools Effectively**
   - Generate boilerplate code quickly
   - Ask for code reviews and improvements
   - Get help with error messages
   - Generate test cases

2. **Communicate Clearly**
   - Explain your approach before coding
   - Discuss trade-offs
   - Ask for clarification when needed
   - Show your thought process

3. **Demonstrate Best Practices**
   - Write tests (even simple ones)
   - Use type hints
   - Follow existing code patterns
   - Add error handling

4. **Time Management**
   - 5-10 min: Understand dataset and requirements
   - 30-35 min: Implement solution
   - 5-10 min: Test and refine
   - 5 min: Demo and discuss

## 📝 Notes

- All environment variables are optional (defaults provided)
- No database setup required (can work with CSV/JSON files)
- Sample datasets in `backend/data/` can be used for testing
- API documentation is auto-generated at http://localhost:8000/docs
- Frontend is optional - you can focus on backend API if needed

---

**Status**: ✅ **READY FOR INTERVIEW**

The repository has:
- ✅ Working backend API (FastAPI)
- ✅ Data processing utilities (pandas, CSV, JSON)
- ✅ Testing framework
- ✅ Clean architecture patterns
- ✅ Docker setup (optional)
- ✅ Documentation

You're all set! Good luck with the interview! 🚀

