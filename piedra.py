import tkinter as tk
from tkinter import messagebox
import random

def obtener_eleccion_computadora():
    return random.choice(["piedra", "papel", "tijera"])

def determinar_ganador(usuario, computadora):
    if usuario == computadora:
        return "Empate"
    elif (usuario == "piedra" and computadora == "tijera") or \
         (usuario == "papel" and computadora == "piedra") or \
         (usuario == "tijera" and computadora == "papel"):
        return "Ganaste"
    else:
        return "Perdiste"

def jugar(eleccion_usuario):
    eleccion_computadora = obtener_eleccion_computadora()
    resultado = determinar_ganador(eleccion_usuario, eleccion_computadora)
    resultado_label.config(text=f"Tu elegiste: {eleccion_usuario}\nLa computadora eligió: {eleccion_computadora}\nResultado: {resultado}")
    messagebox.showinfo("Resultado", f"Tu elegiste: {eleccion_usuario}\nLa computadora eligió: {eleccion_computadora}\nResultado: {resultado}")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Piedra, Papel o Tijera")
ventana.geometry("400x300")
ventana.config(bg="#ADD8E6")

# Etiqueta de bienvenida
bienvenida_label = tk.Label(ventana, text="Bienvenido al juego de piedra, papel o tijera", font=("Helvetica", 16), bg="#ADD8E6")
bienvenida_label.pack(pady=20)

# Frame para los botones
frame_botones = tk.Frame(ventana, bg="#ADD8E6")
frame_botones.pack(pady=20)

# Botones para las elecciones del usuario
boton_piedra = tk.Button(frame_botones, text="Piedra", font=("Helvetica", 14), command=lambda: jugar("piedra"))
boton_piedra.grid(row=0, column=0, padx=10)

boton_papel = tk.Button(frame_botones, text="Papel", font=("Helvetica", 14), command=lambda: jugar("papel"))
boton_papel.grid(row=0, column=1, padx=10)

boton_tijera = tk.Button(frame_botones, text="Tijera", font=("Helvetica", 14), command=lambda: jugar("tijera"))
boton_tijera.grid(row=0, column=2, padx=10)

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(ventana, text="", font=("Helvetica", 14), bg="#ADD8E6")
resultado_label.pack(pady=20)

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()
