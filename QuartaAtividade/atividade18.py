# Utilizando libs nativas do python como string e random, nessa atividade precisava1mos criar um código que gerasse uma senha
# aleatória que contivesse letras, numeros e caracteres especiais a biblioteca string trouxe esses requisitos, e a biblioteca random 
# fez o trabalho de gerar aleatoriedade da senha

import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

try:
    tamanho = int(input("Digite o tamanho da senha desejada: "))
    if tamanho < 1:
        print("O tamanho da senha deve ser maior que 0.")
    else:
        senha_gerada = gerar_senha(tamanho)
        print(f"Senha gerada: {senha_gerada}")
except ValueError:
    print("Por favor, insira um numero valido")