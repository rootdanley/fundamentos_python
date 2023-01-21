#CRUD BÁSICO
import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='proderj@123',
    database='locadora',
)


cursor = conexao.cursor()

opcao = input('Digite a opcao: INSERIR(I) | LEITURA(L) | ATUALIZAR(A) | DELETAR(D)').lower()

if opcao == 'i':
    criar()


# CREATE
def criar():
    nome = input('Digite o nome do cliente: ')
    sobrenome = input('Digite o sobrenome do cliente: ')

    comando = f'INSERT INTO cliente (nome, sobrenome) VALUES ("{nome}", "{sobrenome}")'
    cursor.execute(comando)
    conexao.commit()


#READ
# comando = f'SELECT * FROM cliente'
# cursor.execute(comando)
# resultado = cursor.fetchall()
# print(resultado)

# cursor.close()
# conexao.close()

#UPDATE
# nome_novo = input('Digite o novo:')
# nome_antigo = input('Digite o antigo:')

# comando = f'UPDATE cliente SET nome = "{nome_novo}"  WHERE nome = "{nome_antigo}"'
# cursor.execute(comando)
# conexao.commit()

# cursor.close()
# conexao.close()

#DELETE
# nome = input('Digite o para exlcuir:')


# comando = f'DELETE FROM cliente WHERE nome = "{nome}"'
# cursor.execute(comando)
# conexao.commit()

# cursor.close()
# conexao.close()