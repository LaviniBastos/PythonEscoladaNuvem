# Calcular a idade de uma pessoa em dias, com base em seu ano de nascimento


from datetime import date

def idade_dias(ano):
    ano_atual = date.today().year
    idade_anos = ano_atual - ano
    return idade_anos * 365

ano = int(input(" Digite aqui o seu ano de nascimento"))
print(f"Você tem aproximadamente {idade_dias(ano)} dias de vida.")
    