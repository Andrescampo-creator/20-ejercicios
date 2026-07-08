# Aprobación de crédito educativo
fraude = input("¿La persona está reportada por fraude? (si/no): ")
if fraude == "si":
    print("Crédito rechazado.")
else:
    codeudor = input("¿Tiene codeudor? (si/no): ")
    if codeudor == "si":
        ingresos_codeudor = float(input("Ingrese los ingresos del codeudor: "))
        if ingresos_codeudor > 3000000:
            print("Crédito aprobado.")
        else:
            print("Crédito rechazado.")
    else:
        ingresos = float(input("Ingrese los ingresos mensuales: "))
        if ingresos > 2000000:
            historial = input("¿Tiene historial crediticio positivo? (si/no): ")
            if historial == "si":
                deudas = input("¿Tiene deudas vencidas? (si/no): ")
                if deudas == "no":
                    print("Crédito aprobado.")
                else:
                    print("Crédito rechazado.")
            else:
                print("Crédito rechazado.")
        else:
            print("Crédito rechazado.")