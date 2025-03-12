
# Função que solicita um numero ao usuario e verifica se ele é par ou impar, ele continua solicitando e guardando os numeros para 
# se o usuário digitar "fim" ele exibir o resumo e a quantidade  numeros pares ou impares 

def verifica():
    pares = 0
    impares = 0
    
    while True:
        entrada = input("Digite um numero inteiro (ou 'fim' para sair: ")
        
        if entrada.lower( ) == "fim":
            break
        
        try: 
            numero = int(entrada)
            if numero % 2 == 0:
                print(f" O {numero} é par")
                pares +=1
            else:
                print(f"{numero} é IMPAR")
                impares +=1
        except ValueError:
            print(f"Erro: Por favor digite um numero inteiro")
            
    print("\nResumo")
    print(f"Quantidade de numeros pares: {pares}")
    print(f"Quantidade de números ímpares: {impares}")

verifica()