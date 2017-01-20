from sense_hat import SenseHat
import time
t=SenseHat()
to_print=['t','pitch','roll','yaw']
while(True):
   # '{0:16d},{1:5.3f},{2:5.3f},{3:5.3f}'.format([t.get_accelerometer()[item] for item in to_print])
#    print('{0:16.0f}{1:5.3f}{2:5.3f}{3:5.3f}'.format(t.get_accelerometer()[item] for item in to_print))
#    print('{0[0]:16.0f},{0[1]:9.5f},{0[2]:9.5f},{0[3]:9.5f}'.format([t.get_accelerometer()[tem] for tem in to_print]))
    print(time.time(),format(t.get_accelerometer()['pitch']))

