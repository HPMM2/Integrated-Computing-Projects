import serial
import RPi.GPIO as GPIO
import time

ser = serial.Serial('/dev/ttyUSB0', 9600) # Puerto serial


ledPin = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)

try:
    while True:
        data = ser.readline().decode().strip()
        voltage, refVoltage = map(float, data.split(','))
        
        if voltage > refVoltage:
            GPIO.output(ledPin, GPIO.HIGH) # Encender
            print("Voltaje bajo")
        else:
            GPIO.output(ledPin, GPIO.LOW) # Apagar
            print("Voltaje normal")

        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
