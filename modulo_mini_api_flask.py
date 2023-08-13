from flask import Flask
from flask import jsonify
from flask import request
from data import livros


app = Flask(__name__)

@app.route('/livros', methods=['GET'])
def obter_livros():
    """..."""
    return jsonify(livros)

@app.route('/livros/<int:id_livro>', methods=['GET'])
def obter_livro_por_id(id_livro):
    """..."""
    return [livro for livro in livros
            if livro.get('id') == id_livro]

@app.route('/livros/<int:id_livro>', methods=['PUT'])
def editar_livro_por_id(id_livro):
    """..."""
    livro_alterado = request.get_json()

    return [jsonify(livros[indice]) for indice, livro in enumerate(livros)
            if livro.get('id') == id_livro
            and livros[indice].update(livro_alterado)]

@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
    """..."""
    novo_livro = request.get_json()
    for livro in livros:
        if livro.get('id') == novo_livro['id']:
            return jsonify('Este livro já está cadastrado.')

    livros.append(novo_livro)
    return jsonify(livros)

@app.route('/livros/<int:id_livro>', methods=['DELETE'])
def excluir_livro(id_livro):
    """..."""
    for indice, livro in enumerate(livros):
        if livro.get('id') == id_livro:
            del livros[indice]

    return jsonify(livros)

def run_server_api():
    """..."""
    app.run(port=5000, host='localhost', debug=True)
