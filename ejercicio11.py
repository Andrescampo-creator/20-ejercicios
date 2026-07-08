# Habilitación de un vehículo institucional
comparendos = input("¿Tiene comparendos pendientes? (si/no): ")
if comparendos == "si":
    print("No puede usar el vehículo.")
else:
    emergencia = input("¿Es conductor de emergencia autorizado? (si/no): ")
    if emergencia == "si":
        print("Puede usar el vehículo.")
    else:
        licencia = input("¿Tiene licencia vigente? (si/no): ")
        if licencia == "si":
            revision = input("¿Aprobó la revisión de seguridad? (si/no): ")
            if revision == "si":
                combustible = input("¿El vehículo tiene combustible suficiente? (si/no): ")
                if combustible == "si":
                    print("Puede usar el vehículo.")
                else:
                    print("No puede usar el vehículo.")
            else:
                print("No puede usar el vehículo.")
        else:
            print("No puede usar el vehículo.")