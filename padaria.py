from flask import*

app = Flask(__name__)
receitas = [['ovo',5.5,'sal e ovo'],['panqueca',2.1,'ovo e farinha']]

@app.route("/")
def paginaprincipal():
    return render_template("paginaprincipal.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        senha = request.form.get('senha')
        if senha == 'kaue':
            return render_template('logado.html', msg="", lista=receitas)
        else:
            return render_template('login.html', erro='Senha incorreta!')
    return render_template('login.html')


@app.route('/funcionarios', methods=['GET', 'POST'])
def salvar_funcionario():
    if request.method == 'POST':
        nome = request.form.get('nome')
        cargo = request.form.get('cargo')
        telefone = request.form.get('telefone')

        with open('funcionarios.txt', 'a') as arquivo:
            arquivo.write(f'{nome}-{cargo}-{telefone}\n')

    return render_template('funcionarios.html')


@app.route('/cardapio', methods=['GET', 'POST'])
def salvar_cardapio():
    if request.method == 'GET':
        return render_template('cardapio.html',receitas=receitas)
    else:
        nome_receita = request.form.get('receita')
        return 'recebi a seguinte receita ' + nome_receita



@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar_receita():
    print('cheguei')
    global receitas
    if request.method == 'POST':
        nome = request.form.get('nome')
        preco = request.form.get('preco')
        ingredientes = request.form.get('ingredientes')

        print(nome)
        print( preco)
        print(ingredientes)

        receitas.append([nome, preco, ingredientes])
        msg = f'{nome} foi adicionada com sucesso!'
        return render_template('logado.html', msg=msg, lista=receitas)

    return render_template('adicionareceita.html')


@app.route('/remover', methods=['POST'])
def remover_receita():
    global receitas
    nome = request.form.get('nome')
    for receita in receitas:
        if receita[0] == nome:
            receitas.remove(receita)
            msg = f'{nome} removida com sucesso!'
            break
    else:
        msg = f'{nome} não foi encontrada na lista.'

    return render_template('logado.html', msg=msg, lista=receitas)


@app.route('/receitaslista', methods=['GET'])
def listar_receitas():
    return render_template('receitaslista.html', lista=receitas)


@app.route('/avaliacoes', methods=['GET', 'POST'])
def salvar_avaliacao():
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        comentario = request.form.get('comentario')

        with open('avaliacoes.txt', 'a') as arquivo:
            arquivo.write(f'{usuario}-{comentario}\n')

    return render_template('avaliacoes.html')


if __name__ == "__main__":
    app.run(debug=True)
