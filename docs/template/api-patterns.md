# FastAPI API Patterns

## Overview

Create `app.py` with a FastAPI application that provides a REST API interface to the business logic functions. The API should be a thin layer that calls business logic functions.

**Key Principle:** API endpoints should never implement business logic directly. They should only call functions from the business logic module.

## Complete Template Code

```python
"""
FastAPI REST API for Mathematical Operations

This module provides a REST API interface to the mathematical operations
defined in the business logic module. It demonstrates how APIs can serve
as a thin layer over business logic, making functionality accessible
via HTTP endpoints.

NOTE: Update the API descriptions and endpoint names to match your domain
while keeping the same structure and patterns.
"""

from typing import List, Union
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

from src.math_operations import (
    calculate_stats,
    factorial,
    fibonacci,
    is_prime,
    power,
    square,
)

# Create FastAPI app with metadata
app = FastAPI(
    title="Mathematical Operations API",
    description="Educational Python API demonstrating business logic separation",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Optional: CORS middleware (only needed if serving a frontend)
# from fastapi.middleware.cors import CORSMiddleware
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:3000", "http://localhost:5173"],
#     allow_credentials=True,
#     allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
#     allow_headers=["*"],
# )

# Pydantic request models
class PowerRequest(BaseModel):
    """Request model for power calculation."""
    base: Union[int, float] = Field(..., description="The base number")
    exponent: Union[int, float] = Field(..., description="The exponent")

class StatsRequest(BaseModel):
    """Request model for statistics calculation."""
    numbers: List[Union[int, float]] = Field(
        ..., description="List of numbers to calculate statistics for", min_length=1
    )

# Pydantic response models  
class MathOperationResponse(BaseModel):
    """Base response model for mathematical operations."""
    operation: str = Field(..., description="The operation that was performed")
    success: bool = Field(default=True, description="Whether the operation succeeded")

class SquareResponse(MathOperationResponse):
    """Response model for square operation."""
    input: Union[int, float] = Field(..., description="The input number")
    result: Union[int, float] = Field(..., description="The squared result")

class PowerResponse(MathOperationResponse):
    """Response model for power operation."""
    base: Union[int, float] = Field(..., description="The base number")
    exponent: Union[int, float] = Field(..., description="The exponent")
    result: Union[int, float] = Field(..., description="The power result")

class FactorialResponse(MathOperationResponse):
    """Response model for factorial operation."""
    input: int = Field(..., description="The input number")
    result: int = Field(..., description="The factorial result")

class FibonacciResponse(MathOperationResponse):
    """Response model for fibonacci operation."""
    count: int = Field(..., description="Number of Fibonacci numbers requested")
    sequence: List[int] = Field(..., description="The Fibonacci sequence")

class PrimeResponse(MathOperationResponse):
    """Response model for prime check operation."""
    input: int = Field(..., description="The input number to check")
    is_prime: bool = Field(..., description="Whether the number is prime")

class StatisticsData(BaseModel):
    """Model for statistical calculations."""
    count: int = Field(..., description="Number of values")
    mean: float = Field(..., description="Arithmetic mean")
    median: Union[int, float] = Field(..., description="Median value")
    min: Union[int, float] = Field(..., description="Minimum value")
    max: Union[int, float] = Field(..., description="Maximum value")
    sum: Union[int, float] = Field(..., description="Sum of all values")

class StatsResponse(MathOperationResponse):
    """Response model for statistics operation."""
    input_numbers: List[Union[int, float]] = Field(..., description="The input numbers")
    statistics: StatisticsData = Field(..., description="Calculated statistics")

# API endpoints
@app.get("/")
async def root():
    """API root endpoint providing information about available endpoints."""
    return {
        "message": "Mathematical Operations API",
        "version": "1.0.0",
        "docs_url": "/docs",
        "endpoints": {
            "GET /": "API information",
            "GET /health": "Health check",
            "GET /docs": "Interactive API documentation (Swagger UI)",
            "GET /redoc": "Alternative API documentation (ReDoc)",
            "GET /square/{number}": "Calculate square of a number",
            "GET /factorial/{number}": "Calculate factorial of a number",
            "GET /fibonacci/{count}": "Generate Fibonacci sequence",
            "GET /prime/{number}": "Check if number is prime",
            "POST /power": "Calculate base^exponent",
            "POST /stats": "Calculate statistics for a list of numbers",
        },
    }

@app.get("/health")
async def health_check():
    """Health check endpoint to verify API is running."""
    return {"status": "healthy", "service": "math-operations-api"}

@app.get("/square/{number}", response_model=SquareResponse)
async def api_square(number: Union[int, float]) -> SquareResponse:
    """Calculate the square of a number."""
    try:
        result = square(number)
        return SquareResponse(operation="square", input=number, result=result)
    except (ValueError, TypeError) as e:
        raise HTTPException(status_code=400, detail=f"Invalid input: {str(e)}")

@app.get("/factorial/{number}", response_model=FactorialResponse)
async def api_factorial(number: int) -> FactorialResponse:
    """Calculate the factorial of a non-negative integer."""
    try:
        result = factorial(number)
        return FactorialResponse(operation="factorial", input=number, result=result)
    except (ValueError, TypeError) as e:
        raise HTTPException(status_code=400, detail=f"Invalid input: {str(e)}")

@app.get("/fibonacci/{count}", response_model=FibonacciResponse)
async def api_fibonacci(count: int) -> FibonacciResponse:
    """Generate the first N numbers in the Fibonacci sequence."""
    try:
        result = fibonacci(count)
        return FibonacciResponse(operation="fibonacci", count=count, sequence=result)
    except (ValueError, TypeError) as e:
        raise HTTPException(status_code=400, detail=f"Invalid input: {str(e)}")

@app.get("/prime/{number}", response_model=PrimeResponse)
async def api_is_prime(number: int) -> PrimeResponse:
    """Check if a number is prime."""
    try:
        result = is_prime(number)
        return PrimeResponse(operation="is_prime", input=number, is_prime=result)
    except (ValueError, TypeError) as e:
        raise HTTPException(status_code=400, detail=f"Invalid input: {str(e)}")

@app.post("/power", response_model=PowerResponse)
async def api_power(request: PowerRequest) -> PowerResponse:
    """Calculate base raised to the power of exponent."""
    try:
        result = power(request.base, request.exponent)
        return PowerResponse(
            operation="power",
            base=request.base,
            exponent=request.exponent,
            result=result,
        )
    except (ValueError, TypeError) as e:
        raise HTTPException(status_code=400, detail=f"Invalid input: {str(e)}")

@app.post("/stats", response_model=StatsResponse)
async def api_calculate_stats(request: StatsRequest) -> StatsResponse:
    """Calculate basic statistics for a list of numbers."""
    try:
        result = calculate_stats(request.numbers)
        return StatsResponse(
            operation="calculate_stats",
            input_numbers=request.numbers,
            statistics=StatisticsData(**result),
        )
    except (ValueError, TypeError) as e:
        raise HTTPException(status_code=400, detail=f"Invalid input: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True, log_level="info")
```

