# Matheus Carvalho Sales
# 21804995


# Importando bibliotecas
from flask import Flask, request, render_template
from flaskext.mysql import MySQL
from bd import *


# Instanciando a app Flask
app = Flask(__name__)
# Instanciar o objeto MySQL
mysql = MySQL()
# Ligar o MYSQL ao Flask
mysql.init_app(app)

# Configurando o acesso ao MySQL
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'faculdade'

# Rota para /
@app.route('/')
def principal():
    return render_template('index.html')



# Rota para listar professores
@app.route('/listarprofessores/')
def listarProfessor():

    cursor = mysql.get_db().cursor()
    return render_template('listarprofessores.html', professores=get_idprofessor(cursor))


# Rota para exibir professor
@app.route('/exibirprofessor/<professor>')
def detalhar(professor):

    # Obtendo o cursor para acessar o BD
    cursor = mysql.get_db().cursor()


    return render_template('exibirprofessor.html', detalhes=get_detalhe(cursor, professor))


# Rota para pesquisar por titulacao
@app.route('/consultarPorTitulacao/')
def pesquisarTitulacao():

    return render_template('titulacao.html')



# Rota para titulação
@app.route('/listarTitulacao', methods=['GET','POST'])
def titulacao():
    if request.method == 'POST':
        titulacao = request.form.get('pesquisar')

        #validacao da titulação
        if(titulacao == 'especialização'):
            titulacao = 1
        elif(titulacao == 'mestrado'):
            titulacao = 2
        elif(titulacao == 'doutorado'):
            titulacao = 3

        # Obtendo o cursor para acessar o BD
        cursor = mysql.get_db().cursor()

        # Obtendo o idtitulacao
        idtitulacao = get_idtitulacao(cursor, titulacao)

        # Verificar a senha
        if titulacao is None:
            return render_template('titulacao.html', erro='Titulação não existe!')
        else:
            # Obtendo o cursor para acessar o BD
            cursor = mysql.get_db().cursor()

            return render_template('listartitulacao.html',  disciplinas=get_detalhe(cursor, idtitulacao))

    else:
        return render_template('index.html', erro='Método incorreto. Use POST!')

# Rodando a app
if __name__ == '__main__':
    app.run(debug=True)