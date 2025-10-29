import React, { useState } from 'react';
import MathAPI from '../services/api';

function StatisticsCalculator() {
  const [numbersInput, setNumbersInput] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!numbersInput.trim()) {
      setError('Please enter some numbers');
      return;
    }

    // Parse numbers from input (comma-separated or space-separated)
    const numberStrings = numbersInput
      .split(/[,\s]+/)
      .filter(s => s.trim() !== '');
    
    if (numberStrings.length === 0) {
      setError('Please enter valid numbers');
      return;
    }

    const numbers = [];
    for (const str of numberStrings) {
      const num = parseFloat(str.trim());
      if (isNaN(num)) {
        setError(`"${str}" is not a valid number`);
        return;
      }
      numbers.push(num);
    }

    setLoading(true);
    setError('');
    
    try {
      const response = await MathAPI.calculateStats(numbers);
      setResult(response);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="card">
      <h2>Statistics Calculator</h2>
      <p>Calculate basic statistics for a list of numbers</p>
      
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="stats-numbers">Numbers:</label>
          <input
            id="stats-numbers"
            type="text"
            value={numbersInput}
            onChange={(e) => setNumbersInput(e.target.value)}
            className={`form-input ${error ? 'error' : ''}`}
            placeholder="Enter numbers separated by commas or spaces (e.g., 1, 2, 3, 4, 5)"
          />
          <small style={{ color: '#718096', fontSize: '0.875rem' }}>
            Separate numbers with commas or spaces
          </small>
          {error && <div className="error-message">{error}</div>}
        </div>
        
        <button type="submit" className="btn btn-primary" disabled={loading}>
          {loading ? <div className="loading"></div> : 'Calculate Statistics'}
        </button>
      </form>

      {result && (
        <div className="result success">
          <h3>Statistics Results:</h3>
          <p><strong>Input:</strong> [{result.input_numbers.join(', ')}]</p>
          
          <table className="stats-table">
            <thead>
              <tr>
                <th>Statistic</th>
                <th>Value</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Count</td>
                <td>{result.statistics.count}</td>
              </tr>
              <tr>
                <td>Sum</td>
                <td>{result.statistics.sum}</td>
              </tr>
              <tr>
                <td>Mean</td>
                <td>{result.statistics.mean.toFixed(2)}</td>
              </tr>
              <tr>
                <td>Median</td>
                <td>{result.statistics.median}</td>
              </tr>
              <tr>
                <td>Minimum</td>
                <td>{result.statistics.min}</td>
              </tr>
              <tr>
                <td>Maximum</td>
                <td>{result.statistics.max}</td>
              </tr>
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}

export default StatisticsCalculator;