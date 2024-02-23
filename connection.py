import sqlite3

connection = sqlite3.connect('Tarefa')
cursor = connection.cursor()

# 1. Crie uma tabela chamada "alunos" com os seguintes campos: id
#(inteiro), nome (texto), idade (inteiro) e curso (texto).

#cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100));')


# 2. Insira pelo menos 5 registros de alunos na tabela que você criou no
#exercício anterior.

#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(1, "Fernanda", 20, "Administracao")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(2, "Mariana", 31, "Economia")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(3, "Paulo", 26, "Administracao")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(4, "Fábio", 20, "Ciências de Dados")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(5, "Carolina",45, "Direito")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(6, "Carolina",45, "Engenharia")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(7, " Ana Carolina",25, "Engenharia")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(8, "Walter",18, "Engenharia")')




# 3. Consultas Básicas
# Escreva consultas SQL para realizar as seguintes tarefas:
# a) Selecionar todos os registros da tabela "alunos".
# b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
# c) Selecionar os alunos do curso de "Engenharia" em ordem
# alfabética.
# d) Contar o número total de alunos na tabela

# dados = cursor.execute('SELECT * FROM alunos')
# dados = cursor.execute('SELECT nome FROM alunos WHERE idade > 20')
#dados = cursor.execute('SELECT * FROM alunos WHERE curso = "Engenharia" ORDER BY nome')
#dados = cursor.execute('SELECT COUNT(*) FROM alunos')

# for alunos in dados:
#     print(alunos)

# 4. Atualização e Remoção
# a) Atualize a idade de um aluno específico na tabela.
# b) Remova um aluno pelo seu ID.

#cursor.execute('UPDATE alunos SET idade = 24 WHERE nome = "Paulo"')
#cursor.execute('DELETE FROM  alunos WHERE id = 6')




# 5. Criar uma Tabela e Inserir Dados

# Crie uma tabela chamada "clientes" com os campos: id (chave
# primária), nome (texto), idade (inteiro) e saldo (float). Insira alguns
# registros de clientes na tabela


# cursor.execute('''
#     CREATE TABLE clientes (
#         id INTEGER PRIMARY KEY,
#         nome TEXT,
#         idade INTEGER,
#         saldo REAL
#     )
# ''')
# cursor.execute('INSERT INTO clientes (nome, idade, saldo) VALUES ("João", 30, 1000.50)')
# cursor.execute('INSERT INTO clientes (nome, idade, saldo) VALUES ("Maria", 25, 500.75)')
# cursor.execute('INSERT INTO clientes (nome, idade, saldo) VALUES ("Carlos", 35, 1200.30)')
# cursor.execute('INSERT INTO clientes (nome, idade, saldo) VALUES ("Ana", 28, 800.90)')
# cursor.execute('INSERT INTO clientes (nome, idade, saldo) VALUES ("Pedro", 40, 1500.20)')



# 6. Consultas e Funções Agregadas
# Escreva consultas SQL para realizar as seguintes tarefas:
# a) Selecione o nome e a idade dos clientes com idade superior a
# 30 anos.
# b) Calcule o saldo médio dos clientes.
# c) Encontre o cliente com o saldo máximo.
# d) Conte quantos clientes têm saldo acima de 1000.

#consultas = cursor.execute('SELECT * FROM clientes')

#cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 30')

#cursor.execute('SELECT AVG(saldo) AS saldo_medio FROM clientes')
#cursor.execute('SELECT * FROM clientes WHERE saldo = (SELECT MAX(saldo) FROM clientes)')
# cursor.execute('SELECT COUNT(*) AS total_clientes_saldo_acima_1000 FROM clientes WHERE saldo > 1000;')


# for clientes in consultas:
#     print(clientes)
    
    
    
    
#     7. Atualização e Remoção com Condições
# a) Atualize o saldo de um cliente específico.
# b) Remova um cliente pelo seu ID.

#cursor.execute('UPDATE clientes SET saldo = 2000.50  WHERE nome = "Pedro"')
#cursor.execute('DELETE FROM clientes WHERE id = 4')




# 8. Junção de Tabelas
# Crie uma segunda tabela chamada "compras" com os campos: id
# (chave primária), cliente_id (chave estrangeira referenciando o id
# da tabela "clientes"), produto (texto) e valor (real). Insira algumas
# compras associadas a clientes existentes na tabela "clientes".
# Escreva uma consulta para exibir o nome do cliente, o produto e o
# valor de cada compra.


# consulta = cursor.execute('''
#     SELECT clientes.nome, compras.produto, compras.valor
#     FROM clientes
#     JOIN compras ON clientes.id = compras.cliente_id
# ''')


# cursor.execute('INSERT INTO compras (cliente_id, produto, valor) VALUES (1, "ProdutoA", 50.0)')
# cursor.execute('INSERT INTO compras (cliente_id, produto, valor) VALUES (2, "ProdutoB", 100.0)')
# cursor.execute('INSERT INTO compras (cliente_id, produto, valor) VALUES (3, "ProdutoC", 75.0)')

consulta = cursor.execute('''
    SELECT clientes.nome, compras.produto, compras.valor
    FROM clientes
    JOIN compras ON clientes.id = compras.cliente_id
''')

resultados = consulta.fetchall()


for resultado in resultados:
    print(resultado)


connection.commit()
connection.close()