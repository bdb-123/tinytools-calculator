# TinyTools Calculator

A production-ready calculator with add, subtract, multiply, and divide.

## Setup

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
pylint --errors-only src
pytest tests -v
coverage run -m pytest tests
coverage report --fail-under=100
# TinyTools Calculator
