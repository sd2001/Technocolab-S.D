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
            min_t[-1]=temperature
        if not max_t[-1] or temperature > max_t[-1]:
            max_t[-1]=temperature
    #days = dates.date2num(days)
    #plt.xticks(days)
    #return days,min_t,max_t
    print(min_t)
    print(max_t)
    plot_bars(days,min_t,max_t)
    plot_line(days,min_t,max_t)

def plot_bars(days,min_t,max_t):  
        print(days)      
        days=dates.date2num(days)
        print(days) 
        min_temp_bar=plt.bar(days-0.2, min_t, width=0.4, color='r')
        max_temp_bar=plt.bar(days+0.2, max_t, width=0.4, color='b')        
        plt.xticks(days)
        x_y_axis=plt.gca()
        xaxis_format=dates.DateFormatter('%m/%d')
        
        x_y_axis.xaxis.set_major_formatter(xaxis_format)
        
        for bar_chart in [min_temp_bar,max_temp_bar]:
            for index,bar in enumerate(bar_chart):
                height=bar.get_height()
                xpos=bar.get_x()+bar.get_width()/2.0
                ypos=height 
                label_text=str(int(height))
                plt.text(xpos, ypos,label_text,
                        horizontalalignment='center',
                        verticalalignment='bottom',
                        color='black')
        
        
        plt.savefig('figure.png')

def plot_line(days,min_t,max_t):        
        days=dates.date2num(days)
        rcParams['figure.figsize']=7,4
        plt.plot(days,max_t,color='green',linestyle='dashdot',linewidth = 1,marker='o',markerfacecolor='red',markersize=7) 
        plt.plot(days,min_t,color='orange',linestyle='dashdot',linewidth = 1,marker='o',markerfacecolor='blue',markersize=7)     
        plt.ylim(min(min_t)-4,max(max_t)+4)
        plt.xticks(days)
        x_y_axis=plt.gca()
        xaxis_format=dates.DateFormatter('%m/%d')
        
        
        x_y_axis.xaxis.set_major_formatter(xaxis_format)
        plt.grid(True,color='brown')
        plt.legend(["Maximum Temperaure","Minimum Temperature"],loc=1) 
        plt.xlabel('Dates(mm/dd)') 
        plt.ylabel('Temperature') 
        plt.title('5-Day Weather Forecast')   
        
        for i in range(5):
            plt.text(days[i], min_t[i]-1.5,min_t[i],
                        horizontalalignment='center',
                        verticalalignment='bottom',
                        color='black')
        for i in range(5):
            plt.text(days[i], max_t[i]+0.5,max_t[i],
                        horizontalalignment='center',
                        verticalalignment='bottom',
                        color='black')
        plt.show()
        plt.savefig('E:\Technocolab\Final Project\figure_line.png')