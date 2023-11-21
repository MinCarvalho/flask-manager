
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email


class FormFuncionario(FlaskForm):
    nome_funcionario = StringField('Nome', validators=[DataRequired()])
    cpf_funcionario = StringField('CPF', validators=[DataRequired()])
    email_funcionario = StringField('E-mail', validators=[DataRequired(), Email()])
    
    #botao_submit_criarconta = SubmitField('Cadastrar Usuario')