**Note:** For a working example, reference `backend/app.py` in the actual codebase.

## Code Structure Breakdown

The template above includes:
1. **FastAPI App Initialization** - App metadata and optional CORS middleware
2. **Pydantic Request Models** - For POST endpoints (PowerRequest, StatsRequest)
3. **Pydantic Response Models** - All extending MathOperationResponse base class
4. **API Endpoints** - Thin layer that calls business logic functions

## Required Endpoints

- `GET /` - API information endpoint
- `GET /health` - Health check endpoint
- `GET /square/{number}` - Square calculation
- `GET /factorial/{number}` - Factorial calculation
- `GET /fibonacci/{count}` - Fibonacci sequence generation
- `GET /prime/{number}` - Prime number check
- `POST /power` - Power calculation (JSON body)
- `POST /stats` - Statistics calculation (JSON body)

## Error Handling

Always wrap business logic calls in try/except blocks:

```python
try:
    result = business_logic_function(input)
    return ResponseModel(...)
except (ValueError, TypeError) as e:
    raise HTTPException(status_code=400, detail=f"Invalid input: {str(e)}")
```

## Updating for Your Domain

- Modify endpoint paths to match domain terminology
- Update Pydantic model names and field descriptions
- Keep the same response structure patterns
- Update API documentation strings
- Maintain the thin layer principle (no business logic in endpoints)

