import serial
import RPi.GPIO as GPIO

arduino_port = '/dev/ttyUSB0'  # Puerto serial 
baud_rate = 9600
ser = serial.Serial(arduino_port, baud_rate)

# Configura el pin del LED
led_pin = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

def leer_temperatura():
    temperatura_str = ser.readline().strip().decode('utf-8')
    return float(temperatura_str)

def controlar_led(temperatura_umbral):
    temperatura_actual = leer_temperatura()
    if temperatura_actual >= temperatura_umbral:
        GPIO.output(led_pin, GPIO.HIGH)  # Enciende el LED
        print("Sobrecarga de temperatura:", temperatura_actual, "C")
    else:
        GPIO.output(led_pin, GPIO.LOW)   # Apaga el LED
        print("Temperatura normal", temperatura_actual, "C")

# Temperatura umbral
temperatura_umbral = 25 


try:
    while True:
        controlar_led(temperatura_umbral)
except KeyboardInterrupt:
    GPIO.cleanup()  
