<!-- Use this file to provide workspace-specific custom instructions to Copilot. For more details, visit https://code.visualstudio.com/docs/copilot/copilot-customization#_use-a-githubcopilotinstructionsmd-file -->

# Sample API Project - Copilot Instructions

This is an educational Python API project designed to demonstrate key API concepts to junior engineers. The project emphasizes:

## Project Structure
- **Business Logic**: Separated from API implementation in `src/math_operations.py`
- **API Layer**: Flask-based REST API with GET and POST endpoints
- **CLI Access**: Command-line interface showing business logic can be used outside the API
- **Testing**: Unit tests for business logic functions

## Development Guidelines
- Keep business logic pure and testable
- Maintain clear separation between API routes and core functionality
- Write comprehensive tests for all business logic
- Provide clear examples for cURL testing
- Document all endpoints and their usage

## Key Learning Points
- How APIs act as interfaces to business logic
- Separation of concerns in software architecture  
- Testing strategies for different application layers
- Multiple ways to access the same functionality (API vs CLI)