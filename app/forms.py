
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField
from wtforms.validators import DataRequired, Email



class FormCliente(FlaskForm):
    nome_cliente = StringField('Nome', validators=[DataRequired()])
    cpf_cliente = StringField('CPF', validators=[DataRequired()])
    email_cliente = StringField('E-mail', validators=[DataRequired(), Email()])


class FormProduto(FlaskForm):
    nome_produto =  StringField('Nome',validators=[DataRequired()])
    preco_produto = FloatField('Valor',validators=[DataRequired()])
    
    

class FormEstoque(FlaskForm):
    id_produto = IntegerField('Id Produto', validators=[DataRequired()])
    cod_estoque = IntegerField('Cod', validators=[DataRequired()])
    qtd_estoque = IntegerField('Qtd Estoque', validators=[DataRequired()])
    status_estoque = StringField('Status', validators=[DataRequired()])


class FormFuncionario(FlaskForm):
    nome_funcionario = StringField('Nome', validators=[DataRequired()])
    cpf_funcionario = StringField('CPF', validators=[DataRequired()])
    email_funcionario = StringField('E-mail', validators=[DataRequired(), Email()])
    

class FormTarefa(FlaskForm):
    data_tarefa = StringField('Data', validators=[DataRequired()])
    nome_tarefa = StringField('Tarefa', validators=[DataRequired()])
    status_tarefa = StringField('Status', validators=[DataRequired()])

class FormFuncionarioTarefa(FlaskForm):
    id_tarefa = IntegerField('Id Tarefa', validators=[DataRequired()])
    id_funcionario = IntegerField('ID funcionario', validators=[DataRequired()])
    

 
