import json
from datetime import datetime as dt
from datetime import timedelta

total_water = 0

def clothes_washer(time, file):
    
    # total water var and incremental var
    global total_water
    gal_per_min = 1.5

    # looping to update total water throught duration of shower
    for i in range(1200): # clothes cycle duration 20 mins (20*60)
        time += timedelta(seconds=1)  # updating data every second
        total_water += (gal_per_min/60) # updating water total accordingly
        # adding to csv
        file.write('Kitchen, Clothes Washer, ' + time.strftime(timeFormat) + ', ' + str(gal_per_min) + ', production\n') 
    return time






if __name__ == '__main__':

    f = open("clothes_data.csv", "w")
    timeFormat = "%m/%d/%Y %H:%M:%S"

    # start seven days in the past
    startTime = dt.now() - timedelta(days=7)
    endTime = dt.now()
    currentTime = startTime

    # loopng through past 7 days
    while currentTime < endTime:
        
        # setting today to 7 days ago
        day = currentTime.weekday()


        # M - F
        if day in [0,1,2,3]:
            # running dishwasher
            if (currentTime.hour == 16) and (currentTime.minute == 00): # two times a day
                currentTime = clothes_washer(currentTime, f)
            else:
                f.write('Kitchen, Clothes Washer, ' + currentTime.strftime(timeFormat) + ', ' + '0'  + ', production\n') 
       
 
            
        currentTime += timedelta(seconds=1)
    f.close()



