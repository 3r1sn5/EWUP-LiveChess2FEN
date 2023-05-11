import Jeston.GPIO as GPIO

# Set up the GPIO pin numbering
GPIO.setmode(GPIO.BCM)

# Set up the button pin
button_pin = 20
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Define a callback function to run when the button is pressed
def button_callback(channel):
    print("Number:", channel)

# Detect button presses using interrupts
GPIO.add_event_detect(button_pin, GPIO.FALLING, callback=button_callback, bouncetime=200)

# Keep the script running
while True:
    pass
