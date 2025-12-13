import { useState, useEffect } from 'react';
import SquareCalculator from './components/SquareCalculator';
import PowerCalculator from './components/PowerCalculator';
import FactorialCalculator from './components/FactorialCalculator';
import FibonacciGenerator from './components/FibonacciGenerator';
import PrimeChecker from './components/PrimeChecker';
import StatisticsCalculator from './components/StatisticsCalculator';
import MathAPI from './services/api';

// Style constants - defined outside component to avoid recreation on every render
const statusContainerStyle = {
  marginTop: '1rem',
  display: 'flex',
  flexDirection: 'column',
  gap: '0.5rem',
  alignItems: 'center'
};

const implementationBadgeStyle = {
  marginTop: '0.5rem',
  padding: '0.4rem 0.8rem',
  borderRadius: '20px',
  background: 'rgba(255, 255, 255, 0.2)',
  backdropFilter: 'blur(10px)',
  fontSize: '0.9rem',
  fontWeight: '500',
  display: 'inline-flex',
  alignItems: 'center',
  gap: '0.5rem'
};

const getImplementationTextStyle = (impl) => ({
  textTransform: 'uppercase',
  fontWeight: '600',
  color: impl === 'object-oriented' ? '#ffd700' : '#90ee90',
  letterSpacing: '0.5px'
});

function App() {
  const [apiStatus, setApiStatus] = useState('checking');
  const [apiInfo, setApiInfo] = useState(null);
  const [implementation, setImplementation] = useState(null);

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
        
        // Extract implementation type from service field
        // Format: "math-operations-api (functional)" or "math-operations-api (object-oriented)"
        const service = healthResponse.service || '';
        const implMatch = service.match(/\(([^)]+)\)/);
        if (implMatch) {
          setImplementation(implMatch[1]);
        }
      } else {
        setApiStatus('error');
      }
    } catch (error) {
      console.error('API connection failed:', error);
      setApiStatus('error');
    }
  };

  return (
    <>
      <header className="header">
        <div className="container">
          <h1>Mathematical Operations API</h1>
          <p>Interactive web interface for mathematical calculations</p>
          
          <div style={statusContainerStyle}>
            <div>
              Status: 
              {apiStatus === 'checking' && (
                <span style={{ marginLeft: '0.5rem', color: '#ffd700' }}>
                  <div className="loading" style={{ display: 'inline-block', marginRight: '0.5rem' }}></div>
                  Connecting to API...
                </span>
              )}
              {apiStatus === 'connected' && (
                <span style={{ marginLeft: '0.5rem', color: '#90ee90' }}>
                  ✓ Connected to API v{apiInfo?.version}
                </span>
              )}
              {apiStatus === 'error' && (
                <span style={{ marginLeft: '0.5rem', color: '#ff6b6b' }}>
                  ✗ API Connection Failed
                </span>
              )}
            </div>
            {apiStatus === 'connected' && implementation && (
              <div style={implementationBadgeStyle}>
                <span>Implementation:</span>
                <span style={getImplementationTextStyle(implementation)}>
                  {implementation === 'object-oriented' ? '🏛️ OOP' : '⚡ Functional'}
                </span>
              </div>
            )}
          </div>
        </div>
      </header>

      <main className="container">
        {apiStatus === 'error' && (
          <div className="card" style={{ background: '#fed7d7', borderColor: '#feb2b2' }}>
            <h2>⚠️ API Connection Error</h2>
            <p>
              Cannot connect to the backend API. Please make sure the backend server is running at{' '}
              <code>http://localhost:8000</code>
            </p>
            <p>
              To start the backend server:
            </p>
            <div className="result-list" style={{ marginTop: '1rem' }}>
              cd backend<br/>
              uv run python app.py
            </div>
            <button 
              className="btn btn-primary" 
              onClick={checkApiStatus}
              style={{ marginTop: '1rem' }}
            >
              Retry Connection
            </button>
          </div>
        )}

        {apiStatus === 'connected' && (
          <>
            <div className="card">
              <h2>About This Application</h2>
              <p>
                This React frontend demonstrates how to build a web interface that communicates 
                with a REST API. Each operation below makes HTTP requests to the FastAPI backend 
                running on <code>localhost:8000</code>.
              </p>
              <p>
                <strong>Educational Focus:</strong> This project shows the separation between 
                frontend UI and backend business logic, with the same mathematical operations 
                accessible via web interface, REST API, and command-line interface.
              </p>
            </div>

            <div className="operations-grid">
              <SquareCalculator />
              <PowerCalculator />
              <FactorialCalculator />
              <FibonacciGenerator />
              <PrimeChecker />
              <StatisticsCalculator />
            </div>

            <div className="card">
              <h2>API Documentation</h2>
              <p>
                For detailed API documentation and to test endpoints directly, visit:
              </p>
              <ul style={{ marginTop: '1rem', paddingLeft: '2rem' }}>
                <li>
                  <a 
                    href="http://localhost:8000/docs" 
                    target="_blank" 
                    rel="noopener noreferrer"
                    style={{ color: '#667eea', textDecoration: 'none' }}
                  >
                    Interactive API Docs (Swagger UI) →
                  </a>
                </li>
                <li>
                  <a 
                    href="http://localhost:8000/redoc" 
                    target="_blank" 
                    rel="noopener noreferrer"
                    style={{ color: '#667eea', textDecoration: 'none' }}
                  >
                    Alternative API Docs (ReDoc) →
                  </a>
                </li>
              </ul>
            </div>
          </>
        )}
      </main>

      <footer style={{ 
        textAlign: 'center', 
        padding: '2rem', 
        color: '#718096',
        borderTop: '1px solid #e2e8f0',
        marginTop: '3rem'
      }}>
        <p>
          Educational Full-Stack Project • React Frontend + FastAPI Backend
        </p>
      </footer>
    </>
  );
}

export default App;