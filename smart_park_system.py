
import RPi.GPIO as GPIO
import time
from RPLCD.i2c import CharLCD

# GPIO pins
TRIG = 16
ECHO = 20

# Initialize the LCD (adjust I2C address if necessary using i2cdetect)
lcd = CharLCD('PCF8574', 0x27, cols=16, rows=2)

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

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

        # Determine parking status
        if distance_in < 2:  # Adjust threshold to 2 inches
            status = "The car has been parked"
        else:
            status = "The car has not been parked"

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
    lcd.clear()  # Clear the LCD
    GPIO.cleanup()  # Reset GPIO pins
