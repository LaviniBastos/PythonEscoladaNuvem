# Utilizando a API CEP, o usuario digite um cep e o código faz uma requisição à API e traz as informações do cep
# houve o tratamento de erros caso alguma informação relacionada ao cep não estivesse disponível

import requests

def consulta_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json"
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        dados = resposta.json()
        
        if "erro" not in dados:
            cep = dados.get("localidade", 'Não Disponívels')
            logradouro = dados.get ("logradouro", "Não Disponível")
            complemento = dados.get("complemento", "Não Disponível")
            bairro = dados.get("bairro", "Não Disponível")
            cidade = dados.get("cidade", "Não Disponível")
            estado = dados.get("estado", "Não Disponível")
            
            return { 
                    "cep": cep,
                    "logradouro": logradouro,
                    "complemento": complemento, 
                    "bairro": bairro, 
                    "cidade": cidade,
                    "estado": estado,
                    
                    }
        else:
            return "CEP invalido."
        
    else: 
        "Erro ao buscar cep"
        
        
cep = input("digite o CEP:").strip()
resultado = consulta_cep(cep)
print(resultado)