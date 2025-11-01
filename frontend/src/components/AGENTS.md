# Component Agent Instructions: React Components

## Overview

Components in this directory follow a consistent pattern for interacting with the backend API. Each component handles one operation and demonstrates proper React patterns.

## Component Structure Pattern

Every component should follow this structure:

```javascript
import { useState } from 'react';
import MathAPI from '../services/api';

function OperationComponent() {
  // 1. State Management
  const [input, setInput] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  // 2. Submit Handler
  const handleSubmit = async (e) => {
    e.preventDefault();
    
    // Validation
    if (!input.trim()) {
      setError('Please enter a value');
      return;
    }

    // Parse and validate input
    const value = parseFloat(input);
    if (isNaN(value)) {
      setError('Please enter a valid number');
      return;
    }

    // API Call
    setLoading(true);
    setError('');
    
    try {
      const response = await MathAPI.getOperation(value);
      setResult(response);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  // 3. Render
  return (
    <div className="card">
      <h2>Operation Title</h2>
      <p>Description of operation</p>
      
      <form onSubmit={handleSubmit}>
        {/* Form inputs */}
        {/* Error display */}
        {/* Submit button with loading state */}
      </form>

      {/* Result display */}
    </div>
  );
}

export default OperationComponent;
```

## State Management Pattern

**Required State Variables:**
- `input` / `inputs` - Form input values
- `result` - API response data
- `loading` - Boolean for loading state
- `error` - Error message string

**State Updates:**
- Reset error on new submission
- Set loading true before API call
- Set loading false in finally block
- Clear result on new submission (optional)

## Form Validation Pattern

```javascript
// 1. Check if empty
if (!input.trim()) {
  setError('Please enter a value');
  return;
}

// 2. Parse and validate type
const value = parseFloat(input);
if (isNaN(value)) {
  setError('Please enter a valid number');
  return;
}

// 3. Validate business rules (if needed)
if (value < 0) {
  setError('Value must be non-negative');
  return;
}
```

## API Call Pattern

```javascript
setLoading(true);
setError('');

try {
  const response = await MathAPI.getOperation(value);
  setResult(response);
} catch (err) {
  setError(err.message);
} finally {
  setLoading(false);
}
```

**Always:**
- Set loading state
- Clear previous errors
- Handle errors gracefully
- Reset loading in finally

## Form Input Pattern

```javascript
<input
  id="operation-input"
  type="number"           // or text for complex inputs
  step="any"              // for number inputs
  value={input}
  onChange={(e) => setInput(e.target.value)}
  className={`form-input ${error ? 'error' : ''}`}
  placeholder="Enter a value..."
/>
```

**Features:**
- Controlled component (value + onChange)
- Conditional error styling
- Appropriate input type
- Accessible labels with htmlFor

## Error Display Pattern

```javascript
{error && (
  <div className="error-message">{error}</div>
)}
```

**Placement:**
- After form inputs
- Before submit button
- Clear and visible

## Loading State Pattern

```javascript
<button 
  type="submit" 
  className="btn btn-primary" 
  disabled={loading}
>
  {loading ? (
    <div className="loading"></div>
  ) : (
    'Calculate'
  )}
</button>
```

**Features:**
- Disable button during loading
- Show loading indicator
- Prevent multiple submissions

## Result Display Pattern

```javascript
{result && (
  <div className="result success">
    <h3>Result:</h3>
    <div className="result-value">
      {/* Format result appropriately */}
      {result.input}² = {result.result}
    </div>
  </div>
)}
```

**Features:**
- Conditional rendering
- Clear formatting
- Show both input and output
- Use appropriate semantic HTML

## Multiple Input Pattern

For operations requiring multiple inputs (e.g., power, stats):

```javascript
const [base, setBase] = useState('');
const [exponent, setExponent] = useState('');

const handleSubmit = async (e) => {
  e.preventDefault();
  
  // Validate both inputs
  const baseValue = parseFloat(base);
  const expValue = parseFloat(exponent);
  
  if (isNaN(baseValue) || isNaN(expValue)) {
    setError('Please enter valid numbers');
    return;
  }

  // API call with multiple parameters
  const response = await MathAPI.calculatePower(baseValue, expValue);
  setResult(response);
};
```

## Array Input Pattern

For operations requiring arrays (e.g., statistics):

```javascript
const [numbers, setNumbers] = useState('');

const handleSubmit = async (e) => {
  e.preventDefault();
  
  // Parse comma-separated or space-separated values
  const numberArray = numbers
    .split(/[,\s]+/)
    .map(num => parseFloat(num.trim()))
    .filter(num => !isNaN(num));
  
  if (numberArray.length === 0) {
    setError('Please enter at least one number');
    return;
  }

  const response = await MathAPI.calculateStats(numberArray);
  setResult(response);
};
```

## Component Naming

- Use descriptive names: `SquareCalculator`, `PowerCalculator`
- Follow PascalCase convention
- Match operation name from backend

## File Naming

- Component files: `OperationName.jsx`
- Export default component
- Import as needed in App.jsx

## Best Practices

1. **Single Responsibility**: One component = one operation
2. **Reusability**: Extract common patterns (but keep simple for this educational project)
3. **Accessibility**: Use proper labels, ARIA attributes if needed
4. **User Experience**: Clear error messages, loading feedback
5. **Code Clarity**: Self-documenting code with clear variable names

## Example: Complete Component

Reference `SquareCalculator.jsx` for a complete example following all patterns.

## Adapting for New Operations

1. Create new component file
2. Copy structure from similar existing component
3. Update API service call
4. Adjust input validation
5. Format result display appropriately
6. Add to App.jsx

