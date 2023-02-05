inventario = []
resposta = 's'
while resposta == 's':
    inventario.append(input('Equipamento: '))
    inventario.append(float(input("Valor:")))
    inventario.append(int(input('Numero serial:')))
    inventario.append(input('Departamento:'))
    resposta = input('Digite \"s\" para continuar: ').lower()

# EXPLICANDO:
# Utilizamos o 'while' para o usuario continuar adicionando dados na lista ate ele digitar 'n'.
# o metodo append é responsavel por adicionar os dados na lista



for elemento in inventario:
    print(elemento)

# EXPLICANDO:
# Usando o for conseguimos percorrer a lista e exibir tudo que está nela.
# A cada incrimento, o item da lista(indice) é passado para a variavel 'elemento' que é printada na tela