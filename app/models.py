from app import db

class Funcionario(db.Model):

    __tablename__ = 'funcionario'

    id_funcionario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_funcionario = db.Column(db.String(30))
    cpf_funcionario = db.Column(db.String(15), unique=True)
    email_funcionario = db.Column(db.String(30), unique=True)

    def __init__ (self, nome_funcionario, cpf_funcionario, email_funcionario ):
        self.nome_funcionario = nome_funcionario
        self.cpf_funcionario = cpf_funcionario
        self.email_funcionario = email_funcionario

    def __repr__(self):
        return '<Funcionario %r>' % self.nome_funcionario


