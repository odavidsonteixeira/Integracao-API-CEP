import requests
import xml.etree.ElementTree as ET


def getCEP():
    cep = input("Qual o CEP da sua casa? (Apenas números)\n")
    if cep.isdigit():
        cep = str(cep)
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
            tree.write(f'dados_api.xml', encoding="utf-8", xml_declaration=True)

            print(f"Dados da API do {cep} salvos em 'dados_api.xml'")

        else:
            print(f'Não houve sucesso na requisição: {r.status_code}')
            return None
    else:
        print("Digite apenas números, IDIOTA!")
        exit()


getCEP()
