import pyowm

owm=pyowm.OWM('0833f103dc7c2924da06db624f74565c')
mgr=owm.weather_manager()
place=input("Enter the name of the city : ")
obs=mgr.weather_at_place(place)
weather=obs.weather
temp=weather.temperature(unit='fahrenheit')['temp']

print(f'The Temperature of {place} is {temp} Fahrenheit')


#input : Enter the name of the city : Sydney, AU
#output : The Temperature of Sydney, AU is 61.34 Fahrenheit