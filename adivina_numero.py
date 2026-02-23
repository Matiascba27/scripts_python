# importamos librerias
import random
#from colorama import init, Fore, Style, Back

#init(autoreset=True)

def adivina_numero():
    try:
        numero_secreto = random.randint(0, 100)
        max_intentos = 12
        intentos = 0
        adivinado = False
        usuario = input("Ingresa tu nombre: ")

        print(f"\nBienvenido {usuario} al juego de adivinar el numero!")
        print(f"\nEl juego es simple, tienes que adivinar un numero entre 0 y 100 \nTienes {max_intentos} de intentos")
        print("\nCada vez que adivines un numero, te dire si es mayor o menor al numero secreto")
        print("\nEstas listo? Vamos a empezar!")

        while not adivinado and intentos < max_intentos:
                try:
                    adivina = int(input("\nIngresa el numero entre 0 y 100: "))
                    
                except ValueError:
                    print("\nPor favor, ingresa un numero valido.")
                    continue
                
                if adivina < 1 or adivina > 100:
                    print("\nFuera de rango")
                    continue

                intentos += 1

                if adivina == numero_secreto:
                    adivinado = True
                    print(f"\nFelicidades! Has adivinado el numero en {intentos} intentos")
                elif adivina < numero_secreto:
                    print("\nEl numero secreto es mayor")
                else:
                    print("\nEl numero secreto es menor")
                
                if not adivinado and intentos == max_intentos:
                    print(f"\nLo siento, has agotado tus {max_intentos} intentos. El numero secreto era: {numero_secreto}")
                    print("\nMejor suerte la proxima vez!")
                    print("\nGame Over")
                    break
            
        return intentos

    except KeyboardInterrupt:
            print("\nJuego interrumpido por el usuario. ¡Hasta luego!")

if __name__ == "__main__":
    adivina_numero()
