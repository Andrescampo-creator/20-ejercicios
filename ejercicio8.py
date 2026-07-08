# Reserva de sala de reuniones
pendientes = input("¿Tiene reservas pendientes sin cancelar? (si/no): ")
if pendientes == "si":
    print("No puede reservar.")
else:
    directivo = input("¿Es directivo? (si/no): ")
    if directivo == "si":
        disponible = input("¿La sala está disponible? (si/no): ")
        if disponible == "si":
            print("Puede reservar.")
        else:
            print("No puede reservar.")
    else:
        disponible = input("¿La sala está disponible? (si/no): ")
        if disponible == "si":
            asistentes = int(input("Ingrese el número de asistentes: "))
            capacidad = int(input("Ingrese la capacidad de la sala: "))
            if asistentes <= capacidad:
                anticipacion = int(input("¿Con cuántas horas de anticipación realiza la reserva?: "))
                if anticipacion >= 24:
                    print("Puede reservar.")
                else:
                    print("No puede reservar.")
            else:
                print("No puede reservar.")
        else:
            print("No puede reservar.")