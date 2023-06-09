# Simple Weather REST API

This is a simple REST API that allows users to retrieve, add, modify, and delete temperature data for various locations. The API is built using Python and Flask.

## Installation

To install and run the Simple Weather REST API, follow these steps:

1. Clone the repository: `git clone https://github.com/jxwleong/py-rest-api.git`
2. Navigate to the cloned directory: `cd py-rest-api`
3. Create a virtual environment: `python -m venv venv`
4. Activate the virtual environment: `source venv/bin/activate` (for Linux/MacOS) or `venv\Scripts\activate` (for Windows)
5. Install the dependencies: `pip install -r requirements.txt`
6. Run the server: `python api_server.py`
7. Access the API at `http://localhost:5000/`

## Usage

The Simple Weather REST API has the following functionalities:

- **GET** temperature data for a specific location: `GET /?location=<location>`
- **POST** new temperature data for a location: `POST /?location=<location>&temperature=<temperature>`
- **PUT** update temperature data for a location: `PUT /?location=<location>&temperature=<temperature>`
- **DELETE** delete temperature data for a location: `DELETE /?location=<location>`

Additionally, the following query parameter can be added to the GET request to retrieve all temperature data:

- `return_all_data=True`

### Example Usage

Here is an example Python script that demonstrates how to use the Simple Weather REST API:

```python
import requests

url = "http://localhost:5000/"

# Get temperature data for a specific location
response = requests.get(url=url, params={"location": "Ampang"})
print(response.text)

# Add new temperature data
response = requests.post(url=url, params={"location": "Petaling Jaya", "temperature": "35.1"})
print(response.text)

# Update existing temperature data
response = requests.put(url=url, params={"location": "Petaling Jaya", "temperature": "35.9"})
print(response.text)

# Delete temperature data
response = requests.delete(url=url, params={"location": "Petaling Jaya"})
print(response.text)

# Get all temperature data
response = requests.get(url=url, params={"return_all_data": "True"})
print(response.text)
