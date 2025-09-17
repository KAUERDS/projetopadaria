from flask import *

app = Flask(__name__)

@app.route("/")
def paginaprincipal():
    return render_template("paginaprincipal.html")

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        senha = request.form.get('senha')
        if senha == 'kaue':
            return render_template('funcionarios.html')
        else:
            return render_template('/.html')


@app.route('/funcionarios', methods=['POST','GET'])
def salvar_funcionario():
    nome = request.form.get('nome')
    cargo = request.form.get('cargo')
    telefone = request.form.get('telefone')

    arquivo = open('funcionarios.txt', 'a')
    linha = f'{nome}-{cargo}-{telefone}\n'
    arquivo.write(linha)
    arquivo.close()

    return render_template('funcionarios.html')

@app.route('/cardapio', methods=['POST','GET'])
def salvar_cardapio():
    produto = request.form.get('produto')
    preco = request.form.get('preco')

    arquivo = open('cardapio.txt', 'a')
    linha = f'{produto}-{preco}\n'
    arquivo.write(linha)
    arquivo.close()

    return render_template('cardapio.html')

@app.route('/receitas', methods=['get'])
def adicionar_receitas():
    global receitas
    nome = request.form.get('nome')
    receitas.append(nome)
    mensagem = nome + ' foi adicionado com sucesso'
    return render_template('receitas.html', msg=mensagem)
    arquivo = open('receitas.txt', 'a')
    linha = f'{nome}-{descricao}\n'
    arquivo.write(linha)
    arquivo.close()

    return render_template('receitas.html')

@app.route('/avaliacoes', methods=['POST','GET'])
def salvar_avaliacao():
    usuario = request.form.get('usuario')
    comentario = request.form.get('comentario')

    arquivo = open('avaliacoes.txt', 'a')
    linha = f'{usuario}-{comentario}\n'
    arquivo.write(linha)
    arquivo.close()

    return render_template('avaliacoes.html')

if __name__ == "__main__":
    app.run()
