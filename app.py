from flask import Flask, render_template
import requests
import os
import datetime


app = Flask(__name__, static_folder=os.path.abspath('static/'))

@app.route('/')
def index():
    # Faz uma requisição GET para a API
    response = requests.get('xxxxxxxxxxxxxxxx')
    
    # Obtém os dados da resposta da API
    data = response.json()
    
    # Extrai as colunas desejadas da API
    extracted_data = []
    for item in data:
        dthr_anuencia_marinha = item['dthr_anuencia_marinha']
        if dthr_anuencia_marinha is not None:
            dthr_anuencia_marinha = datetime.datetime.strptime(dthr_anuencia_marinha, '%a, %d %b %Y %H:%M:%S %Z').strftime('%d/%m/%Y %H:%M')
        else:
            dthr_anuencia_marinha = '-'

        dthr_anuencia_policia = item['dthr_anuencia_justica']
        if dthr_anuencia_policia is not None:
            dthr_anuencia_policia = datetime.datetime.strptime(dthr_anuencia_policia, '%a, %d %b %Y %H:%M:%S %Z').strftime('%d/%m/%Y %H:%M')
        else:
            dthr_anuencia_policia = '-'

        dthr_atualizacao = item['dthr_atualizacao']
        if dthr_atualizacao is not None:
            dthr_atualizacao = datetime.datetime.strptime(dthr_atualizacao, '%a, %d %b %Y %H:%M:%S %Z').strftime('%d/%m/%Y %H:%M')
        else:
            dthr_atualizacao = '-'

        dthr_registro = item['dthr_registro']
        if dthr_registro is not None:
            dthr_registro = datetime.datetime.strptime(dthr_registro, '%a, %d %b %Y %H:%M:%S %Z').strftime('%d/%m/%Y %H:%M')
        else:
            dthr_registro = '-'
            
        periodo = item['periodo']
        if periodo is not None:
            periodo = datetime.datetime.strptime(periodo, '%a, %d %b %Y %H:%M:%S %Z').strftime('%d/%m/%Y %H:%M')
        else:
            periodo = '-'

        extracted_item = {
            'duv': item['duv'],
            'situacaoGeral': item['situacao'],
            'dthrAnuenciaMarinha': dthr_anuencia_marinha,
            'dthrAnuenciaPolicia': dthr_anuencia_policia,
            'dthrAtualizacao': dthr_atualizacao,
            'dthrRegistro': dthr_registro,
            'periodo': periodo,
            
        }

        extracted_data.append(extracted_item)
    # Ordena os dados em ordem decrescente com base na coluna 'periodo'
    extracted_data = sorted(extracted_data, key=lambda x: x['periodo'], reverse=True)
    
    # Renderiza o template 'index.html' passando os dados extraídos da API
    return render_template('index.html', data=extracted_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2100)
