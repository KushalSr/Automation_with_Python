import requests

baseUrl = 'http://api.openweathermap.org/data/2.5/forecast'
parameters = {'APPID': '06d40cb41f01b834f9bf3b06ff62929e', 'q': 'Seattle,US'}

response = requests.get(baseUrl, params=parameters)
print(response.content)





