
import requests

# endpoint="http://httpbin.org/anything"
endpoint = 'https://suitecrmdemo.dtbc.eu/service/v2/rest.php'
get_response=requests.get(endpoint)
print(get_response.json())
