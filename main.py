import requests
from datetime import datetime

TOKEN = '1k2j3h1kj23h'
USERNAME = 'pndao'

pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

graph_config = {
    'id': 'graph11',
    'name': 'Cycle Graph',
    'unit': 'Km',
    'type': 'float',
    'color': 'ajisai'
}

headers = {
    'X-USER-TOKEN': TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f'{graph_endpoint}/graph11'

today = datetime.now()
date = today.strftime('%Y%m%d')

pixel_config = {
    'date': date,
    'quantity': input('How many kilometers did you cycle today?: ')
}

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)

update_endpoint = f'{pixel_endpoint}/{date}'

new_pixel_data = {
    'quantity': '9.1'
}

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

# response = requests.delete(url=update_endpoint, headers=headers)
# print(response.text)