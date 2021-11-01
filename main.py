import requests
from datetime import datetime
pixela_endpoint ="https://pixe.la/v1/users"
USERNAME = ""
TOKEN = ""
ID = "graph1"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": ID,
    "name": "Coding Graph",
    "unit": "hour",
    "type": "int",
    "color": "ichou"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# todays date
today = datetime.now()
# today = datetime(year=2021, month=10, day=29)
date = today.strftime("%Y%m%d")
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
quantity_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}"

quantity_config = {
    "date": date,
    "quantity": input("How many hours did you code today? ")
}
# response = requests.post(url=quantity_endpoint, json=quantity_config, headers=headers)
# print(response.text)

# update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}/{date}"
# quantity_update = {
#     "quantity": "100"
# }

response = requests.post(url=quantity_endpoint, json=quantity_config, headers=headers)
print(response.text)


# To Delete a graph

# response = requests.delete(url=quantity_endpoint, headers=headers)
# print(response.text)
