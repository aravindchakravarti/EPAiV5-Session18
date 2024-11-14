# EPAiV5-Session18
Session 18 Assignment

Name: Aravind D. Chakravarti

This project uses GitHub Actions for continuous integration, running tests on Python 3.8 and 3.11.

![image](https://github.com/user-attachments/assets/b9454cca-d89c-489a-afaf-d62021351f6a)


![Build Status](https://github.com/aravindchakravarti/EPAiV5-Session18/actions/workflows/python-app.yml/badge.svg)

# Stock and Trade Data Serialization

## Overview
This project implements custom JSON serialization and deserialization for Stock and Trade data using both custom JSON encoders/decoders and Marshmallow schemas. It supports handling of complex data types including Decimal, DateTime, and Date objects.

## Features
- Custom JSON encoding/decoding for Stock and Trade objects
- Marshmallow schema validation and serialization
- Support for complex data types:
  - Decimal numbers for financial data
  - Date objects for stock quotes
  - DateTime objects for trade timestamps
- Comprehensive test suite
- CI/CD integration with GitHub Actions

## Requirements
- Python 3.8 or 3.11
- Required packages:
  - pytest
  - marshmallow

## Installation
1. Clone the repository
2. Create a virtual environment (recommended)
3. Install dependencies:

```bash
pip install -r requirements.txt
```


## Project Structure
- `assignment.py`: Core implementation with Stock and Trade classes
- `assignment_test.py`: Test suite
- `.github/workflows/python-app.yml`: CI configuration

## Classes

### Stock
Represents stock market quotes with properties:
- symbol
- date
- open
- high
- low
- close
- volume

### Trade
Represents trading transactions with properties:
- symbol
- timestamp
- order
- price
- volume
- commission

## Testing
Run tests using pytest:

```bash
pytest assignment_test.py
```
