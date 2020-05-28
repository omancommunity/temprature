import numpy as np
import csv
from datetime import datetime

np.set_printoptions(precision=1)
PATH= "temp.csv"
def get_cvs(path=PATH):
    print("Reading CSV file...")
    with open(PATH) as csvfile:
     readCSV = csv.reader(csvfile, delimiter=',')
     temps = np.empty([34147 , 1])
     temps2 = np.array([34147, 1], dtype=float)
     dates = np.empty([34147 , 1] ,  dtype='datetime64[s]')


     for i ,row in enumerate(readCSV):

        
    
            dt=datetime.strptime(row[0][0:10], '%d/%m/%Y')
            dt64 = np.datetime64(dt)
            dates[i,0] =dt64

            temps[i,0] = float(row[1])
            #print("inside if if " , float(row[1]))

     print("CSV file Reading complete!.")
     np.set_printoptions(precision=1)
     return temps,dates
def getMaxOfWholePeriod():
    temps , dates = get_cvs(PATH)

    min = np.argmax(temps, axis = 1)
    print("The Maximum Temprature ever recorded in the period is : ",np.amax(temps))

    result = np.where(temps == np.amax(temps))

 

    print("And that in the date:",dates[result[0]])

def getTheHottestYear():
    temps, dates = get_cvs(PATH)

    year2011 = []
    year2012 = []
    year2013 = []
    year2014 = []
    print("getting the hottest year.")
    print("processing... ")
    for r ,t in enumerate(temps):

        if(str(dates[r])[2:6] == "2011"):
            year2011.append(t)
        if (str(dates[r])[2:6] == "2012"):
            year2012.append(t)
        if (str(dates[r])[2:6] == "2013"):
            year2013.append(t)
        if (str(dates[r])[2:6] == "2014"):
            year2014.append(t)




    year2011 = np.array(year2011)
    year2012 = np.array(year2012)
    year2013 = np.array(year2013)
    year2014 = np.array(year2014)

    avg2011 = np.average(year2011)
    avg2012 = np.average(year2012)
    avg2013 = np.average(year2013)
    avg2014 = np.average(year2014)

    np.set_printoptions(precision=1)
    print("the average  of Year 2011 is = ",avg2011)
    print("the average  of Year 2012 is = ", avg2012)
    print("the average  of Year 2013 is = ", avg2013)
    print("the average  of Year 2014 is = ", avg2014)
    avgs = np.array([avg2011,avg2012,avg2013,avg2014])
    print("the Hottest Year  is with average = ", np.amax(avgs))
    #dates1 = pd.DatetimeIndex(dates.flatten()) #['2010-10-17', '2011-05-13', "2012-01-15"])
    #YEAR2014 = np.empty(1)
    #filter = dates[0] == "2014"
    #YEAR2014 = dates1.where(filter )



getMaxOfWholePeriod()
getTheHottestYear()
#lsArray =  np.concatenate((temps,dates),axis=1)
