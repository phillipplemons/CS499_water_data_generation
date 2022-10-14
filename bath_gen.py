import json
from datetime import datetime as dt
from datetime import timedelta

total_water = 0

def take_bath(time, file):
     # total water var and incremental var
    global total_water
    shower_gal_per_min = 2.5

    # adding initial value to csv
    #file.write('Bathroom, Bath, ' + time.strftime(timeFormat) + ', ' + str(shower_gal_per_min) + ' gallons total,' + ' production\n') 

    # looping to update total water throught duration of shower
    for i in range(720): # shower duration 12 mins (12*60)
        time += timedelta(seconds=30)  # updating data every 30 seconds
        total_water += (shower_gal_per_min/2) # updating water accordingly
        # adding to csv
        file.write('Bathroom, Bath, ' + time.strftime(timeFormat) + ', ' + str(shower_gal_per_min) + ', production\n') 
    return time








if __name__ == '__main__':

    f = open("bath_data.csv", "w")
    timeFormat = "%m/%d/%Y %H:%M:%S"

    # start seven days in the past
    startTime = dt.now() - timedelta(days=7)
    endTime = dt.now()
    currentTime = startTime

    # looping through past 7 days
    while currentTime < endTime:
        
        # setting today to 7 days ago
        day = currentTime.weekday()



        # M - F
        if day in [0,1,2,3,4]:
            # taking a bath
            if (currentTime.hour in [9, 11]) and (currentTime.minute == 00): # two times a day
                currentTime = take_bath(currentTime, f)
            
            else:
                f.write('Bathroom, Bath, ' + currentTime.strftime(timeFormat) + ', ' + '0' + ', production\n') 
       
 
        # S - S 
        if day in [5,6]:
            # taking a bath
            if (currentTime.hour in [9, 11, 13]) and (currentTime.minute == 00): # 3 times a day
                currentTime = take_bath(currentTime, f)
            else:
                f.write('Bathroom, Bath, ' + currentTime.strftime(timeFormat) + ', ' + '0' + ', production\n') 





            
        currentTime += timedelta(seconds=1)
    f.close()


