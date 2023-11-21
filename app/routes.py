from app import app, db
from flask import render_template, request, redirect, url_for
from app.forms import FormFuncionario
from app.models import Funcionario


with app.app_context():
    db.create_all()


@app.route('/')
def index():
    funcionario = Funcionario.query.all()
    return render_template('index.html', funcionario=funcionario) 

@app.route('/adicionar', methods=['POST', 'GET'])
def adicionar():
    formFuncionario = FormFuncionario()
    if request.method == 'POST':
        if formFuncionario.validate_on_submit():
            nome_funcionario = formFuncionario.nome_funcionario.data
            cpf_funcionario = formFuncionario.cpf_funcionario.data
            email_funcionario = formFuncionario.email_funcionario.data

            funcionario = Funcionario(nome_funcionario, cpf_funcionario, email_funcionario)
            db.session.add(funcionario)
            db.session.commit()

            return redirect(url_for('index'))

    return render_template('adicionar.html', form=formFuncionario)

@app.route('/deletar/<int:id>', methods=['GET'])
def deletar(id):
    funcionario = Funcionario.query.get(id)

    if not funcionario:
        return redirect(url_for('index'))

    db.session.delete(funcionario)
    db.session.commit()

    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)
