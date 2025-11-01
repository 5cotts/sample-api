import { useState } from 'react';
import MathAPI from '../services/api';

function PowerCalculator() {
  const [base, setBase] = useState('');
  const [exponent, setExponent] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!base.trim() || !exponent.trim()) {
      setError('Please enter both base and exponent');
      return;
    }

    const baseValue = parseFloat(base);
    const exponentValue = parseFloat(exponent);
    
    if (isNaN(baseValue) || isNaN(exponentValue)) {
      setError('Please enter valid numbers');
      return;
    }

    setLoading(true);
    setError('');
    
    try {
      const response = await MathAPI.calculatePower(baseValue, exponentValue);
      setResult(response);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="card">
      <h2>Power Calculator</h2>
      <p>Calculate base raised to the power of exponent (base^exponent)</p>
      
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="power-base">Base:</label>
          <input
            id="power-base"
            type="number"
            step="any"
            value={base}
            onChange={(e) => setBase(e.target.value)}
            className={`form-input ${error ? 'error' : ''}`}
            placeholder="Enter base number..."
          />
        </div>
        
        <div className="form-group">
          <label htmlFor="power-exponent">Exponent:</label>
          <input
            id="power-exponent"
            type="number"
            step="any"
            value={exponent}
            onChange={(e) => setExponent(e.target.value)}
            className={`form-input ${error ? 'error' : ''}`}
            placeholder="Enter exponent..."
          />
        </div>
        
        {error && <div className="error-message">{error}</div>}
        
        <button type="submit" className="btn btn-primary" disabled={loading}>
          {loading ? <div className="loading"></div> : 'Calculate Power'}
        </button>
      </form>

      {result && (
        <div className="result success">
          <h3>Result:</h3>
          <div className="result-value">
            {result.base}^{result.exponent} = {result.result}
          </div>
        </div>
      )}
    </div>
  );
}

export default PowerCalculator;