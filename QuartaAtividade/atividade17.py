# Nessa atividade precisavamos fazer uma requisição à API random User para que obtevessemos os dados de um usuário aleatório


import requests

def obter_usuario():

    response = requests.get('https://randomuser.me/api/')
    
    if response.status_code == 200:
        data = response.json()
        usuario = data['results'][0]
        
    
        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        localizacao = f"{usuario['location']['country']}"
    
        print(f"Nome: {nome}")
        print(f"Email: {email}")
        print(f"País: {localizacao}")
    else:
        return "erro ao buscar dados."
    
if __name__ == '__name__':
    obter_usuario()