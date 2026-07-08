# Autorización de compra empresarial
proveedor = input("¿El proveedor está registrado? (si/no): ")
if proveedor == "no":
    print("Compra rechazada.")
else:
    valor = float(input("Ingrese el valor de la compra: "))
    if valor <= 500000:
        presupuesto = input("¿Tiene presupuesto disponible? (si/no): ")
        if presupuesto == "si":
            print("Compra aprobada.")
        else:
            print("Compra rechazada.")
    else:
        presupuesto = input("¿Tiene presupuesto disponible? (si/no): ")
        if presupuesto == "si":
            supervisor = input("¿Tiene aprobación del supervisor? (si/no): ")
            if supervisor == "si":
                print("Compra aprobada.")
            else:
                print("Compra rechazada.")
        else:
            print("Compra rechazada.")