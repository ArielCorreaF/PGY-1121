sw = 1

Cont_Entradas = 0  

Acum_Total = 0  

Cont_niño = 0  

Cont_Joven = 0  

Cont_Adulto = 0  

Total_Ganancia = 0

while sw == 1:
    print("-------------------------------------------------------------------------")
    print("Bienvenido al Cine Moro")
    print("1. Comprar entrada")
    print("2. ver cantidad total de entradas vendidas y el monto recaudado")
    print("3. Ver porcentaje de entradas vendidas")
    print("4. Salir")
    print("-------------------------------------------------------------------------")
    try:
        vOp = int(input("Seleccione una opción: "))
        if vOp == 1:
            print("CATEGORÍAS:")
            print("Niño [$5500] (1-13)")
            print("Joven [$7000] (14-21)")
            print("Adulto [$9000] (mayor a 22)")
            vcantidad = int(input("Ingrese la cantidad de entradas: "))
            print("---------------------------------")
            print("CATEGORÍAS:")
            print("Niño [$5500] (1-13)")
            print("Joven [$7000] (14-21)")
            print("Adulto [$9000] (mayor a 22)")
            vedad = int(input("ingresa tu edad: "))
            print("---------------------------------")
            print("CATEGORÍAS:")
            print("Niño [$5500] (1-13)")
            print("Joven [$7000] (14-21)")
            print("Adulto [$9000] (mayor a 22)")

            if vedad <= 13:
                subtotal = vcantidad * 5500
                Cont_niño += vcantidad
                print("categoria de entrada niño")
                print(f"cantidad de entradas {vcantidad}")
                print(f"total a pagar = {subtotal}")


          
            elif vedad >= 14 and vedad <= 21:
                subtotal = vcantidad * 7000
                Cont_Joven += vcantidad
                print("categoria de entrada joven")
                print(f"cantidad de entradas {vcantidad}")
                print(f"total a pagar = {subtotal}")

            elif vedad <= 22:
                subtotal = vcantidad * 9000
                Cont_Adulto += vcantidad
                print("categoria de entrada adulto")
                print(f"cantidad de entradas: {vcantidad}")
                print(f"total a pagar = {subtotal}")


            Cont_Entradas += vcantidad
            Acum_Total += subtotal

        elif vOp == 2:
            print("---------------------------------")
            print("Total del día")
            print("---------------------------------")
            print("Cantidad de entradas vendidas:", Cont_Entradas)
            print("Monto total recaudado: $", Acum_Total)

        elif vOp == 3:
            print("---------------------------------")
            print("Porcentaje del día")
            print("---------------------------------")
            print("Porcentaje de entradas por categoría:")
            total_entradas = Cont_niño + Cont_Joven + Cont_Adulto
            if total_entradas > 0:
                porcentaje_ni = (Cont_niño / total_entradas) * 100
                porcentaje_joven = (Cont_Joven / total_entradas) * 100
                porcentaje_adulto = (Cont_Adulto / total_entradas) * 100
                print("Niño:", porcentaje_ni, "%")
                print("Joven:", porcentaje_joven, "%")
                print("Adulto:", porcentaje_adulto, "%")
            else:
                print("No se han vendido entradas aún.")

        elif vOp == 4:
            sw = 0 

            
        else:
            print("Opción inválida")

    except ValueError:
        print("Opción inválida")

print("Gracias por su compra, disfrute la función.")