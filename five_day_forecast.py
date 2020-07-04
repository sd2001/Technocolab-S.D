import matplotlib.pyplot as plt
from matplotlib import dates
from datetime import datetime
import pyowm

owm=pyowm.OWM('0833f103dc7c2924da06db624f74565c')
mgr=owm.weather_manager()

def find_min_max(place,unit):
    days=[]
    dates_2=[]
    min_t=[]
    max_t=[]
    forecaster = mgr.forecast_at_place(place, '3h')
    forecast = forecaster.forecast
    if unit=='Celcius':
        unit_c='celsius'
    else:
        unit_c='fahrenheit'
    
    for weather in forecast:
        day = datetime.utcfromtimestamp(weather.reference_time())
        date = day.date()
        if date not in dates_2:
            dates_2.append(date)
            min_t.append(None)
            max_t.append(None)
            days.append(date)
        temperature = weather.temperature(unit_c)['temp']
        if not min_t[-1] or temperature < min_t[-1]:
            min_t[-1] = temperature
        if not max_t[-1] or temperature > max_t[-1]:
            max_t[-1] = temperature
    #days = dates.date2num(days)
    #plt.xticks(days)
    #return days,min_t,max_t
    print(min_t)
    print(max_t)
    plot_bars(days,max_t,min_t)
    
def plot_bars(days,min_t,max_t):
        days = dates.date2num(days)
        bar_min = plt.bar(days-0.2, min_t, width=0.4, color='r')
        bar_max = plt.bar(days+0.2, max_t, width=0.4, color='b')        
        plt.xticks(days)
        x_y_axis=plt.gca()
        xaxis_format = dates.DateFormatter('%m/%d')
        x_y_axis.xaxis.set_major_formatter(xaxis_format)
        plt.show()   
