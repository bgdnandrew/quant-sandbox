# QuantSandbox

![QuantSandbox Logo](https://quantsandbox.io/quant-sandbox-github-logo.png)

An open-source quantitative analysis platform for exploring financial markets through algorithmic lenses. Built with Django (Python) and DRF.

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Django](https://img.shields.io/badge/Django-5.1-green)
![DRF](https://img.shields.io/badge/DRF-3.14-red)
![License](https://img.shields.io/badge/License-MIT-green)

## Quick Links

- 🌐 [Live Platform](https://quantsandbox.io)
- 🧠 [Backend (this repo)](https://github.com/bgdnandrew/quant-sandbox)
- 🎨 [Frontend Repository](https://github.com/bgdnandrew/quant-sandbox-frontend)
- 👨‍💻 [Bogdan's Website](https://bgdnandrew.com)

## About the Author

**Bogdan Andrei**

- 🌐 Personal Website: [bgdnandrew.com](https://bgdnandrew.com)
- ✖️ X/ Twitter: [@bgdnandrew](https://twitter.com/bgdnandrew)
- 💼 GitHub: [@bgdnandrew](https://github.com/bgdnandrew)
- 🏢 Software Agency: [Oriented Platforms](https://orientedplatforms.com)

## Project Overview

QuantSandbox.io is a Python-based quantitative finance platform that brings professional-grade quantitative analysis tools to anyone interested in exploring financial markets. By combining powerful algorithms with an intuitive interface, it makes quant analysis more accessible.

### Inspiration

This project draws inspiration from educational resources that have made quantitative finance more accessible:

- [Quantopian Lectures](https://gist.github.com/ih2502mk/50d8f7feb614c8676383431b056f4291) (sunsetted)

> **From Wikipedia:** Quantopian was a company that aimed to create a crowd-sourced hedge fund by letting freelance quantitative analysts develop, test, and use trading algorithms to buy and sell securities. In November 2020, Quantopian announced it would shut down after 9 years of operation.

- [PythonProgramming.net](https://pythonprogramming.net) by Sentdex

## Arhitecture Overview

```
                 API LAYER
           (Django REST Framework)
                    ↓ ↑
               SERVICE LAYER
           (Algo Implementations)
                    ↓ ↑
              DATA PROCESSING
               (Pandas/NumPy)
                    ↓ ↑
                DATA SOURCES
          (yfinance/ Alpha Vantage)
```

## Core Features

> **Note on Documentation Style:** Throughout this documentation, you'll notice the use of "we" instead of "I". While this version of the project was developed solely by myself (Bogdan), the use of "we" reflects the collaborative spirit of open-source development and acknowledges the broader community that inspires and supports projects like this.

### 1. Correlation Analysis (algo #1)

Our first implemented algorithm examines the relationship between 2 stocks' movements over a given time period:

- Calculates correlation coefficients and covariance
- Handles missing data and alignment automatically
- Provides comprehensive metadata about the analysis
- Uses pandas for efficient data processing

### 2. Future Algorithms and Features (on the roadmap)

- Volatility Analysis
- Mean Reversion Strategy
- Momentum Analysis
- Pairs Trading Implementation
- Risk Metrics Calculator
- Portfolio Optimization
- Technical Indicator Suite
- Supervised & Unsupervised ML

## Technical Architecture

### Backend Stack

- Django 5.1.3
- Django REST Framework
- PostgreSQL (Production)
- SQLite (Development)
- yfinance for market data; will need to switch to something more robust soon (maybe Alpha Vantage)

### Architectural Decisions

#### 1. Static Class Pattern

We use static classes as namespaces for related functionality:

```python
class CorrelationCalculator:
    @staticmethod
    def calculate(ticker1: str, ticker2: str, ...):
        # Implementation
```

**Benefits:**

- Groups related functionality without instance state
- Provides clear namespace separation
- Enables easy extension while maintaining encapsulation
- Eliminates need for object instantiation

#### 2. Data Processing Pipeline

Our correlation analysis algo implements the following pipeline:

1. Date Handling & Validation
2. Data Fetching
3. Data Alignment
4. Returns Calculation
5. Statistical Analysis
6. Result Validation

#### 3. Error Handling Strategy

We implement a comprehensive error handling system:

```python
try:
    # Core logic
except ValueError as e:
    raise ValueError(f"Specific error context: {str(e)}")
except Exception as e:
    raise ValueError(f"Calculation error: {str(e)}")
```

#### 4. Type Hints

We leverage Python's type hinting system for better code maintainability:

```python
from typing import Dict, Any, Optional

def calculate(
    ticker1: str,
    ticker2: str,
    start_date: Optional[datetime] = None
) -> Dict[str, Any]:
    # Implementation
```

## Getting Started

### Prerequisites

- Python 3.10+
- pip (Python package manager)
- Git
- PostgreSQL (for production)
- venv

### Local Development Setup

1. **Clone the Repository**

```bash
git clone https://github.com/bgdnandrew/quant-sandbox.git
cd quant-sandbox
```

2. **Create and Activate Virtual Environment**

```bash
python3 -m venv .venv-quant-sandbox
source .venv-quant-sandbox/bin/activate  # On Unix/macOS
```

3. **Install Dependencies**

```bash
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```

4. **Environment Configuration**
   Create a `.env` file based on `.env.example`:

```bash
cp .env.example .env
```

Example `.env` configuration:

```plaintext
DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
DB_NAME=quant_sandbox
DB_USER=db_user
DB_PASSWORD=your-password
DB_HOST=localhost
DB_PORT=5432
CORS_ALLOWED_ORIGINS=http://localhost:3000
```

5. **Database Setup**

```bash
python3 manage.py migrate
python3 manage.py createsuperuser
```

6. **Run Development Server**

```bash
python3 manage.py runserver
```

### Project Structure

```plaintext
quant-sandbox/
├── .development-docs/     # evolving documentation; ignored by git; meant to be a precursor for actual documentation
├── algorithms/            # Core algorithm implementations; not a django app
├── correlation_analysis/  # Django app for correlation analysis
├── quant_sandbox/        # Project configuration
│   ├── settings/
│   │   ├── base.py
│   │   ├── dev.py
│   │   └── prod.py
│   ├── urls.py
│   └── wsgi.py
├── static/               # Static files
├── .env.example         # Environment variables template
├── .gitignore
├── manage.py
└── requirements.txt
```

### Development Workflow

#### Settings Management

We use a split settings approach:

- `base.py`: Common settings
- `dev.py`: Development-specific settings
- `prod.py`: Production-specific settings

To use different settings:

```bash
# Development
python3 manage.py runserver --settings=quant_sandbox.settings.dev

# Production
python3 manage.py runserver --settings=quant_sandbox.settings.prod
```

Running your server with this type of settings flag, is possible due to the enhanced version of the `manage.py` script we're using.

#### API Testing

Using Postman:

1. Create a new POST request
2. URL: `http://localhost:8000/api/correlation/correlation-analysis/`
3. Headers:
   ```
   Content-Type: application/json
   ```
4. Body (raw JSON):
   ```json
   {
     "ticker1": "AAPL",
     "ticker2": "MSFT",
     "start_date": "2023-01-01",
     "end_date": "2024-01-01"
   }
   ```

## Contributing

We welcome contributions! Here's how you can help:

### Code Style Guide

1. **Python Style**

- Follow PEP 8 guidelines
- Use Black for code formatting
- Maximum line length: 88 characters (Black default)
- Use type hints for function parameters and return values

2. **Docstring Format**

```python
def function_name(param1: type, param2: type) -> return_type:
    """
    Brief description.

    Detailed description if needed.

    Args:
        param1: Description of param1
        param2: Description of param2

    Returns:
        Description of return value

    Raises:
        ExceptionType: Description of when this exception occurs
    """
    pass
```

3. **Commit Message Format**

```
type(scope): description

[optional body]

[optional footer]
```

Types:

- feat: New feature
- fix: Bug fix
- docs: Documentation changes
- style: Code style changes (formatting, etc.)
- refactor: Code refactoring
- test: Adding missing tests
- chore: Maintenance tasks

### Pull Request Process

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Run tests
5. Update documentation
6. Commit your changes (`git commit -m 'feat: Add amazing feature'`)
7. Push to your branch (`git push origin feature/AmazingFeature`)
8. Open a Pull Request

### Testing

> **Note:** Testing infrastructure is currently under development.

Run tests before submitting PRs:

```bash
python3 manage.py test
```

Code coverage:

```bash
coverage run manage.py test
coverage report
```

## API Documentation

### Correlation Analysis Endpoint

#### POST /api/correlation/correlation-analysis/

Calculates correlation metrics between two stocks over a specified time period.

**Request Body:**

```json
{
  "ticker1": "AAPL",
  "ticker2": "MSFT",
  "start_date": "2023-01-01", // Optional
  "end_date": "2024-01-01" // Optional
}
```

**Response:**

```json
{
  "correlation": 0.8534,
  "covariance": 0.000234,
  "start_date": "2023-01-01",
  "end_date": "2024-01-01",
  "ticker1": "AAPL",
  "ticker2": "MSFT",
  "data_points": 252,
  "first_date": "2023-01-03",
  "last_date": "2023-12-29",
  "trading_days": 255
}
```

**Error Responses:**

- 400 Bad Request: Invalid input data
- 500 Internal Server Error: Server-side processing error

### Response Field Descriptions

| Field        | Type    | Description                                           |
| ------------ | ------- | ----------------------------------------------------- |
| correlation  | float   | Pearson correlation coefficient between stock returns |
| covariance   | float   | Covariance between stock returns                      |
| start_date   | date    | Requested analysis start date                         |
| end_date     | date    | Requested analysis end date                           |
| data_points  | integer | Number of valid data points used                      |
| trading_days | integer | Total number of trading days in range                 |

## Testing Standards (🚧 To Be Implemented)

> **Note:** Testing infrastructure is currently under development.

Contributors interested in helping set up the testing infrastructure are welcome!

## Project Roadmap

1. **Algo Suite Expansion**

   - [ ] Volatility Analysis Implementation
   - [ ] Portfolio Optimization Tools
   - [ ] Enhanced Data Visualization
   - [ ] Supervised/ Unsupervised ML Features
   - [ ] Other Algos

2. **Technical Improvements**

   - [ ] Service Worker Implementation
   - [ ] Improved Error Handling
   - [ ] Performance Optimization
   - [ ] Enhanced Type Safety

3. **User Experience**

   - [ ] Responsive Design Improvements
   - [ ] Enhanced Form Validation
   - [ ] Interactive Tutorials

4. **Advanced Features**

   - [ ] Real-time Market Data Integration
   - [ ] Custom Algorithm Builder
   - [ ] Advanced Portfolio Analytics
   - [ ] Complex Machine Learning Integration

5. **Infrastructure**

   - [ ] Caching Layer Implementation
   - [ ] API Rate Limiting
   - [ ] Performance Monitoring
   - [ ] Automated Testing Pipeline
   - [ ] Real-time Data Processing
   - [ ] Distributed Computing Support

6. **User Features**

   - [ ] User Accounts
   - [ ] Saved Analysis History
   - [ ] Custom Dashboards
   - [ ] Analysis Sharing

### Longer Term Platform Evolution

- Community-contributed Algorithms
- Advanced Backtesting Framework
- Real-time Trading Integration
- Educational Resources

## Additional Resources

### Learning Resources

- [Django for Beginners](https://djangoforbeginners.com/introduction) by Will S. Vincent; IMHO this is **the best** Django resource for beginners out there; Will is regularly updating the website.

- [Python for Finance](https://pythonprogramming.net/getting-stock-prices-python-programming-for-finance/) by Sentdex
- [Quantopian Lectures](https://gist.github.com/ih2502mk/50d8f7feb614c8676383431b056f4291)
- [Quantitative Economics with Python](https://python.quantecon.org/) by QuantEcon
- [Awesome Quant](https://github.com/wilsonfreitas/awesome-quant) on GitHub

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 Bogdan Andrei

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files...
```

## Support

For support, questions, or collaboration:

- 📧 Email: bogdan [at] orientedplatforms.com
- ✖️ X/ Twitter: [@bgdnandrew](https://x.com/bgdnandrew)
- 🌐 Website: [bgdnandrew.com](https://bgdnandrew.com)

---

Built with ❤️ by [Bogdan Andrei](https://bgdnandrew.com) and the open-source community.
