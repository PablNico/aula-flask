from app import db # importa variável db contida no __init__ da raíz


class User(db.Model): #Cria classe usuário como modelo do DB
    __tablename__ = "users" #Nome da tabela

    # Colunas da tabela, podemos passar tamanho máximo: db.String(50)
    id = db.Column(db.Integer, primary_key=True)     # Chave primária de tipo inteiro
    username = db.Column(db.String, unique=True)     # String não poderá ter outra igual
    password = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)

    def __init__(self, username, password, name, email): # Metodo construtor
        self.username = username
        self.password = password
        self.name = name
        self.email = email


    def __repr__(self):                         # forma de representação ao ser printada: print()
        return "<Usuário: %r>" % self.username


class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id')) # define coluna como chave estrangeira e referencia
                                                                # ela por: NomeTabela.Chave

    user = db.relationship('User', foreign_keys=user_id)

    def __init__(self, content, user_id):
        self.content = content
        self.user_id = user_id


    def __repr__(self):
        return "<Post %r>" % self.id


class Follow(db.Model):
    __tablename__ = "follow"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    follower_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', foreign_keys=user_id)
    follower = db.relationship('User', foreign_keys=follower_id)
