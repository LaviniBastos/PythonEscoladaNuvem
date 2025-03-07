#Exemplo pratico utilizando If e else para verificação da maioridade de um usuário

idade = int(input("Digite aqui a sua idade: "))

if idade < 18:
    print("Você ainda é menor de idade") 
elif idade >= 18:
    print("Você já é maior de idade")