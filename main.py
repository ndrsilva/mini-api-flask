from modulo_mini_api_flask import run_server_api

if __name__ == '__main__':
    run_server_api()

# Obs.: Use o POSTMAN ou INSOMNIA

# GET - Ober livros
# http://localhost:5000/livros

# GET - Obter livro pelo id
# http://localhost:5000/livros/2

# PUT - Atualizar livro pelo id
# http://localhost:5000/livros/3

# POST - Incluir novo livro
# http://localhost:5000/livros

# DEL - Deletar um livro pelo id
# http://localhost:5000/livros/1
