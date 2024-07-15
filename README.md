# Home Assignment - SW / Data Engineer for Data Science Group

# Masking API Service

## Overview

This  API service receives text input and masks sensitive information such as credit card numbers, phone numbers, and IP addresses. 
The service is designed to be modular, easy to test, and extendable for additional types of sensitive information.

## Features

- **Masking of sensitive information**: The service can mask credit card numbers, phone numbers, and IP addresses.
- **Modular design**: Easily extendable to handle more types of sensitive information.
- **Tested**: Comprehensive tests ensure the correctness of the service.


## Logging

- Logs are written to app.log in the root directory.
- Logs valid requests and their corresponding HTTP status codes (200 OK for successful requests, 4xx for client errors).


## Setup and Installation

### Prerequisites

- Python 3.6 or higher
- Flask
- pytest
- logging

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/AmitKey/mask-data.git
    cd mask-data
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv mask-data
    source mask-data/bin/activate  # On Windows, use `mask-data\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage


To start the Flask server, run:

```bash
python app.py 
```


## Tests

```bash
python test_app.py
```

