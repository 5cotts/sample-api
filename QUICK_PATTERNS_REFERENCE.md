# Quick Patterns Reference - Add in 5-10 Minutes

These patterns can be quickly added if needed during the interview. All examples follow your existing codebase patterns.

---

## 1. PUT Endpoint (Update Operation)

```python
# In app.py
from fastapi import Query

class UpdateItemRequest(BaseModel):
    name: str = Field(..., description="Updated name")
    value: Union[int, float] = Field(None, description="Updated value")

@app.put("/items/{item_id}", response_model=ItemResponse)
async def update_item(item_id: int, request: UpdateItemRequest):
    """
    Update an item by ID.
    
    - **item_id**: ID of item to update
    - **request**: Updated item data
    """
    try:
        # Call business logic function
        result = update_item_logic(item_id, request.name, request.value)
        return ItemResponse(id=item_id, name=result.name, value=result.value)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
```

---

## 2. DELETE Endpoint

```python
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    """
    Delete an item by ID.
    
    - **item_id**: ID of item to delete
    """
    try:
        delete_item_logic(item_id)
        return {"message": f"Item {item_id} deleted successfully", "id": item_id}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
```

---

## 3. Query Parameters (Filtering/Pagination)

```python
from fastapi import Query
from typing import Optional

@app.get("/items")
async def list_items(
    page: int = Query(1, ge=1, description="Page number"),
    limit: int = Query(10, ge=1, le=100, description="Items per page"),
    search: Optional[str] = Query(None, description="Search term"),
    min_value: Optional[float] = Query(None, description="Minimum value filter")
):
    """
    List items with pagination and filtering.
    
    - **page**: Page number (default: 1)
    - **limit**: Items per page (default: 10, max: 100)
    - **search**: Optional search term
    - **min_value**: Optional minimum value filter
    """
    skip = (page - 1) * limit
    
    # Load data
    df = load_csv("backend/data/items.csv")
    
    # Apply filters
    if search:
        df = filter_dataframe(df, "name", "contains", search)
    if min_value:
        df = filter_dataframe(df, "value", ">=", min_value)
    
    # Paginate
    total = len(df)
    items = df.iloc[skip:skip+limit].to_dict('records')
    
    return {
        "items": items,
        "total": total,
        "page": page,
        "limit": limit,
        "has_next": skip + limit < total
    }
```

---

## 4. Basic SQLite Database (Simple Pattern)

```python
# Add to pyproject.toml dependencies:
# "sqlite3" (built-in) or consider "sqlalchemy>=2.0.0"

# Create: backend/src/database.py
import sqlite3
from pathlib import Path
from typing import List, Dict, Any, Optional

DB_PATH = Path("backend/data/app.db")

def init_db():
    """Initialize database with schema."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            value REAL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def get_items(limit: int = 10, offset: int = 0) -> List[Dict[str, Any]]:
    """Get items from database."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items LIMIT ? OFFSET ?", (limit, offset))
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def create_item(name: str, value: Optional[float] = None) -> Dict[str, Any]:
    """Create new item."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO items (name, value) VALUES (?, ?)",
        (name, value)
    )
    item_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return {"id": item_id, "name": name, "value": value}

# In app.py
from src.database import init_db, get_items, create_item

# Initialize on startup
@app.on_event("startup")
async def startup_event():
    init_db()

@app.get("/db/items")
async def list_db_items(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100)
):
    offset = (page - 1) * limit
    items = get_items(limit=limit, offset=offset)
    return {"items": items, "page": page, "limit": limit}
```

---

## 5. File Upload (Dataset Ingestion)

```python
from fastapi import UploadFile, File
from src.data_parsing import load_csv, dataframe_summary
import shutil
from pathlib import Path

UPLOAD_DIR = Path("backend/data/uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

@app.post("/upload/dataset")
async def upload_dataset(file: UploadFile = File(...)):
    """
    Upload a CSV dataset file.
    
    - **file**: CSV file to upload and analyze
    """
    # Validate file type
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="Only CSV files allowed")
    
    # Save file
    file_path = UPLOAD_DIR / file.filename
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # Analyze dataset
    df = load_csv(file_path)
    summary = dataframe_summary(df)
    
    return {
        "filename": file.filename,
        "message": "File uploaded successfully",
        "summary": summary
    }
```

---

## 6. Search Endpoint (Using Existing Filtering)

```python
@app.get("/dataset/search")
async def search_dataset(
    column: str = Query(..., description="Column to search"),
    condition: str = Query("==", description="Condition: ==, !=, >, <, >=, <=, contains"),
    value: str = Query(..., description="Value to search for"),
    file: str = Query("sample_data.csv", description="Dataset file name")
):
    """
    Search and filter dataset.
    
    - **column**: Column name to filter on
    - **condition**: Comparison operator
    - **value**: Value to compare
    - **file**: Dataset file name (default: sample_data.csv)
    """
    from src.data_parsing import load_csv, filter_dataframe
    
    try:
        df = load_csv(f"backend/data/{file}")
        filtered = filter_dataframe(df, column, condition, value)
        return {
            "matches": len(filtered),
            "results": filtered.to_dict('records')
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
```

---

## Quick Copy-Paste: Minimal CRUD Example

If you need to show full CRUD quickly, here's a minimal example:

```python
# Minimal Item CRUD
@app.get("/items/{item_id}")
async def get_item(item_id: int):
    return {"id": item_id, "name": "Item", "value": 100}

@app.post("/items")
async def create_item(request: CreateItemRequest):
    new_id = 1  # In real app, would generate ID
    return {"id": new_id, **request.dict()}

@app.put("/items/{item_id}")
async def update_item(item_id: int, request: UpdateItemRequest):
    return {"id": item_id, **request.dict(), "updated": True}

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    return {"message": f"Item {item_id} deleted", "id": item_id}
```

---

## When to Use Each Pattern

**For dataset-focused interviews:**
- ✅ Query parameters (#3) - Very common
- ✅ Search endpoint (#6) - Uses your existing data_parsing
- ✅ File upload (#5) - If they give you a file to process

**For general API interviews:**
- ✅ PUT endpoint (#1) - CRUD completeness
- ✅ DELETE endpoint (#2) - CRUD completeness
- ✅ Query parameters (#3) - Standard feature

**If database is required:**
- ✅ Basic SQLite (#4) - Simple but effective

---

**Time to implement:**
- Patterns #1-2 (PUT/DELETE): ~5 minutes
- Pattern #3 (Query params): ~10 minutes
- Pattern #4 (SQLite): ~15 minutes
- Pattern #5 (File upload): ~10 minutes
- Pattern #6 (Search): ~5 minutes

**Total time to add all: ~45 minutes** (but you won't need all of them!)

