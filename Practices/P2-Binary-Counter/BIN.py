import RPi.GPIO as GPIO
import time

LEDS = [2, 3, 4, 17, 27, 22, 10, 9]

def setup_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LEDS, GPIO.OUT)

def mostrar_numero_binario(numero):
    binario = bin(numero)[2:].zfill(8)
    for i in range(8):
        GPIO.output(LEDS[i], int(binario[i]))

def main():
    try:
        setup_gpio()
        
        # Bucle de 0 a 255
        for i in range(256):
            print("Número decimal:", i)
            mostrar_numero_binario(i)
            time.sleep(1)  # Espera 1 segundo

    finally:
        GPIO.cleanup()
        print("Programa finalizado.")

if __name__ == "__main__":
    main()
