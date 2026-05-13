import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import PhotoImage
from rpi_ws281x import PixelStrip, Color

# --------------------------------------------------- LED ----------------------------------------------------------
LED_COUNT = 32  
LED_PIN = 18     
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 255
LED_INVERT = False
LED_CHANNEL = 0

strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

def controlar_tira_led(intensidad, tipo_luz):
    # COLOR
    if tipo_luz == "Blanca/Natural":
        color = Color(255, 255, 255)  
    elif tipo_luz == "Calida":
        color = Color(255, 165, 0)  

    # BRILLO
    if intensidad == "Baja":
        strip.setBrightness(50)
    elif intensidad == "Media":
        strip.setBrightness(150)
    elif intensidad == "Alta":
        strip.setBrightness(255)

    # COMIENZO
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
    strip.show()
# ------------------------------------------------------------------------------------------------------------------




# -------------------------------------------------- TEMPORIZADOR --------------------------------------------------
# COMIENZO
def comenzar_temporizador():
    duracion_seleccionada = dropdown_duracion.get()
    duracion_segundos = obtener_segundos(duracion_seleccionada)
    intensidad_seleccionada = dropdown_intensidad.get()
    tipo_luz_seleccionada = dropdown_frecuencia.get()
    controlar_tira_led(intensidad_seleccionada, tipo_luz_seleccionada)
    ventana_temporizador(root, duracion_segundos)

# CONVERSOR
def obtener_segundos(duracion_seleccionada):
    duracion = duracion_seleccionada.split()[0]  # Extraer el número de la duración
    unidad_tiempo = duracion_seleccionada.split()[1]  # Extraer la unidad de tiempo
    if unidad_tiempo == "minutos":
        duracion_segundos = int(duracion) * 60
    elif unidad_tiempo == "hora":
        duracion_segundos = int(duracion) * 3600
    return duracion_segundos

# VENTANA
def ventana_temporizador(parent, segundos):
    ventana = tk.Toplevel()
    ventana.title("Temporizador")
    
    font_size = 300  
    tiempo_str = "00:00"  
    etiqueta_temporizador = tk.Label(ventana, text=tiempo_str, font=("Arial", font_size))
    etiqueta_temporizador.pack(pady=20)

    ventana_width = etiqueta_temporizador.winfo_reqwidth() + 20  
    ventana_height = etiqueta_temporizador.winfo_reqheight() + 40  
    
    x_position = (ventana.winfo_screenwidth() - ventana_width) // 2
    y_position = (ventana.winfo_screenheight() - ventana_height) // 2
    ventana.geometry(f"{ventana_width}x{ventana_height}+{x_position}+{y_position}")

    def temporizador_reversa(remaining_time):
        if remaining_time <= 0:
            etiqueta_temporizador.config(text="00:00")
            mostrar_alerta()
            ventana.destroy() 
        else:
            minutes, seconds = divmod(remaining_time, 60)
            etiqueta_temporizador.config(text="{:02d}:{:02d}".format(minutes, seconds))
            ventana.after(1000, temporizador_reversa, remaining_time - 1)

    # MENSAJE
    def mostrar_alerta():
        alerta = tk.Toplevel()
        alerta.title("¡Tiempo agotado!")

        label_alerta = tk.Label(alerta, text="¡Tiempo agotado!", font=("Arial", 100))
        label_alerta.pack(padx=20, pady=10)

        btn_aceptar = tk.Button(alerta, text="Aceptar", font=("Arial", 16), command=alerta.destroy)
        btn_aceptar.pack(pady=10)

    temporizador_reversa(segundos)
# ------------------------------------------------------------------------------------------------------------------




# ------------------------------------------------------ LOGO ------------------------------------------------------
def intro_logo(logo_velocidad, logo_mov, logo_duracion):
    global logo
    canvas.move(logo, 0, logo_mov)
    if canvas.coords(logo)[1] < logo_duracion:
        root.after(logo_velocidad, intro_logo, logo_velocidad, logo_mov, logo_duracion)
    else:
        root.after(500, fondo_gris)
# ------------------------------------------------------------------------------------------------------------------




# --------------------------------------------------- FONDO GRIS ---------------------------------------------------
def fondo_gris():
    # Limpiar la ventana
    canvas.delete("all")
    diseño_fondo()
    menu()

def diseño_fondo():
    alpha = 80
    fondo_imagen = Image.open("images/Fondo.png")
    fondo_imagen = fondo_imagen.convert("RGBA")
    fondo_imagen.putalpha(alpha)
    fondo_imagen = ImageTk.PhotoImage(fondo_imagen)
    canvas.create_image(canvas_width / 7, canvas_height / 7, anchor=tk.CENTER, image=fondo_imagen)
    canvas.fondo_imagen = fondo_imagen
# ------------------------------------------------------------------------------------------------------------------




