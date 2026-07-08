# Validación de pago en una tienda virtual
sospechosa = input("¿Se detectó una transacción sospechosa? (si/no): ")
if sospechosa == "si":
    print("Pago rechazado.")
else:
    billetera = input("¿Usa una billetera digital validada? (si/no): ")
    if billetera == "si":
        print("Pago aprobado.")
    else:
        tarjeta = input("¿La tarjeta está vigente? (si/no): ")
        if tarjeta == "si":
            fondos = input("¿Tiene fondos suficientes? (si/no): ")
            if fondos == "si":
                codigo = input("¿El código de seguridad es correcto? (si/no): ")
                if codigo == "si":
                    print("Pago aprobado.")
                else:
                    print("Pago rechazado.")
            else:
                print("Pago rechazado.")
        else:
            print("Pago rechazado.")