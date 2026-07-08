# Selección para prácticas empresariales
disciplinario = input("¿Tiene proceso disciplinario abierto? (si/no): ")
if disciplinario == "si":
    print("No puede ser seleccionado.")
else:
    empresa = input("¿Una empresa lo solicitó directamente? (si/no): ")
    if empresa == "si":
        print("Puede ser seleccionado.")
    else:
        modulos = input("¿Aprobó todos los módulos requeridos? (si/no): ")
        if modulos == "si":
            promedio = float(input("Ingrese el promedio: "))
            if promedio >= 3.8:
                hoja = input("¿Entregó la hoja de vida? (si/no): ")
                if hoja == "si":
                    print("Puede ser seleccionado.")
                else:
                    print("No puede ser seleccionado.")
            else:
                print("No puede ser seleccionado.")
        else:
            print("No puede ser seleccionado.")