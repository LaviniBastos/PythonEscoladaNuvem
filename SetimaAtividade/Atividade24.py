#Criar um Script que cria um arquivo csv e salva os dados inseridos

import csv

#Definindo um nome para o arquivo
arquivinho = "pessoas.csv"

#Definindo os dados que serão incluidos no arquivo
dados = [
    ["Nome", "Idade", "Cidade"],
    ["Ana", 43, "São Paulo"],
    ["Valéria", 30, "Curitiba"],
    ["Carlota", 23, "Rio de Janeiro"],
    ["Barbara", 27, "Florianopolis"],   
]

#Abre o arquivo para ser escrito

with open(arquivinho, mode='w', newline="", encoding="utf=8") as file:
    writer = csv.writer(file)
    
#Escrevendo os dados no arquivo   
    writer.writerows(dados)

print(f"Arquivo '{arquivinho}' criado com sucesso")
    
    
    
    