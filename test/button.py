from gpiozero import Button
from signal import pause
import time

# Define the pin numbers for the buttons
button1_pin = 16
button2_pin = 20

# Create instances of the Button class for each button
button1 = Button(button1_pin)
button2 = Button(button2_pin)

speed = 10

# Define functions to be called when each button is pressed
while True:
    # Check if each button is pressed
    if button1.is_pressed:
        speed += 0.1
    if button2.is_pressed:
        speed -= 0.05

    print(f"\rSpeed: {speed:.2f}", end="", flush=True)
        # Wait for 1 ms before checking again
    time.sleep(0.1)


# Keep the program running
pause()

