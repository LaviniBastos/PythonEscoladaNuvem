#Introdução a função: Função que realiza um comprimento

def comprimentar (nome):
    mensagem = f"ola {nome}, Bom dia, tudo muito bem com o(a) senhor(a)?"
    return mensagem


saudacao = comprimentar("maria")

print(saudacao)