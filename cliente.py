
from app import App

# Carregar os dados do arquivo JSON
with open('data.json', 'r') as file:
    dados = file.read()

# Instância da classe App
app = App()

# Chamar a função find_data para encontrar o primeiro nome
first_name = app.find_data(dados, "first_name")
print("Primeiro nome:", first_name)
