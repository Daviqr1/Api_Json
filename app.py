from flask import Flask, jsonify
import json

class App:
    def __init__(self):
        # Inicialização do aplicativo Flask
        self.app = Flask("Api_Json")

        # Definição da rota para obter dados
        @self.app.route('/get_data', methods=['GET'])
        def get_data():
            # Abre e lê o arquivo JSON
            with open('data.json', 'r') as file:
                data = json.load(file)
            
            # Retorna os dados em formato JSON
            return jsonify(data)
        
    def find_data(self, data, key):
        data_json = json.loads(data)

        if key in data_json:
            return data_json[key]
        else:
            return "Chave não encontrada"
    first_name = app.find_data(dados, "first_name")
    ip_address = app.find_data(dados, "ip_address")

    def run(self):
        # Inicia o servidor Flask na porta 5000 com modo de depuração ativado
        self.app.run(port=5000)

if __name__ == '__main__':
    # Instância da classe App e execução do servidor
    app = App()
    app.run()
