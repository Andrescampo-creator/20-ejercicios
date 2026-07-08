# Asignación de beca de transporte
faltas = input("¿Tiene faltas disciplinarias graves? (si/no): ")
if faltas == "si":
    print("No recibe la beca de transporte.")
else:
    evento = input("¿Representa a la institución en un evento nacional? (si/no): ")
    if evento == "si":
        print("Recibe la beca de transporte.")
    else:
        promedio = float(input("Ingrese el promedio: "))
        if promedio >= 4.2:
            asistencia = float(input("Ingrese el porcentaje de asistencia: "))
            if asistencia > 90:
                distancia = float(input("Ingrese la distancia de su casa a la institución (km): "))
                if distancia > 5:
                    print("Recibe la beca de transporte.")
                else:
                    print("No recibe la beca de transporte.")
            else:
                print("No recibe la beca de transporte.")
        else:
            print("No recibe la beca de transporte.")