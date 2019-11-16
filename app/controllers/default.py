from app import app                # Referencia __init__ da pasta app
from flask import render_template   # Importa rendenizador de páginas do flask

from app.models.tables import User      #Importa a classe User do arquivo models/tables.py
from app.models.forms import LoginForm  #Importa a classe LoginForm contendo os campos do formulários
                                        #no arquivo models/forms


@app.route("/index") #Cria rota para o arquivo "index.html" tanto pela URL "/index" quando URL vazia
@app.route("/")
def index():
    return render_template("index.html")


@app.route('/login', methods=["GET", "POST"])  # Cria rota para o arquivo "login.html"
def login():                                   # Permitindo requisições HTTP do tipo GET e POST
    form = LoginForm()          # Cria objeto com os campos dos formulários, deve ser o mesmo nome passado
                                # para a função render_tamplate, quanto na páginas que vai usar a variável
    if form.validate_on_submit():   # Autentica se os dados do formulário
        print("{} \n"     # Printa os dados enviados no terminal
              "{}".format(form.username.data, form.password.data))

    return render_template('login.html', form=form) # Rendeniza pagína com form



@app.route("/teste/<info>")  # Cria rota para teste e aceita um parâmetro de entrada
@app.route("/teste", defaults={'info': None}) # Caso não seja passado parâmetro, irá tomar essa rota
def teste(info):
    i = User("Nisco",
             "qwersty",
             "Pablo sNicolas",
             "nico@snico.com")
    r = User.query.filter_by(username="Nico").all()
    print(r)
    return "Ok"