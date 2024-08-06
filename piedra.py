import random

def obtener_eleccion_usuario():
   eleccion = input("Elige piedra, papel o tijera ").lower()
   while eleccion not in ["piedra", "papel", "tijera"]:
      print("Elección inválida. Intente de nuevo.")
      eleccion = input("Elige piedra, papel o tijera").lower()
   return eleccion

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

def jugar():
   print("Bienvenido al juego de piedra papel o tijera")
   usuario = obtener_eleccion_usuario()
   computadora = obtener_eleccion_computadora()
   print(f"Tu elegiste: {usuario}")
   print(f"La computadora eligió: {computadora}")
   resultado = determinar_ganador(usuario, computadora)
   print(f"Resultado: {resultado}")

if __name__ == "__main__":
   jugar()