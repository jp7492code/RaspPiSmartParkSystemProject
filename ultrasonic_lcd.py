import RPi.GPIO as GPIO
import time
from RPLCD.i2c import CharLCD

# GPIO pins
TRIG = 16
ECHO = 20
PIN_RED = 7     # The Raspberry Pi GPIO pin connected to the R pin of the traffic light module
PIN_YELLOW = 8  # The Raspberry Pi GPIO pin connected to the Y pin of the traffic light module
PIN_GREEN = 25  # The Raspberry Pi GPIO pin connected to the G pin of the traffic light module

# Time durations for lights (not used in this context, but defined for clarity)
RED_TIME = 2     # RED light duration in seconds
YELLOW_TIME = 1  # YELLOW light duration in seconds
GREEN_TIME = 2   # GREEN light duration in seconds

# Define indices for light states
RED = 0
YELLOW = 1
GREEN = 2

# Create lists for pins
pins = [PIN_RED, PIN_YELLOW, PIN_GREEN]

# Initialize the LCD (adjust I2C address if necessary using i2cdetect)
lcd = CharLCD('PCF8574', 0x27, cols=16, rows=2)

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(PIN_RED, GPIO.OUT)
GPIO.setup(PIN_YELLOW, GPIO.OUT)
GPIO.setup(PIN_GREEN, GPIO.OUT)

def traffic_light_on(light):
    """Turn on the corresponding traffic light and turn off others."""
    for i in range(len(pins)):
        GPIO.output(pins[i], GPIO.HIGH if i == light else GPIO.LOW)

try:
    while True:
        # Trigger the sensor
        GPIO.output(TRIG, True)
        time.sleep(0.00001)  # 10 microseconds pulse
        GPIO.output(TRIG, False)

        # Measure the time for the echo
        while GPIO.input(ECHO) == 0:
            pulse_start = time.time()

        while GPIO.input(ECHO) == 1:
            pulse_end = time.time()

        # Calculate distance
        pulse_duration = pulse_end - pulse_start
        distance_cm = pulse_duration * 17150  # Convert to cm
        distance_in = distance_cm * 0.393701  # Convert cm to inches
        distance_in = round(distance_in, 2)

        # Determine parking status and traffic light color
        if distance_in < 2:  # Car is parked
            status = "The car has been parked"
            traffic_light_on(GREEN)
        elif 2 <= distance_in <= 3:  # Car is close
            status = "The car is near parking"
            traffic_light_on(YELLOW)
        else:  # Car is far
            status = "The car has not been parked"
            traffic_light_on(RED)

        # Print to console
        print(f"Distance: {distance_in:.2f} in - {status}")

        # Display on the LCD
        lcd.clear()
        lcd.write_string(f"Distance: {distance_in:.2f} in")
        lcd.crlf()
        lcd.write_string(status)

        # Wait before the next measurement
        time.sleep(1)

except KeyboardInterrupt:
    print("Measurement stopped by user.")

finally:
    # Clear LCD and reset GPIO pins
    lcd.clear()
    GPIO.cleanup()
