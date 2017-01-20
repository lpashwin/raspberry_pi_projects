from sense_hat import SenseHat
sense=SenseHat()
sense.show_message("running sensors",scroll_speed=0.01)
temp=sense.get_temperature_from_humidity()
print("Temperature ={0:3.2f} C".format(sense.get_temperature()))
while(True):
#	print('Roll : {0:5.3f},Pitch : {1:5.3f},Yaw : {2:5.3f}'.format(sense.get_orientation().values()))
	print(sense.get_orientation().values())
