import matplotlib.pyplot as plt2
from matplotlib import dates
from datetime import datetime
import pyowm
from matplotlib import rcParams

def plot_line(days,min_t,max_t):        
        days=dates.date2num(days)
        rcParams['figure.figsize']=7,4
        plt2.plot(days,max_t,color='green',linestyle='dashdot',linewidth = 1,marker='o',markerfacecolor='red',markersize=7) 
        plt2.plot(days,min_t,color='orange',linestyle='dashdot',linewidth = 1,marker='o',markerfacecolor='blue',markersize=7)     
        plt2.ylim(min(min_t)-4,max(max_t)+4)
        plt2.xticks(days)
        x_y_axis=plt2.gca()
        xaxis_format=dates.DateFormatter('%m/%d')
        
        
        x_y_axis.xaxis.set_major_formatter(xaxis_format)
        plt2.grid(True,color='brown')
        plt2.legend(["Maximum Temperaure","Minimum Temperature"],loc=1) 
        plt2.xlabel('Dates(mm/dd)') 
        plt2.ylabel('Temperature') 
        plt2.title('5-Day Weather Forecast')   
        
        for i in range(5):
            plt2.text(days[i], min_t[i]-1.5,min_t[i],
                        horizontalalignment='center',
                        verticalalignment='bottom',
                        color='black')
        for i in range(5):
            plt2.text(days[i], max_t[i]+0.5,max_t[i],
                        horizontalalignment='center',
                        verticalalignment='bottom',
                        color='black')
        #plt.show()
        plt2.savefig('figure_line.png')
        plt2.clf()