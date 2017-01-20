#!/usr/bin/python
#
# 
# Measure distance using an ultrasonic module HC-SR04
# using a class
#
# Author : Ashwin Parambath
# Date   : 29/01/2016

# -----------------------
# Import required Python libraries
# -----------------------
import time
import RPi.GPIO as GPIO
import numpy as np 
 
# settle time, time before restarting reading
s_time=0.001

class distance():
    
    def __init__(self,TRIGGER_PIN,ECHO_PIN,pin_num=GPIO.BCM):
        # Trigger and echo pins set
        self.__GPIO_TRIGGER=TRIGGER_PIN
        self.__GPIO_ECHO=ECHO_PIN
        GPIO.setmode(pin_num)
        GPIO.setup(self.__GPIO_TRIGGER,GPIO.OUT)  # Trigger
        GPIO.setup(self.__GPIO_ECHO,GPIO.IN)      # Echo
        # Set trigger to False (Low) initially
        GPIO.output(self.__GPIO_TRIGGER, False)

    def read_sensor(self,distance_factor= 34300):
        '''
        This function measures the distance by triggering
        the trigger pins and reading data from the echo pin 
        Inputs
        ------
        Optional:
        distance factor : factor used to calibrate the distance
                          measurement
        '''
        GPIO.output(self.__GPIO_TRIGGER, True)
        time.sleep(0.00001)
        GPIO.output(self.__GPIO_TRIGGER, False)
        start = time.time()
        while GPIO.input(self.__GPIO_ECHO)==0:
            start = time.time()
        while GPIO.input(self.__GPIO_ECHO)==1:
            stop = time.time()
        elapsed = stop-start
        distance = (elapsed * distance_factor)/2
        return distance

    def read_distance(self,interval=0.001,\
        num_points=3,std_flag=True,max_std=0):
        '''
        Function to measure the average of num_points
        to improve accuracy. It also checks the standard 
        deviation to ensure that data points are not too 
        far off
        Inputs
        ------
        
        Optional
        num_points : Number of points over which to average
                   : default = 3
        std_flag   : Flag to ensure that standard deviation check
                     is enabled
                   : default = True 
        max_std    : Maximum standard deviation permissible
                   : default = -1
        '''
        distance_val=[]
        for ii in range(num_points):
            distance_val.append(self.read_sensor())
            time.sleep(interval)
        
        distance_array=np.array(distance_val)
        skip_flag=True
        if std_flag and max_std:
            if distance_array.std()<max_std:
                #return distance_array.mean()
               	skip_flag=False
            else: 
                #print(distance_array,distance_array.std())
                #return distance_array.mean()
                pass
        else:
            if std_flag:
                print('Please provide max_std value')
                # Raise an error here
            else:
                # this part can be skipped 
                #print('Std=',distance_array.std())
                #return distance_array.mean()
                pass
        return skip_flag,distance_array.mean(),distance_array.std()

    def cleanup(self):
        GPIO.cleanup()


if __name__=='__main__':
    i=0
    D_sensor1=distance(TRIGGER_PIN=18,ECHO_PIN=23)
    try:

        while True:

            i+=1 
            skip,distance,std = D_sensor1.read_distance(num_points=20,max_std=3,interval=.01)
            if not skip: 
	        print("{0} {1:8.2f}".format(i,distance))
            

    except KeyboardInterrupt:
        # User pressed CTRL-C
        # Reset GPIO settings
        D_sensor1.cleanup()
