from app import db


class Cliente(db.Model):
    __tablename__ = 'clientes'

    id_cliente = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_cliente = db.Column(db.String(30))
    cpf_cliente = db.Column(db.String(15), unique=True)
    email_cliente = db.Column(db.String(30), unique=True)
    
    def __init__(self, nome_cliente, cpf_cliente, email_cliente):
        self.nome_cliente = nome_cliente
        self.cpf_cliente = cpf_cliente
        self.email_cliente = email_cliente

    def __repr__(self):
        return '<Cliente %r>' % self.nome_cliente
    
class Produto(db.Model):
    id_produto = db.Column(db.Integer, primary_key=True, autoincrement=True) 
    nome_produto = db.Column(db.String(30))
    preco_produto = db.Column(db.Float)

    estoque = db.relationship('Estoque', backref='produto', uselist=False)

    def __init__(self, nome_produto, preco_produto):
        self.nome_produto = nome_produto
        self.preco_produto = preco_produto
    
    def __repr__(self):
        return '<Produto %r>' % self.nome_produto
        

class Estoque(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cod_estoque = db.Column(db.Integer)
    qtd_estoque = db.Column(db.Integer)
    status_estoque = db.Column(db.String(75))
    produto_id = db.Column(db.Integer, db.ForeignKey('produto.id_produto'))

    def __init__(self, cod_estoque, qtd_estoque, status_estoque, produto_id):
        self.cod_estoque = cod_estoque
        self.qtd_estoque = qtd_estoque
        self.status_estoque = status_estoque
        self.produto_id = produto_id

    def __repr__(self):
        return '<Estoque %r>' % self.cod_estoque
    


class Funcionario(db.Model):
    __tablename__ = 'funcionario'

    id_funcionario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_funcionario = db.Column(db.String(30))
    cpf_funcionario = db.Column(db.String(15), unique=True)
    email_funcionario = db.Column(db.String(30), unique=True)

    # Remova a relação aqui por enquanto
    # tarefas = db.relationship('Tarefa', secondary='funcionario_tarefa', back_populates='funcionarios')

    def __init__(self, nome_funcionario, cpf_funcionario, email_funcionario):
        self.nome_funcionario = nome_funcionario
        self.cpf_funcionario = cpf_funcionario
        self.email_funcionario = email_funcionario

    def __repr__(self):
        return '<Funcionario %r>' % self.nome_funcionario


class Tarefa(db.Model):
    id_tarefa = db.Column(db.Integer, primary_key=True)
    data_tarefa = db.Column(db.Text)
    nome_tarefa = db.Column(db.Text)
    status_tarefa = db.Column(db.Text)

    # Remova a relação aqui por enquanto
    # funcionarios = db.relationship('Funcionario', secondary='funcionario_tarefa', back_populates='tarefas')

    def __init__(self, data_tarefa, nome_tarefa, status_tarefa):
        self.data_tarefa = data_tarefa
        self.nome_tarefa = nome_tarefa
        self.status_tarefa = status_tarefa     

    def __repr__(self):
        return '<Tarefa %r>' % self.nome_tarefa


# Agora, defina a classe Funcionario_Tarefa
class Funcionario_Tarefa(db.Model):
    id_tarefa = db.Column(db.Integer, db.ForeignKey('tarefa.id_tarefa'), primary_key=True)
    id_funcionario = db.Column(db.Integer, db.ForeignKey('funcionario.id_funcionario'), primary_key=True)

    def __init__(self, id_tarefa, id_funcionario):
        self.id_tarefa = id_tarefa
        self.id_funcionario = id_funcionario

    def __repr__(self):
        return '<Funcionario_Tarefa %r>' 


# Agora, adicione as relações nas classes Funcionario e Tarefa
Funcionario.tarefas = db.relationship('Tarefa', secondary='funcionario_tarefa', back_populates='funcionarios')
Tarefa.funcionarios = db.relationship('Funcionario', secondary='funcionario_tarefa', back_populates='tarefas')


        