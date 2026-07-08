#Acceso a examen virtual Un estudiante puede presentar un examen si está matriculado, tiene conexión a internet y su
#cámara funciona. También puede ingresar si tiene autorización del instructor y está en un aula presencial.
#No puede acceder si su cuenta está bloqueada.
bloqueada = input("¿La cuenta está bloqueada? (SI/NO): ")
if bloqueada == "SI":
    print("No puede presentar el examen")
else:
    autorizacion = input("¿Tiene autorización del instructor? (SI/NO): ")

    if autorizacion == "NO":
        aula = input("¿Está en un aula presencial? (SI/NO): ")

        if aula == "SI":
            print("Puede presentar el examen")
        else:
            print("No puede presentar el examen")

    else:
        matriculado = input("¿Está matriculado? (SI/NO): ")

        if matriculado == "SI":
            internet = input("¿Tiene conexión a internet? (SI/NO): ")

            if internet == "SI":
                camara = input("¿Su cámara funciona? (SI/NO): ")

                if camara == "SI":
                    print("Puede presentar el examen")
                else:
                    print("No puede presentar el examen")
            else:
                print("No puede presentar el examen")
        else:
            print("No puede presentar el examen")