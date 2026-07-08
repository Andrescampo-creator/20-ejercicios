# Acceso a una plataforma empresarial
pais = input("¿Se conecta desde un país autorizado? (si/no): ")
if pais == "no":
    print("No puede ingresar.")
else:
    administrador = input("¿Tiene acceso temporal generado por un administrador? (si/no): ")
    if administrador == "si":
        print("Puede ingresar.")
    else:
        usuario = input("¿El usuario es correcto? (si/no): ")
        if usuario == "si":
            contraseña = input("¿La contraseña es correcta? (si/no): ")
            if contraseña == "si":
                verificacion = input("¿Tiene activada la verificación en dos pasos? (si/no): ")
                if verificacion == "si":
                    cuenta = input("¿La cuenta está activa? (si/no): ")
                    if cuenta == "si":
                        print("Puede ingresar.")
                    else:
                        print("No puede ingresar.")
                else:
                    print("No puede ingresar.")
            else:
                print("No puede ingresar.")
        else:
            print("No puede ingresar.")