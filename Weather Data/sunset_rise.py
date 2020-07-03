import pyowm

owm=pyowm.OWM('0833f103dc7c2924da06db624f74565c')
mgr=owm.weather_manager()
place=(input("Enter the city name : "))
obs=mgr.weather_at_place(place)
weather=obs.weather
print(f"Sunset time in {place} is ",weather.sunset_time(timeformat='iso'))
print(f"Sunrise time in {place} is ",weather.sunrise_time(timeformat='iso'))

#input-Enter the city name : Boston, US
#output-Sunset time in Boston, US is  2020-07-03 00:24:34+00     Sunrise time in Boston, US is  2020-07-02 09:11:52+00