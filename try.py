from sense_hat import SenseHat
sense=SenseHat()
sense.show_message("Hello Viji, You are a monkey")
temp=sense.get_temperature_from_humidity()
print("Temperature =%s C" %temp)
