# Autorización de salida de menores
restriccion = input("¿Tiene restricción médica activa? (si/no): ")
if restriccion == "si":
    print("No puede salir.")
else:
    acudiente = input("¿El acudiente lo acompaña? (si/no): ")
    if acudiente == "si":
        print("Puede salir.")
    else:
        permiso = input("¿Tiene permiso firmado? (si/no): ")
        if permiso == "si":
            lista = input("¿Aparece en la lista oficial? (si/no): ")
            if lista == "si":
                seguro = input("¿Cuenta con seguro vigente? (si/no): ")
                if seguro == "si":
                    print("Puede salir.")
                else:
                    print("No puede salir.")
            else:
                print("No puede salir.")
        else:
            print("No puede salir.")