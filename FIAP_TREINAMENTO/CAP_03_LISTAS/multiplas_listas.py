# Ao inves de uma lista, podemos tambem criar varias listas, um para cada dado
equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = 's'
while resposta  == 's':
    equipamentos.append(input('Equipamento:  '))
    valores.append(float(input('Valor: ')))
    seriais.append(int(input('Numero Serial')))
    departamentos.append(input('Departamento: '))
    resposta = input('Digite \"s\" para continuar: ').lower()


# o for só vai mostrar os itens em equipamentos, pq apenas ele esta sendo printado. para exibir as outras listas podemos usar os indices 
for equipamento in equipamentos:
    print('Equipamento: ', equipamentos)



# Nossa estrutura mudou, agora estamos trabalhando na base do indice
for indice in range(0, len(equipamentos)): #funcao len() pega a qtd de elementos dentro da lista equipamentos
    print('\nEquipamento:', indice+1)
    print('Nome: ', equipamentos[indice])
    print('Valor: ', valores[indice])
    print('Serial: ', seriais[indice])
    print('Departamento', departamentos[indice])



# pesquisando na lista
busca = input('\nDigite o nome do equipamento que deseja buscar:')
for indice in range(0, len(equipamentos)):
    if equipamentos[indice] == busca: # quando o nome do equipamento for igual ao da busca
        print('Valor...:', valores[indice])
        print('Serial..:', seriais[indice])



#DESAFIOS:
# Situação 1: 
# todos  os  equipamentos  “impressora”  receberão uma depreciação (desvalorização após certo período) de 10%.Monte o código que  seria  responsável  por  alterar  o  valor  de  todos  os  equipamentos “impressora”.

# quando  igualamos  uma  lista (acompanhada  de  um índice),  sobrescrevemos o  conteúdo  do  dado  na  posição especificada pelo índice

busca_depreciacao = input('Digite o equipamento: ')
for indice in range(0, len(equipamentos)):
    if equipamentos[indice] == busca_depreciacao:
        print(f'Valor antes da depreciacao: R${valores[indice]}')
        valores[indice] = valores[indice] * 0.9
        print(f'Novo valor: R${valores[indice]}')



# Situação  2:
# um  equipamento  com  um  determinado  número  serial  foi danificado  e  será  descartado.  Precisamos  eliminar  esse equipamento.
# Dica:para  eliminar  um  item de  uma  lista, você  utilizará o comando “del”.
# Exemplo: del lista[<indice>]

busca_deletar = int(input('Digite o serial do equipamento para deletar: '))
for indice in range(0, len(equipamentos)):
    if seriais[indice] == busca_deletar:
        del seriais[indice]
        del equipamentos[indice]
        del valores[indice]
        del departamentos[indice]
        break

#o USO DO 'break':
# quando  ele  encontrar  o  valor  desejado  irá  excluir  o elemento da posição onde foi encontrado e depois irá sair do laço “for” (função do break).Isso porque, a partir do momento que excluímos um item, o índice poderá se perder,  pois  um  elemento  foi  excluído  e,consequentemente,o  contador  (laço)  foi quebrado.  O  comando  “break”  serve  também  para forçar  o  fimdos  laços  com  o comando “while”.