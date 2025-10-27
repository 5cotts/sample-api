import React, { useState } from 'react';
import MathAPI from '../services/api';

function FibonacciGenerator() {
  const [count, setCount] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!count.trim()) {
      setError('Please enter a count');
      return;
    }

    const countValue = parseInt(count);
    if (isNaN(countValue) || countValue <= 0 || !Number.isInteger(parseFloat(count))) {
      setError('Please enter a positive integer');
      return;
    }

    if (countValue > 50) {
      setError('Please enter a number 50 or less for better performance');
      return;
    }

    setLoading(true);
    setError('');
    
    try {
      const response = await MathAPI.getFibonacci(countValue);
      setResult(response);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="card">
      <h2>Fibonacci Generator</h2>
      <p>Generate the first N numbers in the Fibonacci sequence</p>
      
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="fibonacci-count">Count:</label>
          <input
            id="fibonacci-count"
            type="number"
            min="1"
            max="50"
            step="1"
            value={count}
            onChange={(e) => setCount(e.target.value)}
            className={`form-input ${error ? 'error' : ''}`}
            placeholder="Enter number of Fibonacci numbers (1-50)..."
          />
          {error && <div className="error-message">{error}</div>}
        </div>
        
        <button type="submit" className="btn btn-primary" disabled={loading}>
          {loading ? <div className="loading"></div> : 'Generate Sequence'}
        </button>
      </form>

      {result && (
        <div className="result success">
          <h3>Fibonacci Sequence (first {result.count} numbers):</h3>
          <div className="result-list">
            [{result.sequence.join(', ')}]
          </div>
          <p style={{ marginTop: '1rem', color: '#718096' }}>
            Length: {result.sequence.length}
          </p>
        </div>
      )}
    </div>
  );
}

export default FibonacciGenerator;