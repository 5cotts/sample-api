# Mathematical Operations Frontend

A React-based web interface for the Mathematical Operations API, demonstrating full-stack development concepts.

## 🚀 Features

- **Interactive UI**: Clean, responsive web interface for all mathematical operations
- **Real-time API Communication**: Direct integration with FastAPI backend
- **Error Handling**: Comprehensive error handling and user feedback
- **Educational Focus**: Code structure teaches React and API integration concepts

## 🛠️ Technology Stack

- **React 18**: Modern React with functional components and hooks
- **Vite**: Fast build tool and development server
- **Axios**: HTTP client for API communication
- **Vanilla CSS**: Custom styling without external UI libraries (educational focus)
- **ESLint**: Code linting for consistency

## 📋 Prerequisites

- Node.js 18+ 
- npm or yarn
- Backend API running on `localhost:8000`

## 🚀 Quick Start

### 1. Install Dependencies

```bash
cd frontend
npm install
```

### 2. Start Development Server

```bash
npm run dev
```

The frontend will be available at `http://localhost:3000`

### 3. Ensure Backend is Running

Make sure the FastAPI backend is running:

```bash
cd ../backend
uv run python app.py
```

## 📱 Available Operations

The frontend provides interactive interfaces for:

- **Square Calculator**: Calculate n²
- **Power Calculator**: Calculate base^exponent  
- **Factorial Calculator**: Calculate n!
- **Fibonacci Generator**: Generate Fibonacci sequences
- **Prime Checker**: Check if numbers are prime
- **Statistics Calculator**: Calculate mean, median, min, max for datasets

## 🏗️ Project Structure

```
frontend/
├── public/
│   ├── calculator.svg          # App icon
│   └── index.html             # HTML template
├── src/
│   ├── components/            # React components
│   │   ├── SquareCalculator.jsx
│   │   ├── PowerCalculator.jsx
│   │   ├── FactorialCalculator.jsx
│   │   ├── FibonacciGenerator.jsx
│   │   ├── PrimeChecker.jsx
│   │   └── StatisticsCalculator.jsx
│   ├── services/
│   │   └── api.js             # API service layer
│   ├── App.jsx                # Main application component
│   ├── main.jsx              # React entry point
│   └── index.css             # Global styles
├── .env                       # Environment variables
├── package.json              # Dependencies and scripts
└── vite.config.js            # Vite configuration
```

## 🔧 Development Commands

```bash
# Start development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Run linting
npm run lint
```

## 🌐 API Integration

The frontend communicates with the backend API through:

- **Base URL**: `http://localhost:8000` (configurable via `.env`)
- **HTTP Client**: Axios with request/response interceptors
- **Error Handling**: Automatic error parsing and user-friendly messages
- **Proxy Configuration**: Vite proxy setup for development

### API Service Example

```javascript
// GET request
const result = await MathAPI.getSquare(5);

// POST request
const result = await MathAPI.calculatePower(2, 8);
```

## 🎨 Styling Approach

- **Vanilla CSS**: No external UI frameworks for educational clarity
- **CSS Grid/Flexbox**: Modern layout techniques
- **Custom Properties**: CSS variables for theming
- **Responsive Design**: Mobile-friendly responsive layout
- **Accessibility**: ARIA labels and semantic HTML

## 🧪 Educational Value

This frontend demonstrates:

1. **Component Architecture**: Reusable React components with clear separation of concerns
2. **State Management**: React hooks for local state management
3. **API Integration**: RESTful API communication patterns
4. **Error Handling**: Comprehensive error handling strategies
5. **Form Validation**: Client-side input validation
6. **Responsive Design**: Mobile-first responsive web design
7. **Modern JavaScript**: ES6+ features and async/await patterns

## 🔄 Backend Communication

The frontend makes HTTP requests to these backend endpoints:

- `GET /square/{number}` - Calculate square
- `GET /factorial/{number}` - Calculate factorial  
- `GET /fibonacci/{count}` - Generate Fibonacci sequence
- `GET /prime/{number}` - Check if prime
- `POST /power` - Calculate power
- `POST /stats` - Calculate statistics

## 🚀 Production Build

```bash
# Build optimized production bundle
npm run build

# The build output will be in the `dist/` directory
# Serve with any static file server
```

## 🤝 Contributing

This is an educational project. Key areas for learning:

- Adding new mathematical operations
- Implementing additional React features (routing, context)
- Adding a UI component library
- Implementing testing (Jest, React Testing Library)
- Adding TypeScript for type safety

---

*Part of the Educational Full-Stack API Project demonstrating React frontend + FastAPI backend architecture.*