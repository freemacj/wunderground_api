import urllib.request as request
import json
key = 'your_api_key_here'
while 1:
    zip_code = input('For which ZIP code would you like to see the weather? ')
    fileName = "http://api.wunderground.com/api/" + key +    "/geolookup/conditions/q/PA/" + zip_code + ".json"
    f = request.urlopen(fileName)
    json_string = f.read().decode('utf-8')
    parsed_json = json.loads(json_string)
    location = parsed_json['location']['city']
    temp_f = parsed_json['current_observation']['temp_f']
    city = parsed_json['location']['city']
    state = parsed_json['location']['state']
    weather = parsed_json['current_observation']['weather']
    temperature_string = parsed_json['current_observation']['temperature_string']
    feelslike_string = parsed_json['current_observation']['feelslike_string']
    print ('Weather in ' + city + ', ' + state + ': ' + weather.lower() + '. The temperature is ' + temperature_string + ' but it feels like ' + feelslike_string + '.')
    f.close()
#references: https://www.wunderground.com/weather/api/d/docs?d=resources/code-samples&MR=1
