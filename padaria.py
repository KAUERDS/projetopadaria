from flask import *

app = Flask(__name__)
receitas = []
ingredientes = []

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
    return render_template('receitas.html')

@app.route('/adicionar', methods=['post','get'])
def adicionar_receita():
    if request.method == 'GET':
        return render_template('adicionareceita.html')
    global receitas
    nome = request.form.get('nome')
    preco = request.form.get('preco')
    ingredientes = request.form.get('ingredientes')

    receitas.append([nome, preco, ingredientes])
    mensagem = nome + ' Sua receita foi adicionado com sucesso'
    return render_template('receitaslista.html', msg=mensagem, lista=receitas)

@app.route('/remover', methods=['post'])
def remover_receita():
    #torna a variável modificável no escopo global
    global receitas
    nome = request.form.get('nome')
    if nome in receitas:
        receitas.remove(nome)

    else:
        msg = 'nao consta na lista de receitas'

    return render_template('logado.html')

@app.route('/receitaslistas', methods=['get'])
def listar_receitas():
    if len(receitas) > 0:
        return render_template('receitaslista.html', lista=receitas, ingredientes=receitas)
    else:
        return render_template('listareceitas.html', ingredientes=receitas)

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
