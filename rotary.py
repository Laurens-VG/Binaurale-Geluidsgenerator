from RPi import GPIO
from time import sleep

clk = 20
dt = 21
btn = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
counter = 0
clkLastState = GPIO.input(clk)
btnLastState = GPIO.input(btn)

try:

        while True:
                clkState = GPIO.input(clk)
                dtState = GPIO.input(dt)
                btnState = GPIO.input(btn)
                if btnState != btnLastState and btnState != 1:
                        print("Push")
                if clkState != clkLastState:
                        if dtState != clkState:
                                counter += 1
                        else:
                                counter -= 1
                        print(counter)
                clkLastState = clkState
                btnLastState = btnState
                sleep(0.01)
finally:
        GPIO.cleanup()