import pyowm
from pyowm.utils import timestamps
from datetime import timedelta, datetime

owm=pyowm.OWM('0833f103dc7c2924da06db624f74565c')
mgr=owm.weather_manager()
place=input("Enter tha name of the place : ")
forecaster = mgr.forecast_at_place(place,'3h')
time1=timestamps.tomorrow(15,0)
weather=forecaster.get_weather_at(time1)
temperature=weather.temperature(unit='fahrenheit')['temp']

print(f'The temperature of {place} at {time1} is {temperature}')

#input-Enter tha name of the place : Los Angeles, US
#output-The temperature of Los Angeles, US at 2020-07-04 15:00:00 is 72.61