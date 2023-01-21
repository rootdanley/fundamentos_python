def criar(cursor, conexao):
    nome_filme = input('Digite o nome do filme: ')
    ano_filme = input('Digite o ano de lançamento:')

    comando = f'INSERT INTO filme (nome_filme, ano_filme) VALUES ("{nome_filme}", "{ano_filme}")'
    cursor.execute(comando)
    conexao.commit()

#CRIAR BUSCAR MAIS APROFUNDADA
def leitura(cursor, conexao):
    comando = f'SELECT * FROM filme'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    print(resultado)

    cursor.close()
    conexao.close()

def atualizar(cursor, conexao):
    nome_novo = input('Digite o novo nome do filme:')
    nome_antigo = input('Digite o antigo nome:')

    comando = f'UPDATE filme SET nome_filme = "{nome_novo}"  WHERE nome_filme = "{nome_antigo}"'
    cursor.execute(comando)
    conexao.commit()

    cursor.close()
    conexao.close()

def deletar(cursor, conexao):
    nome = input('Digite o nome do filme para excluir:')

    comando = f'DELETE FROM filme WHERE nome_filme = "{nome}"'
    cursor.execute(comando)
    conexao.commit()

    cursor.close()
    conexao.close()

