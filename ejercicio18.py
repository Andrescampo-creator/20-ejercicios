# Publicación de contenido en una plataforma
suspension = input("¿Tiene suspensión activa? (si/no): ")
if suspension == "si":
    print("No puede publicar.")
else:
    moderador = input("¿Es moderador? (si/no): ")
    if moderador == "si":
        print("Puede publicar.")
    else:
        verificada = input("¿La cuenta está verificada? (si/no): ")
        if verificada == "si":
            normas = input("¿Acepta las normas de la plataforma? (si/no): ")
            if normas == "si":
                palabras = input("¿El contenido contiene palabras prohibidas? (si/no): ")
                if palabras == "no":
                    print("Puede publicar.")
                else:
                    print("No puede publicar.")
            else:
                print("No puede publicar.")
        else:
            print("No puede publicar.")