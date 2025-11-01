# Frontend Agent Instructions: React Application

## Overview

This directory contains a React frontend application that consumes the FastAPI backend. It demonstrates how to build a web interface that communicates with a REST API.

**Key Principle:** Frontend components call API service functions, never implement business logic directly.

## Project Structure

```
frontend/
├── AGENTS.md              # This file
├── src/
│   ├── App.jsx            # Main application component
│   ├── main.jsx           # Entry point
│   ├── index.css          # Global styles
│   ├── components/        # React components
│   │   └── AGENTS.md      # Component-specific patterns
│   └── services/
│       └── api.js         # API service layer
├── public/                # Static assets
├── package.json           # Dependencies
└── vite.config.js         # Vite configuration
```

## Architecture

1. **API Service Layer** (`src/services/api.js`)
   - Centralized API client using axios
   - Methods for each backend endpoint
   - Error handling and interceptors

2. **Components** (`src/components/`)
   - Each component handles one operation
   - Calls API service methods
   - Manages local state (form inputs, results, loading, errors)

3. **App Component** (`src/App.jsx`)
   - Coordinates all components
   - API health checking
   - Error state handling

## Key Patterns

### API Service (`src/services/api.js`)

```javascript
import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Response interceptor for error handling
api.interceptors.response.use(
  (response) => response,
  (error) => {
    console.error('API Error:', error);
    return Promise.reject(error);
  }
);

export class MathAPI {
  static async getSquare(number) {
    try {
      const response = await api.get(`/square/${number}`);
      return response.data;
    } catch (error) {
      throw new Error(error.response?.data?.detail || 'Failed to calculate square');
    }
  }
  
  // Add methods for other endpoints...
}

export default MathAPI;
```

**Pattern:**
- Use axios for HTTP requests
- Configure base URL from environment variable
- Add interceptors for error handling
- Static methods for each API endpoint
- Transform errors into user-friendly messages

### Component Pattern

See `src/components/AGENTS.md` for detailed component patterns.

**Key elements:**
- useState for form inputs, results, loading, errors
- handleSubmit async function
- Form validation
- API service calls
- Error handling
- Loading states

### App Component Pattern

```javascript
function App() {
  const [apiStatus, setApiStatus] = useState('checking');
  const [apiInfo, setApiInfo] = useState(null);

  useEffect(() => {
    checkApiStatus();
  }, []);

  const checkApiStatus = async () => {
    try {
      const [healthResponse, infoResponse] = await Promise.all([
        MathAPI.getHealth(),
        MathAPI.getApiInfo()
      ]);
      
      if (healthResponse.status === 'healthy') {
        setApiStatus('connected');
        setApiInfo(infoResponse);
      }
    } catch (error) {
      setApiStatus('error');
    }
  };

  // Render components conditionally based on apiStatus
}
```

## Environment Variables

Create `.env` file:
```
VITE_API_URL=http://localhost:8000
```

## Development

```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build
```

## API Integration

When backend endpoints change:

1. Update `src/services/api.js` with new methods
2. Update component props and state if needed
3. Update error messages to match backend responses

## Styling

- Global styles in `src/index.css`
- Component-specific styles use CSS classes
- Responsive design with CSS Grid
- Consistent card-based layout

## Error Handling

**API Errors:**
- Catch errors in API service methods
- Transform to user-friendly messages
- Display in component error state

**Component Errors:**
- Validate inputs before API calls
- Show inline error messages
- Reset errors on retry

## Component Guidelines

Follow patterns in `src/components/AGENTS.md`:
- Consistent state management
- Form validation patterns
- Loading state handling
- Result display formatting

