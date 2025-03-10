# Função que verifica se uma senha é forte o suficiente, ele valida se a senha é maior ou igual a 8 caracteres 
# e deve conter pelo menos 1 numero, ou usuário pode "sair" do programa caso queiram

def senha_forte(senha):
    return len(senha) >=8 and any(char.isdigit() for char in senha)

while True:
    senha = input("Digite uma senha forte que deve conter no minimo 8 caracteres e 1 numero, ou digite sair para terminar: ")
    
    if senha.lower() == "sair":
        print("Encerrando o programa..")
        break
    
    if senha_forte(senha):
        print("Senha validada com sucesso!")
        break
    
    else: 
        print("Senha muito fraca. Tente outra vez")