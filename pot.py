import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1115(i2c)

# Create single-ended input on channel 0
chan1 = AnalogIn(ads, ADS.P1)
chan2 = AnalogIn(ads, ADS.P2)
chan3 = AnalogIn(ads, ADS.P3)

# Create differential input between channel 0 and 1
#chan = AnalogIn(ads, ADS.P1, ADS.P2)

print("{:>5}\t{:>5}".format('raw', 'v'))

while True:
    print("")
    print("****************")
    print("Pin 1: ", chan1.voltage)
    print("Pin 2: ", chan2.voltage)
    print("Pin 3: ", chan3.voltage)
    print("****************")
    print("")
    time.sleep(0.5)
