from gpiozero import LED, Button, MotionSensor, Buzzer
from signal import pause
import threading
import time

# ------------------------LEDS--------------------
led1 = LED(17)  
led2 = LED(27)
led3 = LED(22)
led4 = LED(10)
led5 = LED(9)

boton1 = Button(21)
boton2 = Button(20)
boton3 = Button(19)
ultimo_boton = None
# ------------------------PIR--------------------
pir_sensor = MotionSensor(4)

# ------------------------BUZZER--------------------
buzzer = Buzzer(11)
buzzer_activo = False

# ------------------------LEDS--------------------
def secuencia1():
    led1.off()
    led2.off()
    led3.off()
    led4.on()
    led5.on()


def secuencia2():
    led1.on()
    led2.on()
    led3.on()
    led4.off()
    led5.off()

    
    
def guardar_ultimo_boton(secuencia1):
    global ultimo_boton
    ultimo_boton = secuencia1
    
# ------------------------BUZZER--------------------
def secuencia_buzzer():
    global buzzer_activo
    while buzzer_activo:
        buzzer.on()
        time.sleep(5)  
        buzzer.off()
        time.sleep(2)

 
def apagar_buzzer():
    global buzzer_activo
    buzzer_activo = False
    buzzer.off()
    led1.off()
    led2.off()
    led3.off()
    led4.off()
    led5.off()
    

def encender_buzzer():
    global buzzer_activo
    buzzer_activo = True
    buzzer_thread = threading.Thread(target=secuencia_buzzer)
    buzzer_thread.start()  
    
# Asigna las acciones a los botones
boton1.when_pressed = lambda: guardar_ultimo_boton(secuencia1)
boton2.when_pressed = lambda: guardar_ultimo_boton(secuencia2)
boton3.when_pressed = lambda: apagar_buzzer()


# Detector de movimiento
def detectar_movimiento():
    if pir_sensor.motion_detected:
        print("¡Alarma! Movimiento detectado")
        if ultimo_boton:
            ultimo_boton()
        # ------------------------BUZZER--------------------
        if not buzzer_activo:
            encender_buzzer()
   
        
# Ejecuta la detección de movimiento en segundo plano
pir_sensor.when_motion = detectar_movimiento


# Mantén el programa en ejecución
pause()
