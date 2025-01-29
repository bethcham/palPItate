import time
import board
import busio
import adafruit_mprls

si7021_ADD = 0x18 #Add the I2C bus address for the sensor here

i2c = busio.I2C(board.SCL, board.SDA)
mpr = adafruit_mprls.MPRLS(i2c, psi_min=0, psi_max=25)

while True:
    print("Pressure (hPa):", mpr.pressure)
    time.sleep(0.1)