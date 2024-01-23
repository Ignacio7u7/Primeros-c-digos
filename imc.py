altura = float(input("Ingrese su altura en cm: "))
peso = float(input("Ingrese su peso en kg: "))

IMC = peso / altura ** 2

print("Su IMC es de: ", IMC)

if IMC < 18.5:
    print("Su peso es bajo: Usted es delgado")
elif IMC > 18.5 and IMC < 24.9:
    print("Su peso es adecuado: Aceptable")
elif IMC > 25.0 and IMC < 29.9:
    print("Usted tiene sobrepeso")
elif IMC > 30.0 and IMC < 34.9:
    print("Usted tiene obesidad de grado 1")
elif IMC > 35.0 and IMC < 40.0:
    print("Usted tiene obesidad de grado 2")

