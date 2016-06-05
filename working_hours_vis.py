import sqlite3
import datetime
import matplotlib.pyplot as plt
import numpy
import math


def get_startups(c):
    c.execute("select * from startups_shutdowns_computer where proxy != 'None' and is_startup = 1")
    return c.fetchall()

def get_shutdowns(c):
    c.execute("select * from startups_shutdowns_computer where proxy != 'None' and is_startup = 0")  
    return c.fetchall()


def plot(work_time_deltas_hours):
 
    # 45 minutes break is assumed    
    work_overtime = sum([w - 8.75 for w in work_time_deltas_hours ])
 
    plt.boxplot(work_time_deltas_hours)
    plt.ylabel("Working Hours")
        
    plt.xticks([0,1,2],())    
        
    yvalues = numpy.arange(numpy.floor(numpy.min(work_time_deltas_hours)),numpy.ceil(numpy.max(work_time_deltas_hours)),0.25)    
    plt.yticks(yvalues,[ str(math.floor(x)) + "h " + str(int((x % 1.0) * 60)) +"min" for x  in yvalues],rotation=0)
  
    # Debug
    print("Mean: "+str(numpy.mean(work_time_deltas_hours))) 
    print("Min: "+str(numpy.min(work_time_deltas_hours)))
    print("Max: "+str(numpy.max(work_time_deltas_hours)))
    print("Median: "+str(numpy.median(work_time_deltas_hours)))
    print("Work overtime: "+ str(work_overtime))
    print("Days tracked: "+str(len(work_time_deltas_hours)))
     
    plt.text(1.35,10,"Mean: " + str(math.floor(numpy.mean(work_time_deltas_hours))) + "h " + str(int((numpy.mean(work_time_deltas_hours) % 1.0) * 60)) + "min"
             "\nMax: " + str(math.floor(numpy.max(work_time_deltas_hours))) + "h " + str(int((numpy.max(work_time_deltas_hours) % 1.0) * 60)) + "min"
             "\nMin: "+ str(math.floor(numpy.min(work_time_deltas_hours))) + "h " + str(int((numpy.min(work_time_deltas_hours) % 1.0) * 60)) + "min"
             "\nMedian: "+ str(math.floor(numpy.median(work_time_deltas_hours))) + "h " + str(int((numpy.median(work_time_deltas_hours) % 1.0) * 60)) + "min"+
             "\nOvertime: " + str(math.floor(work_overtime)) +"h "+ str(int((work_overtime % 1.0) * 60)) + "min" +
             "\nDays: " + str(len(work_time_deltas_hours)),
             bbox=dict(boxstyle='round', facecolor='white', alpha=0.5))
    
    plt.title("Working Hours Boxplot")
    plt.show()   

def main():
    conn = sqlite3.connect("working_hours.db")   
    c = conn.cursor()
    
    startups = get_startups(c)   
    shutdowns = get_shutdowns(c)
        
    # Subtract start from end time and convert date and time strings to timedelta objects
    work_time_deltas = [datetime.datetime.strptime(end[0] +" "+end[1], "%Y-%m-%d %H:%M:%S") - datetime.datetime.strptime(start[0] +" "+start[1], "%Y-%m-%d %H:%M:%S") for start, end in zip(startups, shutdowns)]
   
    # Get a list of worked hours each day
    work_time_deltas_hours = [ work_time_delta.total_seconds() / 3600 for work_time_delta in work_time_deltas]


    
    plot(work_time_deltas_hours)

    
      


if __name__ == '__main__':
    main()
