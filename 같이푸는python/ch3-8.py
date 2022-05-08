from pip import main
import requests
import json



city = "Seoul"
apikey =  "bd1d4ebff7a6583132ae3a7df26159a6"
api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}"


result = requests.get(api)

print(result.text)

data = json.loads(result.text)

#print(type(result.text))
#print(type(data))

print(data["name"],"의 날씨입니다.")
print("날씨는",data["weather"][0]["main"],"입니다")
print("현재 온도는 ",data["main"]["temp"],"입니다.")
print("하지만 체감 온도는 ",data["main"]["feels_like"],"입니다.")
print("최저온도는",data["main"]["temp_min"],"입니다.")
print("최고기온은",data["main"]["temp_max"],"입니다.")
print("습도는",data["main"]["humidity"],"입니다.")
print("기압은",data["main"]["pressure"],"입니다.")
print("풍향은",data["wind"]["deg"],"입니다.")
print("풍속은",data["wind"]["speed"],"입니다.")