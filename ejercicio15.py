# Activación de un descuento corporativo
promociones = input("¿Intenta combinar promociones no acumulables? (si/no): ")
if promociones == "si":
    print("No recibe el descuento.")
else:
    codigo = input("¿Tiene un código promocional vigente? (si/no): ")
    if codigo == "si":
        print("Recibe el descuento.")
    else:
        empresa = input("¿Pertenece a una empresa aliada? (si/no): ")
        if empresa == "si":
            identificacion = input("¿Presenta identificación laboral? (si/no): ")
            if identificacion == "si":
                compra = float(input("Ingrese el valor de la compra: "))
                if compra > 100000:
                    print("Recibe el descuento.")
                else:
                    print("No recibe el descuento.")
            else:
                print("No recibe el descuento.")
        else:
            print("No recibe el descuento.")