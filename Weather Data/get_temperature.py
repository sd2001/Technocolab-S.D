import pyowm

owm=pyowm.OWM('0833f103dc7c2924da06db624f74565c')
mgr=owm.weather_manager()
place=(input("Enter the city name : "))
obs=mgr.weather_at_place(place)
weather=obs.weather
temp_f=weather.temperature(unit='fahrenheit')['temp']
temp_c=weather.temperature(unit='celsius')['temp']

print(f'The Temperature of {place} is {temp_f} Fahrenheit and {temp_c} Celsius')

#input-Enter the city name : Kolkata
#output-The Temperature of Kolkata is 91.4 Fahrenheit and 33.0 Celsius