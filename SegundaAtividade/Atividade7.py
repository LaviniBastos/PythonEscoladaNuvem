# Essa tarefa tem a função de definir o estágio da vida de uma pessoa com base em sua idade


idade = int(input("Digite aqui a sua idade: "))

if idade <= 12:
    print("Você ainda é criança") 
elif idade <= 17:
    print("Você já é adolescente")
elif idade <= 59:
    print("Você já é adulto")
else:
    print("Você é idoso")