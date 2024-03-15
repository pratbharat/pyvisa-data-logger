import os
import pyvisa
import csv
import time
import matplotlib.pyplot as plt


with open('example.csv', 'w', newline='') as file:
    # Create a CSV writer object
    csv_writer = csv.writer(file)

    # Write a single row of data
    csv_writer.writerow(["Time", "Channel1", "Channel2","Channel3" ])

#variable definitions
multimeter = pyvisa.ResourceManager().open_resource('GPIB0::1::INSTR')
startTime = time.time()

timeList = [[] for i in range(3)]
temperatureList = [[] for _ in range (3)]
print(timeList[0])
channels = [101, 102, 103]
iteration=0
while True:
    i=0
    for channel in channels:
        multimeter.write(":ROUTe:CLOSe (@{})".format(channel))
        multimeter.write(":SENSe:FUNCtion 'TEMPerature'")
        temperatureReading = float(multimeter.query(':SENSe:DATA:FRESh?').split(',')[0][:-2])
        #print(temperatureReading)
        temperatureList[i].append(temperatureReading)
        timeList[i].append(float(time.time() - startTime))
        #print(timeList[0])
        i=i+1
    with open('example.csv', 'a',newline='') as file:
        # Create a CSV writer object
        csv_writer = csv.writer(file)    
        csv_writer.writerow([float(time.time() - startTime), temperatureList[0][iteration], temperatureList[1][iteration],temperatureList[2][iteration] ])
    print([float(time.time() - startTime), temperatureList[0][iteration], temperatureList[1][iteration],temperatureList[2][iteration] ])
    iteration=iteration+1
    time.sleep(2)
    
