# Aprobación de una devolución de compra
personalizado = input("¿El artículo fue personalizado? (si/no): ")

if personalizado == "si":
    print("No se acepta la devolución.")
else:
    defectuoso = input("¿El producto llegó defectuoso? (si/no): ")
    if defectuoso == "si":
        print("Se acepta la devolución.")
    else:
        dias = int(input("Ingrese los días transcurridos desde la compra: "))
        if dias <= 30:
            factura = input("¿Tiene factura? (si/no): ")
            if factura == "si":
                daños = input("¿Presenta daños por mal uso? (si/no): ")
                if daños == "no":
                    print("Se acepta la devolución.")
                else:
                    print("No se acepta la devolución.")
            else:
                print("No se acepta la devolución.")
        else:
            print("No se acepta la devolución.")