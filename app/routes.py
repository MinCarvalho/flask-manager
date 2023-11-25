from app import app, db
from flask import render_template, request, redirect, url_for
from app.forms import FormFuncionario, FormCliente, FormEstoque, FormProduto, FormFuncionarioTarefa, FormTarefa
from app.models import Funcionario, Cliente, Estoque, Produto, Tarefa, Funcionario_Tarefa


with app.app_context():
    db.create_all()


@app.route('/')
def index():
    funcionario = Funcionario.query.all()
    cliente = Cliente.query.all()
    estoque = Estoque.query.all()
    produto = Produto.query.all()
    tarefa = Tarefa.query.all()
    funcionario_tarefa = db.session.query(Funcionario_Tarefa, Funcionario, Tarefa)\
        .join(Funcionario).join(Tarefa).all()
    return render_template('index.html', funcionario=funcionario, cliente=cliente, estoque=estoque, produto=produto, tarefa=tarefa, funcionario_tarefa=funcionario_tarefa) 

@app.route('/addfuncionario', methods=['POST', 'GET'])
def addfuncionario():
    formFuncionario = FormFuncionario()

    if formFuncionario.validate_on_submit():
        nome_funcionario = formFuncionario.nome_funcionario.data
        cpf_funcionario = formFuncionario.cpf_funcionario.data
        email_funcionario = formFuncionario.email_funcionario.data

        funcionario = Funcionario(nome_funcionario, cpf_funcionario, email_funcionario)
        db.session.add(funcionario)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('adicionar.html', form=formFuncionario)




@app.route('/addcliente', methods=['POST', 'GET'])
def addcliente():
    formCliente = FormCliente()
    if request.method == 'POST':
        if formCliente.validate_on_submit():
            nome_cliente = formCliente.nome_cliente.data
            cpf_cliente = formCliente.cpf_cliente.data
            email_cliente = formCliente.email_cliente.data
            cliente = Cliente(nome_cliente, cpf_cliente, email_cliente)
            db.session.add(cliente)
            db.session.commit()
            

            return redirect(url_for('index'))

    return render_template('addcliente.html', form=formCliente)


@app.route('/add_produto', methods=['POST', 'GET'])
def add_produto():
    formProduto = FormProduto()
    if request.method == 'POST':
        if formProduto.validate_on_submit():
            nome_produto = formProduto.nome_produto.data
            preco_produto = formProduto.preco_produto.data
            
            produto = Produto(nome_produto, preco_produto)
            db.session.add(produto)
            db.session.commit()
            

            return redirect(url_for('index'))

    return render_template('add_produto.html', form=formProduto)



@app.route('/addestoque', methods=['POST', 'GET'])
def addestoque():
    formEstoque = FormEstoque()

    if formEstoque.validate_on_submit():
        
        estoque = Estoque(
            cod_estoque=formEstoque.cod_estoque.data,
            qtd_estoque=formEstoque.qtd_estoque.data,
            status_estoque=formEstoque.status_estoque.data,
            produto_id=formEstoque.id_produto.data  # Assumindo que você obtém o id_produto do formulário
        )

        db.session.add(estoque)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('addestoque.html', form=formEstoque)


@app.route('/add_tarefa', methods=['POST', 'GET'])
def add_tarefa():
    formtarefa = FormTarefa()

    if formtarefa.validate_on_submit():
        
        tarefa = Tarefa(
            data_tarefa=formtarefa.data_tarefa.data,
            nome_tarefa=formtarefa.nome_tarefa.data,
            status_tarefa=formtarefa.status_tarefa.data,
            
        )

        db.session.add(tarefa)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('add_tarefa.html', form=formtarefa)

@app.route('/funcionario_tarefa', methods=['POST'])
def funcionario_tarefa():
    formFunTarefa = FormFuncionarioTarefa()

    if formFunTarefa.validate_on_submit():
        id_tarefa = formFunTarefa.id_tarefa.data
        id_funcionario = formFunTarefa.id_funcionario.data

        # Verifique se a tarefa e o funcionário existem no banco de dados
        tarefa = Tarefa.query.get(id_tarefa)
        funcionario = Funcionario.query.get(id_funcionario)

        if tarefa and funcionario:
            # Crie uma nova instância de Funcionario_Tarefa
            func_tarefa = Funcionario_Tarefa(id_tarefa=id_tarefa, id_funcionario=id_funcionario)

            # Adicione ao banco de dados
            db.session.add(func_tarefa)
            db.session.commit()

            return redirect(url_for('index'))  # Redirecione para a página inicial ou outra página desejada após a associação

    return render_template('funcionario_tarefa.html', form=formFunTarefa)






###DELETEEEEEE
@app.route('/deletar/<int:id>', methods=['GET'])
def deletar(id):
    funcionario = Funcionario.query.get(id)

    if not funcionario:
        return redirect(url_for('index'))

    db.session.delete(funcionario)
    db.session.commit()

    return redirect(url_for('index'))



@app.route('/deletar_cliente/<int:id>', methods=['GET'])
def deletar_cliente(id):
    cliente = Cliente.query.get(id)

    if not cliente:
        return redirect(url_for('index'))

    db.session.delete(cliente)
    db.session.commit()

    return redirect(url_for('index'))



@app.route('/deletar_estoque/<int:id>', methods=['GET'])
def deletar_estoque(id):
    estoque = Estoque.query.get(id)

    if not estoque:
        return redirect(url_for('index'))

    db.session.delete(estoque)
    db.session.commit()

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
