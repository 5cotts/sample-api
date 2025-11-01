# Agent Instructions: Educational API Project Template

## Overview

This project demonstrates a complete full-stack educational API with:
- **Backend**: Python FastAPI with business logic separation
- **Frontend**: React application consuming the API
- **Key Principle**: Business logic is independent of interface (API, CLI, or Web)

**Note:** For instructions on running and using this application (not as a template), see [README.md](README.md).

## Project Structure

```
project/
├── AGENTS.md              # This file - global instructions
├── backend/
│   └── AGENTS.md          # Backend-specific template instructions
├── frontend/
│   ├── AGENTS.md          # Frontend-specific instructions
│   └── src/
│       └── components/
│           └── AGENTS.md  # Component patterns and guidelines
└── scripts/
    └── validate_template.py  # Template validation script
```

## Quick Start

1. **Backend Setup**: See `backend/AGENTS.md` for complete Python API template
2. **Frontend Setup**: See `frontend/AGENTS.md` for React patterns
3. **Component Patterns**: See `frontend/src/components/AGENTS.md` for component guidelines

## Key Principles

1. **Separation of Concerns**: Business logic in `backend/src/`, API in `backend/app.py`, CLI in `backend/cli.py`
2. **Pure Functions**: Business logic should have no side effects
3. **Thin API Layer**: Endpoints call business logic, never implement it
4. **Multiple Interfaces**: Same business logic accessible via API, CLI, and Web UI
5. **Comprehensive Testing**: Unit tests for business logic, integration tests for API/CLI

## Directory-Specific Instructions

- **[Backend Instructions](backend/AGENTS.md)** - Complete Python API template with FastAPI
- **[Frontend Instructions](frontend/AGENTS.md)** - React application patterns
- **[Component Instructions](frontend/src/components/AGENTS.md)** - React component guidelines

## Validation

After creating a project from this template:

```bash
python scripts/validate_template.py backend/
```

## Customization

When adapting this template for different domains:

1. **Backend**: See customization section in `backend/AGENTS.md`
2. **Frontend**: Update API service calls in `frontend/src/services/api.js`
3. **Components**: Follow patterns in `frontend/src/components/AGENTS.md`

The key is maintaining the infrastructure and patterns while replacing domain logic.

## Application Documentation

For detailed usage instructions, API examples, and running the application:
- See [README.md](README.md) for complete application documentation

