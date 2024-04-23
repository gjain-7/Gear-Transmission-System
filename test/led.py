from gpiozero import LED
from time import sleep

# Create an instance of the LED class for pin 17
leds = [LED(6), LED(19), LED(13), LED(26), LED(21)]

cnt = 0
while True: # Run forever
    leds[cnt].on()
    sleep(0.5)
    leds[cnt].off()
    cnt  = (cnt + 1) % 5

