# Registro de asistencia en formación virtual
suplantacion = input("¿Se detectó suplantación? (si/no): ")
if suplantacion == "si":
    print("No queda presente.")
else:
    excusa = input("¿Tiene una excusa aprobada por el instructor? (si/no): ")
    if excusa == "si":
        print("Queda presente.")
    else:
        conexion = float(input("Ingrese el porcentaje de conexión: "))
        if conexion >= 80:
            actividad = input("¿Participó en al menos una actividad? (si/no): ")
            if actividad == "si":
                encuesta = input("¿Respondió la encuesta final? (si/no): ")
                if encuesta == "si":
                    print("Queda presente.")
                else:
                    print("No queda presente.")
            else:
                print("No queda presente.")
        else:
            print("No queda presente.")