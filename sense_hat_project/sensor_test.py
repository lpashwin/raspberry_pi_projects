from sense_hat import SenseHat
import RTIMU
t=SenseHat()
while(True):
    print(t._imu.getIMUData())
    #print(t._imu.getIMUData(),t.get_accelerometer_raw())
