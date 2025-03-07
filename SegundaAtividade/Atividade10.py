# Nessa tarefa precisamos calcular e verificar se o ano inserido pelo usuário é bissexto

ano = int(input("Digite o ano para saber se  ele é bissexto: "))

if (ano % 4 ==0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"{ano} é um ano bissexto")
else:
    print(f"{ano} não é bissexto")
    