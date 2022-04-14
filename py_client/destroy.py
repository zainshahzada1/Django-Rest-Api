import json
import requests
product_id=input('Enter Product Id : ')
try:
    product_id=int(product_id)
except:
    product_id=None
    print(f'{product_id} is not Valid !')
endpoint = f'http://127.0.0.1:8000/api/products/{product_id}/destroy/'
data = {
    'title': 'Hello This is Second Title',
    'content': 'This is Second content',
    'price': 129.99
}
get_response = requests.delete(endpoint, json=data)
print(get_response.status_code,get_response.status_code==204)
