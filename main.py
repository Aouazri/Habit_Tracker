import requests
from datetime import datetime

USERNAME = "your username"
TOKEN = "your token"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# Creating User
response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)

# Creating a graph definition
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "min",
    "type": "int",
    "color": "ajisai",  # purple color
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)

# Posting a pixel
today = datetime.now()
post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"
pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many minutes did you code today? "),
}
response = requests.post(url=post_pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)

# Update a pixel
update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/20220914"
update_config = {
    "quantity": "59",
}
response = requests.put(url=update_pixel_endpoint, json=update_config, headers=headers)
print(response.text)

# Delete a pixel
delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/20220914"
response = requests.delete(url=delete_pixel_endpoint, headers=headers)
print(response.text)
