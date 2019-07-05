x = 13


n = int(input("Intente adivinar el numero: "))
while True:
    if n<x:
        print("Menor")
        n = int(input("Intente adivinar el numero: "))
    elif n>x:
        print("Mayor")
        n = int(input("Intente adivinar el numero: "))
    elif n==x:
        print("Felicidades! Adivinaste!")
        break
