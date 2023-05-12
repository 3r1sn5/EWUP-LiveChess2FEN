import RPi.GPIO as GPIO
import time

# Set up the button pin
button_pin = 18


def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(button_pin, GPIO.IN)
    prevValue = None

    print("Starting LC2F, Press CTRL+C to exit")
    try:
        while True:
            value = GPIO.input(button_pin)
            if value != prevValue:
                if value == GPIO.LOW:
                    value_str = "Taking picture..."
                else:
                    value_str = "System IDLE..."
            print("System Status : ", value_str)
            prevValue = None
            time.sleep(1)
    finally:
        GPIO.cleanup()


if _name_ == '_main_':
    main()