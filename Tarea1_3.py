import math
# a = 4
# b = 14
# c = -5
# d = 2
# e = 4
# precio = None
# costo = 5.2
#
# # print(bin(0b101111 | 2) + " es 0b10111100")
# print(str(5 in [1, 2, 3]) + " es False")
# print(str(costo is None) + " es False")
# print(str(a - b) + " es -10")
# # print(bin(0b101111) + " es -0b110000")
# print(str(a / c) + " es -0.8")
# print(str(14 % 4) + " es 2")
# print(str(1 in [1, 2, 3]) + " es True")
# print(bin(0b101111 ^ 0b001101) + " es 0b100010")
# print(str(precio != None) + " es False")
# # print(str(c  a) + " es 3")
# print(str(4 == 4) + " es True")
# print(str(4/2 *  14) + " es 28")
# print(str(a-1 == 3) + " es True")
# print(str(4 - 14) + " es -10")
# print(str(b % a) + " es 2")
# print(str(-5 -1 + 4) + " es -2")
# print(str(a + b) + " es 18 ")
# print(str(4/-2 == -2) + " es True")
# print(str(5 not in [1, 2, 3]) + " es True")
# print(str(c -1 + a) + " es -2")
# print(str(a * d * 2) + " es 16")
# print(str(int(b -2) / a) + " es 3")
# print(str(4 / -5) + " es -0.8")
# print(str(4 * 14) + " es 56")
# print(str(a is not b) + " es True")
# print(bin(0b101111 & 0b001101) + " es 0b1101")
# print(str(True is False) + " es False")
# print(str(4 *2* 2) + " es 16")
# # print(bin(0b101111 + 3) + " es 0b101")
# print(str(-5 +4 + 4) + " es 3")
# print(str(a * b) + " es 56")
# print(str(1 not in [1, 2, 3]) + " es False")
# print(str(True is not False) + " es True")
# print(str(costo is not None) + " es True")
# print(str(True is True) + " es True")
# print(bin(0b101111 | 0b001101) + " es 0b101111")
# print(str(not False) + " es True")
# print(str(a == 4) + " es True")
# print(str(a == e) + " es True")
# print(str(precio is None) + " es True")
# print(str(False & False) + " es False")
# print(str((14-2)/ 4) + " es 3")
#
# x = 3
# print(str(x)+" es 3")
# x =  x - 100
# print(str(x)+" es -97")
# x = x + 110
# print(str(x)+" es 13")
# x = x ** 2
# print(str(x)+" es 169")
# x = x ** 0.5
# print(str(x)+" es 13")
# x = x * 2
# print(str(x)+" es 26")
# x = 5
# print(str(x)+" es 5")
# x = x % 2
# print(str(x)+" es 1")
#
# n = int(input("ingrese n: "))
# n = n + (n*10+n) + (n*100+n*10+n)
# print(n)
#
# n = int(input("Ingrese precio del item: "))
# itbis = n * 0.18
# print(itbis)
#
# radio = int(input("Ingrese el radio: "))
# altura = int(input("Ingrese la altura: "))
# volumen  = math.pi * math.pow(radio, 2) * altura
# print(volumen)

a = int(input("Ingrese a: "))
b = int(input("Ingrese b: "))
c = int(input("Ingrese c: "))
resultado1 = (-b + math.sqrt(math.pow(b,2) + (4*a*c)))/(2*a)
resultado2 = (-b - math.sqrt(math.pow(b,2) + (4*a*c)))/(2*a)
print(str(resultado1) + " " + str(resultado2))
# T1.3.5. Dado los coeficientes (a,b,c). Haz un programa que solucione una ecuación cuadrática (ax^2+bx+c=0).
