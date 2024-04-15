# Bootcamp Back-End Python e Django

## SEMANA 5 - Banco de Dados SQL

### Exercícios Banco de Dados

**1. Criação de Tabela**
- Crie uma tabela chamada `alunos` com os seguintes campos:
  - `id`: inteiro
  - `nome`: texto
  - `idade`: inteiro
  - `curso`: texto

**2. Inserção de Registros**
- Insira pelo menos 5 registros de alunos na tabela `alunos`.

**3. Consultas Básicas**
Escreva consultas SQL para realizar as seguintes tarefas:
  - a) Selecionar todos os registros da tabela `alunos`.
  - b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
  - c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
  - d) Contar o número total de alunos na tabela.

**4. Atualização e Remoção**
  - a) Atualize a idade de um aluno específico na tabela.
  - b) Remova um aluno pelo seu ID.

**5. Criação de Tabela e Inserção de Dados**
- Crie uma tabela chamada `clientes` com os campos:
  - `id`: chave primária
  - `nome`: texto
  - `idade`: inteiro
  - `saldo`: float
- Insira alguns registros de clientes na tabela.

**6. Consultas e Funções Agregadas**
Escreva consultas SQL para realizar as seguintes tarefas:
  - a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.
  - b) Calcule o saldo médio dos clientes.
  - c) Encontre o cliente com o saldo máximo.
  - d) Conte quantos clientes têm saldo acima de 1000.

**7. Atualização e Remoção com Condições**
  - a) Atualize o saldo de um cliente específico.
  - b) Remova um cliente pelo seu ID.

**8. Junção de Tabelas**
- Crie uma segunda tabela chamada `compras` com os campos:
  - `id`: chave primária
  - `cliente_id`: chave estrangeira referenciando o id da tabela `clientes`
  - `produto`: texto
  - `valor`: real
- Insira algumas compras associadas a clientes existentes na tabela `clientes`.
- Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.

---

Da engenharia à liderança, conectamos mulheres que querem fazer a diferença na tecnologia e inovação. Visite [WoMakersCode](http://womakerscode.org).

### Como Acessar e Executar a Atividade

Para executar a atividade, siga os passos abaixo:

**1. Clonar o Repositório**
   - Utilize o comando `git clone <https://github.com/kerllare/WomakersCode---Banco-de-Dados-SQL-.git>` para clonar este repositório localmente em sua máquina.

**2. Instalar Dependências**
   - Certifique-se de que o Python está instalado em sua máquina e, opcionalmente, instale um ambiente virtual para a execução do projeto.
   - Instale as dependências necessárias utilizando o comando `pip install -r requirements.txt` (assumindo que este arquivo esteja presente).

**3. Configurar o Banco de Dados SQLite**
   - Se ainda não estiver configurado, instale o SQLite3 em sua máquina.
   - Utilize o DBeaver ou uma ferramenta similar para abrir e interagir com o banco de dados.

**4. Abrir o Projeto no VSCode**
   - Abra a pasta clonada no VSCode.
   - Você encontrará os arquivos relacionados à tarefa na pasta `Tarefa`, e os scripts de conexão no arquivo `connection.py`.

**5. Executar os Scripts SQL**
   - Execute os scripts SQL no DBeaver para criar as tabelas e popular com dados.
   - Utilize o arquivo `tempCodeRunnerFile.py` para rodar os comandos e interagir com o banco de dados através do Python.

Certifique-se de ler qualquer documentação adicional ou arquivos `README` adicionais no repositório para quaisquer instruções específicas ou configurações adicionais necessárias.
