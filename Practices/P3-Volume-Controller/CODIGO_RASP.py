import serial
import time
import RPi.GPIO as GPIO

# Definir los pines GPIO para los segmentos
segmentos = {
    'A': 2,
    'B': 3,
    'C': 4,
    'D': 17,
    'E': 27,
    'F': 22,
    'G': 10,
    'DP': 9  # Punto decimal (si tu display lo tiene)
}

# Definir los números de 0 a 9 en formato de segmentos
numeros = {
    0: ['G'],
    1: ['A', 'D', 'E', 'F', 'G'], 
    2: ['C', 'F'], 
    3: ['F', 'D'],
    4: ['A', 'D', 'E'],
    5: ['B', 'D'], 
    6: ['B'], 
    7: ['D', 'E', 'F','G'],
    8: [], 
    9: ['D'] 
}

# Definir los pines GPIO para los LEDs
led_pins = [11, 5, 6, 13, 19, 26, 21, 20, 16]

# Configuración de la comunicación serial
ser = serial.Serial('/dev/ttyUSB0', 9600)  # Ajusta '/dev/ttyUSB0' al puerto serial correcto
ser.flush()

# Configuración de los pines GPIO
GPIO.setmode(GPIO.BCM)
for seg_pin in segmentos.values():
    GPIO.setup(seg_pin, GPIO.OUT)
    GPIO.output(seg_pin, GPIO.LOW)
for led_pin in led_pins:
    GPIO.setup(led_pin, GPIO.OUT)
    GPIO.output(led_pin, GPIO.LOW)

try:
    while True:
        # Leer la línea de la comunicación serial
        line = ser.readline().decode('utf-8').rstrip()
        
        # Verificar si se recibió una línea válida
        if line:
            valor_analogico = int(line)  # Convertir el valor a entero
            
            # Dividir el valor en rangos de 10 y limitarlo entre 0 y 9
            valor_display = max(0, min(9, valor_analogico // 10))
            
            # Mostrar el número en el display de 7 segmentos
            for segmento, seg_pin in segmentos.items():
                if segmento in numeros[valor_display]:
                    GPIO.output(seg_pin, GPIO.HIGH)
                else:
                    GPIO.output(seg_pin, GPIO.LOW)
            
            # Encender los LEDs según el nivel del potenciómetro
            for i in range(valor_display):
                GPIO.output(led_pins[i], GPIO.HIGH)
            for i in range(valor_display, len(led_pins)):
                GPIO.output(led_pins[i], GPIO.LOW)
        
        time.sleep(0.01)  # Pequeña pausa para evitar leer demasiado rápido
except KeyboardInterrupt:
    ser.close()
    GPIO.cleanup()
