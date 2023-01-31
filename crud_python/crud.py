#CRUD BÁSICO
import mysql.connector
from funcoes import *

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='proderj@123',
    database='locadora',
)


cursor = conexao.cursor()

resposta = 's'
while resposta != 'n':
    print('Digite a opcao:\n| INSERIR(I) \n| LEITURA(L) \n| ATUALIZAR(A) \n| DELETAR(D)')
    opcao = input('Resposta: ').lower()
    # CREATE
    if opcao == 'i':
        criar(cursor, conexao)

    #READ
    elif opcao == 'l':
        leitura(cursor, conexao)

    #UPDATE
    elif opcao == 'a':
        atualizar(cursor, conexao)

    #DELETE
    elif opcao == 'd':
        deletar(cursor, conexao)

    else:
        print('Opcao Invalida')

    resposta = input('Deseja continuar? [S] ou [N]').lower()









