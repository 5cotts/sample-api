import axios from 'axios';

// Configure axios with base URL
const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Add request/response interceptors for better error handling
api.interceptors.response.use(
  (response) => response,
  (error) => {
    console.error('API Error:', error);
    return Promise.reject(error);
  }
);

export class MathAPI {
  // GET endpoints
  static async getSquare(number) {
    try {
      const response = await api.get(`/square/${number}`);
      return response.data;
    } catch (error) {
      throw new Error(error.response?.data?.detail || 'Failed to calculate square');
    }
  }

  static async getFactorial(number) {
    try {
      const response = await api.get(`/factorial/${number}`);
      return response.data;
    } catch (error) {
      throw new Error(error.response?.data?.detail || 'Failed to calculate factorial');
    }
  }

  static async getFibonacci(count) {
    try {
      const response = await api.get(`/fibonacci/${count}`);
      return response.data;
    } catch (error) {
      throw new Error(error.response?.data?.detail || 'Failed to generate Fibonacci sequence');
    }
  }

  static async isPrime(number) {
    try {
      const response = await api.get(`/prime/${number}`);
      return response.data;
    } catch (error) {
      throw new Error(error.response?.data?.detail || 'Failed to check if number is prime');
    }
  }

  // POST endpoints
  static async calculatePower(base, exponent) {
    try {
      const response = await api.post('/power', { base, exponent });
      return response.data;
    } catch (error) {
      throw new Error(error.response?.data?.detail || 'Failed to calculate power');
    }
  }

  static async calculateStats(numbers) {
    try {
      const response = await api.post('/stats', { numbers });
      return response.data;
    } catch (error) {
      throw new Error(error.response?.data?.detail || 'Failed to calculate statistics');
    }
  }

  // Health check
  static async getHealth() {
    try {
      const response = await api.get('/health');
      return response.data;
    } catch (error) {
      throw new Error('Failed to check API health');
    }
  }

  // API info
  static async getApiInfo() {
    try {
      const response = await api.get('/');
      return response.data;
    } catch (error) {
      throw new Error('Failed to get API information');
    }
  }
}

export default MathAPI;