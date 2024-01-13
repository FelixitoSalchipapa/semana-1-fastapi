def suma(numero1: int, numero2: str):
    suma = numero1 + numero2

    if( suma % 2 == 0):
        print("El número es: ", suma)
        print("Es par")
    else:
        print("El número es: ", suma)
        print("Es impar")

a = int(input("Digite el primer número: "))
b = int(input("Digite el segundo número: "))

suma(a, b)

