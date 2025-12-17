from flask import Flask, render_template, request, session, redirect, g
from dao.banco import Session, init_db
from dao.usuarioDAO import UsuarioDAO
from modelos.modelos import Usuario

app = Flask(__name__)
app.secret_key = 'Eu-Sou-O-Melhor'

init_db()

def criar_admin():
    session = Session()
    if not session.query(Usuario).filter_by(email='kaue').first():
        admin = Usuario(
            email='kaue',
            nome='Admi',
            senha='123'
        )
        session.add(admin)
        session.commit()
    session.close()

criar_admin()


@app.before_request
def pegar_sessao():
    g.session = Session()

@app.teardown_appcontext
def encerrar_sessao(exception=None):
    Session.remove()

receitas = [
    ['ovo', 5.5, 'sal e ovo'],
    ['panqueca', 2.1, 'ovo e farinha']
]

@app.route("/")
def paginaprincipal():
    return render_template("paginaprincipal.html")


@app.route('/login', methods=['GET', 'POST'])
def fazer_login():

    if request.method == 'GET':
        return render_template('login.html')

    email = request.form.get('loginusuario')
    senha = request.form.get('senhausuario')

    usuario_dao = UsuarioDAO(g.session)
    usuario = usuario_dao.autenticar(email, senha)

    if usuario:
        session['login'] = usuario.email
        return render_template('logado.html', usuario=usuario)
    else:
        msg = 'Usuário ou senha inválidos'
        return render_template('login.html', texto=msg)


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


@app.route('/funcionarios', methods=['GET', 'POST'])
def salvar_funcionario():

    if 'login' not in session:
        return redirect('/login')

    if request.method == 'POST':
        nome = request.form.get('nome')
        cargo = request.form.get('cargo')
        telefone = request.form.get('telefone')

        with open('funcionarios.txt', 'a') as arquivo:
            arquivo.write(f'{nome}-{cargo}-{telefone}\n')

    return render_template('funcionarios.html')


@app.route('/cardapio', methods=['GET', 'POST'])
def salvar_cardapio():

    if request.method == 'POST':
        nome_receita = request.form.get('receita')
        return f'Pedido realizado: {nome_receita}'

    return render_template('cardapio.html', receitas=receitas)


@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar_receita():

    if 'login' not in session:
        return redirect('/login')

    if request.method == 'POST':
        nome = request.form.get('nome')
        preco = request.form.get('preco')
        ingredientes = request.form.get('ingredientes')

        receitas.append([nome, preco, ingredientes])
        msg = f'Receita "{nome}" adicionada com sucesso!'

        return render_template('logado.html', msg=msg)

    return render_template('adicionareceita.html')

@app.route('/remover', methods=['POST'])
def remover_receita():

    if 'login' not in session:
        return redirect('/login')

    nome = request.form.get('nome')

    for receita in receitas:
        if receita[0] == nome:
            receitas.remove(receita)
            msg = f'Receita "{nome}" removida com sucesso!'
            break
    else:
        msg = f'Receita "{nome}" não encontrada.'

    return render_template('logado.html', msg=msg)


@app.route('/receitaslista')
def listar_receitas():
    return render_template('receitaslista.html', lista=receitas)

if __name__ == "__main__":
    app.run(debug=True)
