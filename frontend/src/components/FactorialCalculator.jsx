import React, { useState } from 'react';
import MathAPI from '../services/api';

function FactorialCalculator() {
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
    if (isNaN(numValue) || numValue < 0 || !Number.isInteger(parseFloat(number))) {
      setError('Please enter a non-negative integer');
      return;
    }

    setLoading(true);
    setError('');
    
    try {
      const response = await MathAPI.getFactorial(numValue);
      setResult(response);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="card">
      <h2>Factorial Calculator</h2>
      <p>Calculate the factorial of a non-negative integer (n!)</p>
      
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="factorial-number">Number:</label>
          <input
            id="factorial-number"
            type="number"
            min="0"
            step="1"
            value={number}
            onChange={(e) => setNumber(e.target.value)}
            className={`form-input ${error ? 'error' : ''}`}
            placeholder="Enter a non-negative integer..."
          />
          {error && <div className="error-message">{error}</div>}
        </div>
        
        <button type="submit" className="btn btn-primary" disabled={loading}>
          {loading ? <div className="loading"></div> : 'Calculate Factorial'}
        </button>
      </form>

      {result && (
        <div className="result success">
          <h3>Result:</h3>
          <div className="result-value">{result.input}! = {result.result.toLocaleString()}</div>
        </div>
      )}
    </div>
  );
}

export default FactorialCalculator;