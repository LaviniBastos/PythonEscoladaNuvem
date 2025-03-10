# Definir uma função que calcula a porcentagem da gorjeta com o valor total da conta de um cliente em um restaurante.

def calcular_gorjeta(valor_conta, percentual=10):
    gorjeta = (valor_conta * percentual) / 100
    total_com_gorjeta = valor_conta + gorjeta
    return gorjeta, total_com_gorjeta
    
    
valor_conta = float(input("digite aqui o valor da conta: R$ "))
percentual = float(input("Digite a porcentagem da gorjeta (padrão é 10%: )" or 10))

gorjeta, total = calcular_gorjeta(valor_conta, percentual)

print(f"Gorjeta: R$ {gorjeta:.2f}")
print(f"Total a pagar: R$ {total:.2f}")