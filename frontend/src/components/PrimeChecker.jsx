import { useState } from 'react';
import MathAPI from '../services/api';

function PrimeChecker() {
  const [number, setNumber] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!number.trim()) {
      setError('Please enter a number');
      return;
    }

    const numValue = parseInt(number);
    if (isNaN(numValue) || numValue < 2 || !Number.isInteger(parseFloat(number))) {
      setError('Please enter an integer greater than or equal to 2');
      return;
    }

    setLoading(true);
    setError('');
    
    try {
      const response = await MathAPI.isPrime(numValue);
      setResult(response);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="card">
      <h2>Prime Number Checker</h2>
      <p>Check if a number is prime (only divisible by 1 and itself)</p>
      
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="prime-number">Number:</label>
          <input
            id="prime-number"
            type="number"
            min="2"
            step="1"
            value={number}
            onChange={(e) => setNumber(e.target.value)}
            className={`form-input ${error ? 'error' : ''}`}
            placeholder="Enter an integer ≥ 2..."
          />
          {error && <div className="error-message">{error}</div>}
        </div>
        
        <button type="submit" className="btn btn-primary" disabled={loading}>
          {loading ? <div className="loading"></div> : 'Check Prime'}
        </button>
      </form>

      {result && (
        <div className="result success">
          <h3>Result:</h3>
          <div className="result-value">
            {result.input} is {result.is_prime ? '' : 'not '}a prime number
            {result.is_prime ? ' ✓' : ' ✗'}
          </div>
        </div>
      )}
    </div>
  );
}

export default PrimeChecker;