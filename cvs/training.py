import requests

limit = 1292

def get_pokemon(name):
    url = f'https://pokeapi.co/api/v2/pokemon/?limit={limit}'
    response = requests.get(url)
    data = response.json()
    id_list = [i for i in range(len(data['results']))]
    
    for id in id_list:
        if data['results'][id_list[id]]['name'] == name:
            print(name)
       

chosen_name = input('Escolha seu Pokemon: ')

get_pokemon(chosen_name)   

    
    