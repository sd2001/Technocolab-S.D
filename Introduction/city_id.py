import pyowm

owm=pyowm.OWM('0833f103dc7c2924da06db624f74565c')
mgr=owm.weather_manager()
place=int(input("Enter the city id : "))
obs=mgr.weather_at_id(place)
weather=obs.weather
temp=weather.temperature(unit='fahrenheit')['temp']

print(f'The Temperature of {place} is {temp} Fahrenheit')

#input-Enter the city id : 6094817
#output-The Temperature of 6094817 is 75.65 Fahrenheit