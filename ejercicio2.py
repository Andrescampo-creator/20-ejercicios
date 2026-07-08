#Cálculo de envío gratuito con restricciones
#Una tienda ofrece envío gratuito si el valor de compra es mayor o igual a $150.000 y la entrega es dentro
#de la ciudad. También aplica si el cliente es premium y compra más de $80.000. No aplica si el producto está marcado
#como “envío especial”.
# Cálculo de envío gratuito con restricciones

envio_especial = input("¿El producto es de envío especial? (SI/NO): ")
if envio_especial == "SI":
    print("No tiene envío gratuito")
else:
    premium = input("¿El cliente es premium? (SI/NO): ")
    if premium == "SI":
        compra = float(input("Ingrese el valor de la compra: $"))
        if compra > 80000:
            print("Tiene envío gratuito")
        else:
            print("No tiene envío gratuito")
    else:
        compra = float(input("Ingrese el valor de la compra: "))
        if compra >= 150000:
            ciudad = input("¿La entrega es dentro de la ciudad? (SI/NO): ")
            if ciudad == "SI":
                print("Tiene envío gratuito")
            else:
                print("No tiene envío gratuito")
        else:
            print("No tiene envío gratuito")