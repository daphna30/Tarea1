dia = int(input("Dia de nacimiento: "))
Mes_de_nacimiento = input("Mes de nacimiento: (marzo, julio, etc): ")

if Mes_de_nacimiento == "enero":
    if dia >= 20:
        print("Acuario")
    else:
        print("Capricornio")
elif Mes_de_nacimiento == "febrero":
    if dia>=19:
        print("Piscis")
    else:
        print("Acuario")
elif Mes_de_nacimiento == "marzo":
    if dia >= 21:
        print("Aries")
    else:
        print("Piscis")
elif Mes_de_nacimiento == "abril":
    if dia>=20:
        print("Tauro")
    else:
        print("Aries")
elif Mes_de_nacimiento == "mayo":
    if dia>=21:
        print("Geminis")
    else:
        print("Tauro")
elif Mes_de_nacimiento == "junio":
    if dia>=21:
        print("Cancer")
    else:
        print("Geminis")
elif Mes_de_nacimiento == "julio":
    if dia>=23:
        print("Leo")
    else:
        print("Cancer")
elif Mes_de_nacimiento == "agosto":
    if dia>=23:
        print("Virgo")
    else:
        print("Leo")
elif Mes_de_nacimiento == "septiembre":
    if dia>=23:
        print("Libra")
    else:
        print("Virgo")
elif Mes_de_nacimiento == "octubre":
    if dia>=23:
        print("Escorpio")
    else:
        print("Libra")
elif Mes_de_nacimiento == "noviembre":
    if dia>=22:
        print("Sagitario")
    else:
        print("Escorpio")
elif Mes_de_nacimiento == "diciembre":
    if dia>=22:
        print("Capricornio")
    else:
        print("Sagitario")
