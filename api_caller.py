import requests
url = "http://127.0.0.1:5000/"

# Get all data
print("Existing Temperature data")
params={"return_all_data": "True"}
response = requests.get(url=url, params=params)
print(response.text)

# Get existing data
print("GET Ampang Temperature")
params={"location": "Ampang"}
response = requests.get(url=url, params=params)
print(response.text)

# Post new data
# Atttempt wrong first (Try to post existing location)...
print("Trying to POST existing data")
params={"location": "Kajang", "temperature": "35.1"}
response = requests.post(url=url, params=params)
print(response.text)


print("POST new data")
params={"location": "Petaling Jaya", "temperature": "35.1"}
response = requests.post(url=url, params=params)
print(response.text)

# Get all data
params={"return_all_data": "True"}
response = requests.get(url=url, params=params)
print(response.text)

# Put existing data
print("PUT Petaling Jaya temperature data")
params={"location": "Petaling Jaya", "temperature": "35.9"}
response = requests.put(url=url, params=params)
print(response.text)

# Get all data
params={"return_all_data": "True"}
response = requests.get(url=url, params=params)
print(response.text)

# Delete data
print("DELETE Petaling Jaya temperature data")
params={"location": "Petaling Jaya"}
response = requests.delete(url=url, params=params)
print(response.text)

# Get all data
params={"return_all_data": "True"}
response = requests.get(url=url, params=params)
print(response.text)