# ------------------------------------------------------ MENU ------------------------------------------------------
def menu():
    global dropdown_duracion, dropdown_intensidad, dropdown_frecuencia
    canvas.create_text(canvas_width / 2, 80, text="Bienvenido!", font=("Arial", 100), fill="#1b1b1b")

    # - DURACION -----------------------------------------------------------------------------------------------
    label_duracion = tk.Label(root, text="Duración:", font=("Arial", 50))
    label_duracion.place(relx=0.3, rely=0.3, anchor=tk.CENTER)

    # Opciones de duración
    opciones_duracion = ["5 minutos", "10 minutos", "25 minutos", "30 minutos", "45 minutos", "1 hora"]
    selected_option_duracion = tk.StringVar()
    selected_option_duracion.set(opciones_duracion[0])
    dropdown_duracion = ttk.Combobox(root, textvariable=selected_option_duracion, values=opciones_duracion,
                                     font=("Arial", 35), state="readonly")
    dropdown_duracion.place(relx=0.7, rely=0.3, anchor=tk.CENTER)

    # Customizar
    style = ttk.Style()
    style.theme_use('clam')
    style.configure('Custom.TCombobox', padding=15, width=10, fieldbackground='#81e6e4', foreground='#000000',
                    bordercolor='#000000', arrowcolor='#81e6e4')
    style.map('Custom.TCombobox', background=[('active', '#000000')])
    dropdown_duracion.config(style='Custom.TCombobox')
    # ----------------------------------------------------------------------------------------------------------

    # - INTENSIDAD ---------------------------------------------------------------------------------------------
    label_intensidad = tk.Label(root, text="Intensidad:", font=("Arial", 50))
    label_intensidad.place(relx=0.3, rely=0.5, anchor=tk.CENTER)

    # Opciones de intensidad
    opciones_intensidad = ["Baja", "Media", "Alta"]
    selected_option_intensidad = tk.StringVar()
    selected_option_intensidad.set(opciones_intensidad[0])
    dropdown_intensidad = ttk.Combobox(root, textvariable=selected_option_intensidad, values=opciones_intensidad,
                                       font=("Arial", 35), state="readonly")
    dropdown_intensidad.place(relx=0.7, rely=0.5, anchor=tk.CENTER)

    # Customizar
    dropdown_intensidad.config(style='Custom.TCombobox')
    # ----------------------------------------------------------------------------------------------------------

    # - LUZ ---------------------------------------------------------------------------------------------
    label_frecuencia = tk.Label(root, text="Luz:", font=("Arial", 50))
    label_frecuencia.place(relx=0.3, rely=0.7, anchor=tk.CENTER)

    # Opciones de frecuencia
    opciones_frecuencia = ["Blanca/Natural", "Calida"]
    selected_option_frecuencia = tk.StringVar()
    selected_option_frecuencia.set(opciones_frecuencia[0])
    dropdown_frecuencia = ttk.Combobox(root, textvariable=selected_option_frecuencia, values=opciones_frecuencia,
                                       font=("Arial", 35), state="readonly")
    dropdown_frecuencia.place(relx=0.7, rely=0.7, anchor=tk.CENTER)

    # Customizar
    dropdown_frecuencia.config(style='Custom.TCombobox')
    # ----------------------------------------------------------------------------------------------------------

    # - COMENZAR -----------------------------------------------------------------------------------------------
    btn_comenzar = tk.Button(root, text="Comenzar", font=("Arial", 24), command=comenzar_temporizador)
    btn_comenzar.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
    # ----------------------------------------------------------------------------------------------------------

    # - SALIR --------------------------------------------------------------------------------------------------
    btn_salir = tk.Button(root, text="Salir", font=("Arial", 24), command=root.quit)
    btn_salir.place(relx=0.5, rely=0.9, anchor=tk.CENTER)
    # ----------------------------------------------------------------------------------------------------------

    # - TEMPORIZADOR -------------------------------------------------------------------------------------------
    global etiqueta_temporizador
    etiqueta_temporizador = tk.Label(root, text="", font=("Arial", 300))
    etiqueta_temporizador.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
    # ----------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------




# Definir opciones
logo_velocidad = 6  # Velocidad de la animación
logo_mov = 8  # Incremento de píxeles en cada movimiento
logo_duracion = 300  # Coordenada Y final de la animación




# ------------------------------------------------- LOGO ANIMACION -------------------------------------------------
root = tk.Tk()
root.attributes("-fullscreen", True)
root.title("Intro Animada")

ancho = root.winfo_screenwidth()
alto = root.winfo_screenheight()

canvas_width = ancho
canvas_height = alto
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack(expand=True, fill="both")

logo_image = PhotoImage(file="images/LOGO.png")
logo = canvas.create_image(canvas_width / 2, -130, anchor=tk.N, image=logo_image)

root.after(500, intro_logo, logo_velocidad, logo_mov, logo_duracion)
# ------------------------------------------------------------------------------------------------------------------

menu()

root.mainloop()
