# Criar Script que cria um arquivo json com dados pessoais e depois leia os mesmo dados e exibe-os em tela

import json

arquivo_json = "pessoa.json"

pessoa = {
    "nome": "Allejandro",
    "idade": 29,
    "cidade": "São Paulo"
    
}

with open(arquivo_json, 'w', encoding='utf-8') as arquivo:
    json.dump(pessoa, arquivo, indent=4, ensure_ascii=False)
    
print("Dados escritos no Json com sucesso")

with open(arquivo_json, "r", encoding="utf=8") as arquivo:
    dados = json.load(arquivo)
    
print("/n Dados lidos do JSON: ")
print(dados)