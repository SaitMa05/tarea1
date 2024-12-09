import random

numeroAleatorio = random.randint(1, 10)

print("Adivina el número que estoy pensando entre 1 y 10")

intento = None

while intento != numeroAleatorio:
    try:
            intento = int(input("Introduce tu número: "))
            if intento < numeroAleatorio:
                print("El número es más alto. Inténtalo de nuevo.")
            elif intento > numeroAleatorio:
                print("El número es más bajo. Inténtalo de nuevo.")
            else:
                print("¡Felicidades! Adivinaste el número.")
    except ValueError:
            print("Por favor, introduce un número entero.")