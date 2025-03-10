#Função que verifica se uma palavra ou frase pode ser lida de tras para frente e manter o mesmo significado


def eh_palindromo(texto):
    texto = ''.join(caractere for caractere in texto.lower() if caractere.isalnum())
    
    return texto == texto [::-1]

while True:
    palavra_ou_frase = input("Digite uma palavra ou frase (ou 'fim' para sair): ")
    if palavra_ou_frase.lower() == "fim":
        break
    
    if eh_palindromo(palavra_ou_frase):
        print("Sim")
    else:
        print("Não")