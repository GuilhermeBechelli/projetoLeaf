from flask import Flask, render_template
import requests
import os
import datetime
from itertools import groupby

app = Flask(__name__, static_folder=os.path.abspath('static/'))

@app.route('/')
def index():
    # Faz uma requisição GET para a API
    response = requests.get('')

    # Obtém os dados da resposta da API
    data = response.json()

    # Extrai as colunas desejadas da API
    extracted_data = []
    for item in data:
        dthr_anuencia_marinha = item.get('dthr_anuencia_marinha')
        dthr_anuencia_marinha = datetime.datetime.strptime(dthr_anuencia_marinha, '%a, %d %b %Y %H:%M:%S %Z').strftime('%d/%m/%Y %H:%M') if dthr_anuencia_marinha is not None else '-'

        dthr_anuencia_policia = item.get('dthr_anuencia_justica')
        dthr_anuencia_policia = datetime.datetime.strptime(dthr_anuencia_policia, '%a, %d %b %Y %H:%M:%S %Z').strftime('%d/%m/%Y %H:%M') if dthr_anuencia_policia is not None else '-'

        dthr_atualizacao = item.get('dthr_atualizacao')
        dthr_atualizacao = datetime.datetime.strptime(dthr_atualizacao, '%a, %d %b %Y %H:%M:%S %Z').strftime('%d/%m/%Y %H:%M') if dthr_atualizacao is not None else '-'

        dthr_registro = item.get('dthr_registro')
        dthr_registro = datetime.datetime.strptime(dthr_registro, '%a, %d %b %Y %H:%M:%S %Z').strftime('%d/%m/%Y %H:%M') if dthr_registro is not None else '-'

        carga = item.get('carga', '-')
        pendencias = item.get('pendencias', '-') if item.get('pendencias') is not None else '-'  # Alteração para exibir "-" se o campo "pendencias" estiver ausente ou for igual a None

        extracted_item = {
            'duv': item['duv'],
            'nome': item.get('nome', ''),
            'pendencias': pendencias,
            'carga': carga,
            'local': item.get('local', ''),  ''
            'situacaoGeral': item['situacao'],
            'dthrAnuenciaMarinha': dthr_anuencia_marinha,
            'dthrAnuenciaPolicia': dthr_anuencia_policia,
            'dthrAtualizacao': dthr_atualizacao,
            'dthrRegistro': dthr_registro,
            'periodo': item['periodo'],
            'rap': item['rap']
        }

        extracted_data.append(extracted_item)

    # Ordena os dados pelo período e pela data
    extracted_data.sort(key=lambda x: (x['periodo'], x['dthrRegistro']))

    # Agrupa os itens por período e data
    grouped_data = []
    for key, group in groupby(extracted_data, key=lambda x: x['periodo']):
        grouped_by_period = {
            'periodo': key,
            'grupos_data': []
        }
        for date_key, date_group in groupby(group, key=lambda x: x['dthrRegistro'].split()[0]):
            date_group_sorted = sorted(list(date_group), key=lambda x: x['nome'])  # Adicione esta linha
            grouped_by_period['grupos_data'].append({
                'data': date_key,
                'itens': date_group_sorted  # Substitua a lista original pela lista ordenada
            })
        grouped_data.append(grouped_by_period)

    # Renderiza o template 'index.html' passando os dados agrupados
    return render_template('index.html', data=grouped_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8020)
