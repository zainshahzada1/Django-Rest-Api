import json
from wsgiref import headers
import requests

endpoint = 'http://127.0.0.1:8000/api/products/'
header={
    'Authorization': 'Bearer 49ec97414da31ae4c94317e35485bb4f9dcfd4d3'
}
data={
    'title':'This is title'
}
get_response = requests.post(endpoint,json=data,headers=header)
print(get_response.json())
