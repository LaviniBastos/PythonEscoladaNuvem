#Calculando o IMC do usuário interessado para ajuda-lo a entender como está a sua condição física

peso = float(input("Digite aqui o seu peso em kg: "))
altura = float(input("Digite aqui a sua altura: "))


imc = peso / (altura ** 2)

if imc < 18.5:
    print ("Você está abaixo do peso!")
elif imc < 25:
    print("Você está no seu peso ideal")
elif imc < 30:
    print("Você está com sobrepeso")
else:
    print("Você está obeso!")