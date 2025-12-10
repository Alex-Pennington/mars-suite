# Contributing to MARS Suite

Thank you for your interest in contributing to the Phoenix Nest MARS Communications Suite!

## Getting Started

1. Fork the repository
2. Clone your fork locally
3. Create a new branch for your feature or bugfix
4. Make your changes
5. Test your changes thoroughly
6. Submit a pull request

## Development Setup

```bash
# Clone the repository
git clone https://github.com/Alex-Pennington/mars-suite.git
cd mars-suite

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements-dev.txt
```

## Code Style

- Follow PEP 8 guidelines for Python code
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Keep functions focused and concise

## Testing

- Write tests for new features
- Ensure all tests pass before submitting a PR
- Aim for good test coverage

```bash
# Run tests
pytest

# Run tests with coverage
pytest --cov=mars_suite
```

## Communication

- For bugs and feature requests, please open an issue
- For questions and discussions, use GitHub Discussions
- Contact: projects@organicengineer.com

## Amateur Radio Guidelines

As this project is intended for MARS operations:
- Ensure all digital modes comply with FCC regulations
- Follow proper operating procedures
- Respect bandwidth limitations
- Maintain proper station identification

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
