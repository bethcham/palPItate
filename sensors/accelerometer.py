import time
import board
import busio
from adafruit_lis3dh import LIS3DH_I2Cs
i2c = busio.I2C(board.SCL, board.SDA)
lis3dh = LIS3DH_I2C(i2c)
print("Reading data")
try:
    while True:
        x, y, z = lis3dh.acceleration
        print(f"X: {x:.2f} m/s², Y: {y:.2f} m/s², Z: {z:.2f} m/s²")
        time.sleep(0.5)
except KeyboardInterrupt:
    print("stopped")
