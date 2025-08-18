#pip install -r requirements.txt

import requests                                             #Requests module used for sending HTTP requests and fetching data from APIs
from plyer import notification                              #To create desktop notifications across all major operating systems.

city = input("Enter the city name: ")  

                                                            #Getting the data from open-metio.com to check whether the city is in there or not
geo_url = "https://geocoding-api.open-meteo.com/v1/search"
geo_parameters = {'name': city, 'count': 1}
geo_result = requests.get(geo_url, params = geo_parameters).json()

                                                            #if the city is in the data source then we will fetch the data like latitude and longitude using the API
if "results" in geo_result:
    latitude = geo_result["results"][0]["latitude"]
    longitude = geo_result["results"][0]["longitude"]

    weather_url = "https://api.open-meteo.com/v1/forecast"
    weather_parameters = {                                      #Contains coordinates and tells API to return only current weather.
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": True
    }

    weather_result = requests.get(weather_url, params = weather_parameters).json()

                                                            #testing whether the data is fetched correctly or not
                                                            #print(weather_res) 

                                                            #After having the data we will show it as a desktop notification
    if "current_weather" in weather_result:
        temp = weather_result["current_weather"]["temperature"]
        wind = weather_result["current_weather"]["windspeed"]
        weather_info = f"{city}: {temp}°C, wind {wind} km/h"

        print("weather: ",weather_info)

        notification.notify(                                #Shows the weather info in a desktop popup
            title = "Weather Update", 
            message = weather_info,
            timeout = 5                                     #Notification stays visible for 5 seconds
        )
    else:
        print("Weather data not found.")
else:
    print("City not found.")