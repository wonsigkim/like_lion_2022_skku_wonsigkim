import requests
import json



city = "Seoul"
apikey =  "bd1d4ebff7a6583132ae3a7df26159a6"
api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}"


result = requests.get(api)

print(result.text)

data = json.loads(result.text)

print(type(result.text))
print(type(data))