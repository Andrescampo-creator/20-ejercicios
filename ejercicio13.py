# Acceso a un laboratorio especializado
alerta = input("¿Hay una alerta de seguridad activa? (si/no): ")
if alerta == "si":
    print("No puede ingresar.")
else:
    instructor = input("¿Es el instructor responsable del laboratorio? (si/no): ")
    if instructor == "si":
        print("Puede ingresar.")
    else:
        induccion = input("¿Aprobó la inducción de seguridad? (si/no): ")
        if induccion == "si":
            proteccion = input("¿Usa los elementos de protección requeridos? (si/no): ")
            if proteccion == "si":
                reserva = input("¿Tiene reserva confirmada? (si/no): ")
                if reserva == "si":
                    print("Puede ingresar.")
                else:
                    print("No puede ingresar.")
            else:
                print("No puede ingresar.")
        else:
            print("No puede ingresar.")