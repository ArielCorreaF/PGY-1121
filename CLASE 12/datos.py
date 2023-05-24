print("INGRESA DATOS")
print("-------------------------")
vnom = input("ingresa tu nombre: ")
while True:
    try:
        vedad = input("ingrese su edad: ")
        break
    except:
        print("error de ingreso")    
print("-------------------------")
print(f"tu nombre es {vnom}")
print(f"tu edad es {vedad}")
print("programa finalizado")