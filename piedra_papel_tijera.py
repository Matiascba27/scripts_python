import random

print("¡Bienvenido al juego de Piedra, Papel o Tijera!")
print("Las reglas son simples: Piedra vence a Tijera, Tijera vence a Papel y Papel vence a Piedra.")
print("El juego se juega al mejor de 3 rondas. ¡Buena suerte!")

victorias_usuario = 0
victorias_computadora = 0
numero_rondas = 0

usuario = input("Por favor, ingresa tu nombre: ")
opciones = [1, 2, 3] # 1: Piedra, 2: Papel, 3: Tijera
decision = int(input("Elige tu opcion (1:Piedra, 2:Papel o 3:Tijera): "))


while decision not in opciones:
    print("Opción no válida. Por favor, elige 1:Piedra, 2:Papel o 3:Tijera.")
    