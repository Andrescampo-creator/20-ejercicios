#Validación de inscripción a un curso avanzado:
#Un aprendiz puede inscribirse si aprobó el curso básico con nota mayor o igual a 3.5 y
#tiene asistencia superior al 80%. También puede ingresar si presentó una prueba de nivelación y
#obtuvo 85 puntos o más. No puede inscribirse si tiene sanción académica
sancion=input('Diga si tiene alguna sanción académica (SI/NO)? ')
if sancion =='NO':
    nivelacion= input('Usted presento prueba de nivelación (SI/NO): ')
    if nivelacion=='SI':
        puntos=float(input('ingrese puntaje obtenido: '))
        if puntos>84:
            print('Usted se puede inscribir al curso avanzado')
        else:
            print('Usted no se puede inscribir al curso avanzado')
    else:
        nota = float(input('Ingrese la nota del curso básico:'))
        if nota >3.4:
            asistencia = float(input("Ingrese el porcentaje de asistencia: "))
            if asistencia > 80:
                print("Puede inscribirse al curso avanzado")
            else:
                    print('Usted no se puede inscribir al curso avanzado')
        else:
            print("usted no puede inscribirse al curso avanzado")
else:
    print("usted no puede inscribirse al curso avanzado")