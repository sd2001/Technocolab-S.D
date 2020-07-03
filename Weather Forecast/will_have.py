import pyowm
from pyowm.utils import timestamps
from datetime import timedelta, datetime

owm=pyowm.OWM('0833f103dc7c2924da06db624f74565c')
mgr=owm.weather_manager()
place=input("Enter the name of the place : ")
forecaster = mgr.forecast_at_place(place,'3h')
print(f"Cloud Forecast in {place} : ",forecaster.will_have_clouds())
print(f"Storm Forecast in {place} : ",forecaster.will_have_storm())
print(f"Clear Sky Forecast in {place} : ",forecaster.will_have_clear())

#input-Enter the name of the place : Los Angeles, US
#output-Cloud Forecast in Los Angeles, US :  False   Storm Forecast in Los Angeles, US :  False  Clear Sky Forecast in Los Angeles, US :  True