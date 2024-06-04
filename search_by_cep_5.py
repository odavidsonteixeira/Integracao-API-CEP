import requests
import xml.etree.ElementTree as ET


def getCEP(x, cep):
    url = 'https://viacep.com.br/ws/'
    formato = '/json/'

    r = requests.get(url + cep + formato)

    if r.status_code == 200:

        data = r.json()

        root = ET.Element("dados")

        for key, value in data.items():
            element = ET.SubElement(root, key)
            element.text = str(value)

        tree = ET.ElementTree(root)
        tree.write(f'dados_api{x + 1}.xml', encoding="utf-8", xml_declaration=True)

        print(f"Dados da API do {cep} salvos em 'dados_api{x + 1}.xml'")

    else:
        print(f'Não houve sucesso na requisição: {r.status_code}')
        return None


cep = input("Qual o CEP da sua casa? (Apenas números)")
if cep.isdigit():
    for x in range(5):
        cep = str(cep)
        getCEP(x, cep)
        cep = int(cep) + 1
else:
    print("Digite apenas números, IDIOTA!")
    exit()
