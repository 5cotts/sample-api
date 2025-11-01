import { useState } from 'react';
import MathAPI from '../services/api';

function SquareCalculator() {
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

    const numValue = parseFloat(number);
    if (isNaN(numValue)) {
      setError('Please enter a valid number');
      return;
    }

    setLoading(true);
    setError('');
    
    try {
      const response = await MathAPI.getSquare(numValue);
      setResult(response);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="card">
      <h2>Square Calculator</h2>
      <p>Calculate the square of a number (n²)</p>
      
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="square-number">Number:</label>
          <input
            id="square-number"
            type="number"
            step="any"
            value={number}
            onChange={(e) => setNumber(e.target.value)}
            className={`form-input ${error ? 'error' : ''}`}
            placeholder="Enter a number..."
          />
          {error && <div className="error-message">{error}</div>}
        </div>
        
        <button type="submit" className="btn btn-primary" disabled={loading}>
          {loading ? <div className="loading"></div> : 'Calculate Square'}
        </button>
      </form>

      {result && (
        <div className="result success">
          <h3>Result:</h3>
          <div className="result-value">{result.input}² = {result.result}</div>
        </div>
      )}
    </div>
  );
}

export default SquareCalculator;