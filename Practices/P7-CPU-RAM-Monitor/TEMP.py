import RPi.GPIO as GPIO
import psutil
import time
import serial

led_amarillo_pin = 6 
led_rojo_pin = 13
led_verde1_pin = 12
led_verde2_pin = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_amarillo_pin, GPIO.OUT)
GPIO.setup(led_rojo_pin, GPIO.OUT)
GPIO.setup(led_verde1_pin, GPIO.OUT)
GPIO.setup(led_verde2_pin, GPIO.OUT)

GPIO.output(led_verde1_pin, GPIO.HIGH)
GPIO.output(led_verde2_pin, GPIO.HIGH)

arduino_port = '/dev/ttyUSB0'  # Puerto serial 
baud_rate = 9600
ser = serial.Serial(arduino_port, baud_rate)

def obtener_porcentaje_uso_cpu():
    return psutil.cpu_percent(interval=1)

def obtener_porcentaje_uso_ram():
    return psutil.virtual_memory().percent

def leer_temperatura():
    try:
        ser.write(b'r')  
        temperatura_str = ser.readline().strip().decode('utf-8')
        return float(temperatura_str)
    except Exception as e:
        print("Error al leer la temperatura:", e)
        return None

def controlar_leds():
    porcentaje_cpu = obtener_porcentaje_uso_cpu()
    porcentaje_ram = obtener_porcentaje_uso_ram()
    temperatura = leer_temperatura()

    if temperatura is not None:
        print("Temperatura:", temperatura, "°C")

    print("Uso del CPU:", porcentaje_cpu, "%")
    print("Uso de la RAM:", porcentaje_ram, "%")

    if porcentaje_cpu >= 65:
        GPIO.output(led_amarillo_pin, GPIO.HIGH)
    else:
        GPIO.output(led_amarillo_pin, GPIO.LOW)

    if porcentaje_ram >= 60:
        GPIO.output(led_rojo_pin, GPIO.HIGH)
    else:
        GPIO.output(led_rojo_pin, GPIO.LOW)

    if porcentaje_cpu > 80 or porcentaje_ram > 80:
        GPIO.output(led_verde1_pin, GPIO.LOW)
        GPIO.output(led_verde2_pin, GPIO.LOW)
    else:
        GPIO.output(led_verde1_pin, GPIO.HIGH)
        GPIO.output(led_verde2_pin, GPIO.HIGH)        

try:
    while True:
        controlar_leds()
        time.sleep(2) 
except KeyboardInterrupt:
    GPIO.cleanup()
