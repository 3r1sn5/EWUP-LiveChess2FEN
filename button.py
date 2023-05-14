import RPi.GPIO as GPIO
import time
import subprocess

# Button Initialize
button_pin = 18


def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(button_pin, GPIO.IN)
    count = 0;
    
    print("Starting LC2F, Press CTRL+C to exit")
    try:
        while True:
            value = GPIO.input(button_pin)
            if value == GPIO.LOW:
                count += 1 
                print("System Status : Taking picture...")
                cmd = "nvgstcapture-1.0 --image-res=2 -A --capture-auto >/dev/null 2>&1"
                start = time.perf_counter()
                subprocess.run(cmd.split(), check=True, stderr=subprocess.DEVNULL)
                elapsed_time = time.perf_counter() - start
                print(f"Elapsed time taking picture: {elapsed_time}")
                print(f"#{count} Predictions")
                print("Activating LC2F process")
                subprocess.run(["python3", "lc2fen.py", "-o", "predictions/test1.jpg", "BL"])
    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    main()

