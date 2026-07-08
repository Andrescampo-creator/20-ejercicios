# Ingreso a una zona restringida
evacuacion = input("¿Hay un protocolo de evacuación activo? (si/no): ")
if evacuacion == "si":
    print("No puede ingresar.")
else:
    emergencia = input("¿Es personal de emergencia? (si/no): ")
    if emergencia == "si":
        print("Puede ingresar.")
    else:
        credencial = input("¿Tiene credencial autorizada? (si/no): ")
        if credencial == "si":
            biometria = input("¿La biometría fue validada? (si/no): ")
            if biometria == "si":
                horario = input("¿Está dentro del horario permitido? (si/no): ")
                if horario == "si":
                    print("Puede ingresar.")
                else:
                    print("No puede ingresar.")
            else:
                print("No puede ingresar.")
        else:
            print("No puede ingresar.")