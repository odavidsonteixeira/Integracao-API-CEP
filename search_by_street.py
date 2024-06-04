import json

import requests
import xml.etree.ElementTree as ET


def getInfo():
    url = 'https://viacep.com.br/ws'
    estado = input("Digite o estado do endereço: \n")
    cidade = input("Digite a cidade do endereço: \n")
    rua = input("Digite a rua do endereço: \n")
    rua_without_spaces = rua.replace(" ", "%20")
    formato = '/json/'

    r = requests.get(f'{url}/{estado}/{cidade}/{rua_without_spaces}{formato}')

    if r.status_code == 200:

        data = r.json()
        with open("search_by_street.json", "w") as j_file:
            json.dump(data, j_file)
    else:
        print(f'Não houve sucesso na requisição: {r.status_code}')
        return None


getInfo()
