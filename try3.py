from sense_hat import SenseHat
from time import gmtime,strftime
sense=SenseHat()
#sense.show_message("running sensors",scroll_speed=0.01)
temp=sense.get_temperature_from_humidity()
print("Temperature ={0:3.2f} C".format(sense.get_temperature()))
while(True):
    pitch, roll, yaw=sense.get_orientataion().values()	
    print(strftime('%H:%M:%S',gmtime()),pitch,roll,way)
