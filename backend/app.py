"""
FastAPI REST API for Mathematical Operations

This module provides a REST API interface to the mathematical operations
defined in the business logic module. It demonstrates how APIs can serve
as a thin layer over business logic, making functionality accessible
via HTTP endpoints.

FastAPI features demonstrated:
- Automatic API documentation (Swagger UI at /docs)
- Request/response data validation with Pydantic
- Type hints for better code clarity
- Automatic JSON serialization
- Built-in error handling

MCP Server:
- Auto-converted from FastAPI endpoints using FastMCP
- Available at /mcp endpoint for AI assistant integration
"""

import json
import os

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastmcp import FastMCP
from pydantic import BaseModel, Field
from starlette.middleware.base import BaseHTTPMiddleware

# Import implementation from shared loader
from impl_loader import (
    calculate_stats,
    factorial,
    fibonacci,
)
from impl_loader import implementation as _implementation
from impl_loader import (
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

# Configure CORS origins from environment variable
cors_origins = os.getenv(
    "CORS_ORIGINS",
    (
        "http://localhost:3000,http://localhost:5173,"
        "http://127.0.0.1:3000,http://127.0.0.1:5173"
    ),
).split(",")

# Add CORS middleware to allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=[origin.strip() for origin in cors_origins],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

# MCP Parameter Cleaning Middleware
# Converts string parameters to numbers for MCP tool calls
# This handles cases where MCP clients (like Cursor) pass string parameters


class MCPParameterCleaningMiddleware(BaseHTTPMiddleware):
    """Middleware to clean MCP tool call parameters by converting strings to numbers."""

    async def dispatch(self, request: Request, call_next):
        # Only process POST requests to MCP endpoints
        if request.method == "POST" and request.url.path.startswith("/mcp"):
            try:
                body = await request.body()
                if body:
                    data = json.loads(body)

                    # Check if this is a tools/call request
                    if data.get("method") == "tools/call" and "params" in data:
                        params = data["params"]
                        arguments = params.get("arguments", {})

                        # Clean numeric parameters (convert strings to numbers)
                        cleaned_args = {}
                        for param_name, param_value in arguments.items():
                            if isinstance(param_value, str):
                                # Try to convert to number
                                try:
                                    # Try int first, then float
                                    if "." in param_value or "e" in param_value.lower():
                                        cleaned_args[param_name] = float(param_value)
                                    else:
                                        cleaned_args[param_name] = int(param_value)
                                except (ValueError, TypeError):
                                    # If conversion fails, keep original value
                                    cleaned_args[param_name] = param_value
                            else:
                                cleaned_args[param_name] = param_value

                        # Update the request data
                        data["params"]["arguments"] = cleaned_args

                        # Create a new request with cleaned body
                        async def receive():
                            return {
                                "type": "http.request",
                                "body": json.dumps(data).encode(),
                            }

                        # Replace the request's receive function
                        request._receive = receive

            except (json.JSONDecodeError, KeyError, AttributeError):
                # If parsing fails, continue with original request
                pass

        response = await call_next(request)
        return response


# Add MCP parameter cleaning middleware
app.add_middleware(MCPParameterCleaningMiddleware)


# Pydantic models for POST request validation
class PowerRequest(BaseModel):
    """Request model for power calculation."""

    base: int = Field(..., description="The base number")
    exponent: int = Field(..., description="The exponent")


class StatsRequest(BaseModel):
    """Request model for statistics calculation."""

    numbers: list[int] = Field(
        ..., description="List of numbers to calculate statistics for", min_length=1
    )


# Pydantic models for response validation
class HealthResponse(BaseModel):
    """Response model for health check."""

    status: str = Field(..., description="Health status of the service")
    service: str = Field(..., description="Service name")


class APIInfoResponse(BaseModel):
    """Response model for API information."""

    message: str = Field(..., description="Welcome message")
    version: str = Field(..., description="API version")
    docs_url: str = Field(..., description="URL for interactive documentation")
    endpoints: dict = Field(..., description="Available API endpoints")


class MathOperationResponse(BaseModel):
    """Base response model for mathematical operations."""

    operation: str = Field(..., description="The operation that was performed")
    success: bool = Field(default=True, description="Whether the operation succeeded")


class SquareResponse(MathOperationResponse):
    """Response model for square operation."""

    input: int = Field(..., description="The input number")
    result: int = Field(..., description="The squared result")


class PowerResponse(MathOperationResponse):
    """Response model for power operation."""

    base: int = Field(..., description="The base number")
    exponent: int = Field(..., description="The exponent")
    result: int = Field(..., description="The power result")


class FactorialResponse(MathOperationResponse):
    """Response model for factorial operation."""

    input: int = Field(..., description="The input number")
    result: int = Field(..., description="The factorial result")


class FibonacciResponse(MathOperationResponse):
    """Response model for fibonacci operation."""

    count: int = Field(..., description="Number of Fibonacci numbers requested")
    sequence: list[int] = Field(..., description="The Fibonacci sequence")


class PrimeResponse(MathOperationResponse):
    """Response model for prime check operation."""

    input: int = Field(..., description="The input number to check")
    is_prime: bool = Field(..., description="Whether the number is prime")


class StatisticsData(BaseModel):
    """Model for statistical calculations."""

    count: int = Field(..., description="Number of values")
    mean: float = Field(..., description="Arithmetic mean")
    median: int = Field(..., description="Median value")
    min: int = Field(..., description="Minimum value")
    max: int = Field(..., description="Maximum value")
    sum: int = Field(..., description="Sum of all values")


class StatsResponse(MathOperationResponse):
    """Response model for statistics operation."""

    input_numbers: list[int] = Field(..., description="The input numbers")
    statistics: StatisticsData = Field(..., description="Calculated statistics")


class ErrorResponse(BaseModel):
    """Response model for errors."""

    error: str = Field(..., description="Error type")
    message: str = Field(..., description="Detailed error message")
    success: bool = Field(default=False, description="Always false for errors")


@app.get("/", response_model=APIInfoResponse)
async def root() -> APIInfoResponse:
    """
    API root endpoint providing information about available endpoints.
    """
    return APIInfoResponse(
        message="Mathematical Operations API",
        version="1.0.0",
        docs_url="/docs",
        endpoints={
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
    )


@app.get("/health", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    """
    Health check endpoint to verify API is running.
    """
    return HealthResponse(
        status="healthy",
        service=f"math-operations-api ({_implementation})",
    )


@app.get("/square/{number}", response_model=SquareResponse)
async def api_square(number: int) -> SquareResponse:
    """
    Calculate the square of a number.

    - **number**: The number to square (integer)
    """
    try:
        result = square(number)
        return SquareResponse(operation="square", input=number, result=result)
    except (ValueError, TypeError) as e:
        raise HTTPException(status_code=400, detail=f"Invalid input: {str(e)}")


@app.get("/factorial/{number}", response_model=FactorialResponse)
async def api_factorial(number: int) -> FactorialResponse:
    """
    Calculate the factorial of a non-negative integer.

    - **number**: The integer to calculate factorial for (must be >= 0)
    """
    try:
        result = factorial(number)
        return FactorialResponse(operation="factorial", input=number, result=result)
    except (ValueError, TypeError) as e:
        raise HTTPException(status_code=400, detail=f"Invalid input: {str(e)}")


@app.get("/fibonacci/{count}", response_model=FibonacciResponse)
async def api_fibonacci(count: int) -> FibonacciResponse:
    """
    Generate the first N numbers in the Fibonacci sequence.

    - **count**: Number of Fibonacci numbers to generate (must be > 0)
    """
    try:
        result = fibonacci(count)
        return FibonacciResponse(operation="fibonacci", count=count, sequence=result)
    except (ValueError, TypeError) as e:
        raise HTTPException(status_code=400, detail=f"Invalid input: {str(e)}")


@app.get("/prime/{number}", response_model=PrimeResponse)
async def api_is_prime(number: int) -> PrimeResponse:
    """
    Check if a number is prime.

    - **number**: The integer to check for primality (must be >= 2)
    """
    try:
        result = is_prime(number)
        return PrimeResponse(operation="is_prime", input=number, is_prime=result)
    except (ValueError, TypeError) as e:
        raise HTTPException(status_code=400, detail=f"Invalid input: {str(e)}")


@app.post("/power", response_model=PowerResponse)
async def api_power(request: PowerRequest) -> PowerResponse:
    """
    Calculate base raised to the power of exponent.

    Request body should contain:
    - **base**: The base number
    - **exponent**: The exponent
    """
    try:
        # Data cleaning: Convert strings to numbers if needed (for MCP compatibility)
        base = request.base
        exponent = request.exponent

        if isinstance(base, str):
            try:
                base = int(base)
            except ValueError:
                base = float(base)

        if isinstance(exponent, str):
            try:
                exponent = int(exponent)
            except ValueError:
                exponent = float(exponent)

        result = power(base, exponent)
        return PowerResponse(
            operation="power",
            base=base,
            exponent=exponent,
            result=result,
        )
    except (ValueError, TypeError) as e:
        raise HTTPException(status_code=400, detail=f"Invalid input: {str(e)}")


@app.post("/stats", response_model=StatsResponse)
async def api_calculate_stats(request: StatsRequest) -> StatsResponse:
    """
    Calculate basic statistics for a list of numbers.

    Request body should contain:
    - **numbers**: Array of numbers to analyze (must not be empty)

    Returns count, mean, median, min, max, and sum.
    """
    try:
        result = calculate_stats(request.numbers)
        return StatsResponse(
            operation="calculate_stats",
            input_numbers=request.numbers,
            statistics=StatisticsData(**result),
        )
    except (ValueError, TypeError) as e:
        raise HTTPException(status_code=400, detail=f"Invalid input: {str(e)}")


# Custom exception handler for better error responses
@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    """Handle unexpected exceptions gracefully."""
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal server error",
            "message": "An unexpected error occurred",
            "success": False,
        },
    )


# MCP Server: Auto-convert FastAPI endpoints to MCP tools
# This enables AI assistants to use the API via Model Context Protocol
# One-line conversion: FastMCP automatically converts all endpoints to MCP tools
mcp = FastMCP.from_fastapi(app=app, name="Mathematical Operations MCP")


# Mount MCP server into FastAPI app at /mcp endpoint
# This allows both REST API and MCP to be served from the same server
# The MCPParameterCleaningMiddleware (added above) will handle parameter conversion
# Note: For production, consider passing mcp_app.lifespan to FastAPI app creation
# if you need proper session management. Current setup works for basic use cases.
mcp_app = mcp.http_app(path="/mcp")
app.mount("/mcp", mcp_app)


if __name__ == "__main__":
    import uvicorn

    print("Starting Mathematical Operations API with FastAPI...")
    print(f"Using {_implementation} implementation")
    print("\nAvailable endpoints:")
    print("  GET  /                    - API information")
    print("  GET  /health              - Health check")
    print("  GET  /docs               - Interactive API documentation (Swagger UI)")
    print("  GET  /redoc              - Alternative API documentation (ReDoc)")
    print("  GET  /square/{number}     - Calculate square")
    print("  GET  /factorial/{number}  - Calculate factorial")
    print("  GET  /fibonacci/{count}   - Generate Fibonacci sequence")
    print("  GET  /prime/{number}      - Check if prime")
    print("  POST /power               - Calculate power (JSON body)")
    print("  POST /stats               - Calculate statistics (JSON body)")
    print("\nMCP Server:")
    print("  POST /mcp                - MCP endpoint for AI assistants")
    print("\nAPI running on http://localhost:8000")
    print("Interactive docs available at http://localhost:8000/docs")
    print("MCP server available at http://localhost:8000/mcp")
    print("Press Ctrl+C to stop the server")

    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=8000,
        reload=True,  # Auto-reload on code changes
        log_level="info",
    )
