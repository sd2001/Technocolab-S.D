import pyowm

owm=pyowm.OWM('0833f103dc7c2924da06db624f74565c')
mgr=owm.weather_manager()
place=(input("Enter the city name : "))
obs=mgr.weather_at_place(place)
weather=obs.weather
cloud_cov=weather.clouds
winds=weather.wind()['speed']
print(f'The current cloud coverage for {place} is {cloud_cov}%')
print(f'The current wind speed for {place} is {winds}mph')

#input-The current cloud coverage for Los Angeles,California is 90%
#output-The current wind speed for Los Angeles,California is 1.98mph