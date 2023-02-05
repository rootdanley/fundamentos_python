def preencher_inventario(lista):
    resp = 's'
    while resp == 's':
          equipamento = [input('Equipamento:'),
                   float(input('Valor:')),
                   int(input('Numero serial:')),
                   input('Departamento')]
    lista.append(equipamento)
    resp= input('Digite \"s\" para continuar: ').lower()


def exibir_inventario(lista):
     for elemento in lista:
        print("Nome.........: ", elemento[0])
        print("Valor........: ", elemento[1])
        print("Serial.......: ", elemento[2])
        print("Departamento.:",  elemento[3])
        print('\n') 

def localizar_por_nome(lista):
    busca=input("\nDigite o nome do equipamento que deseja buscar: ")
    for elemento in lista:
        if busca==elemento[0]:
            print("Valor..: ", elemento[1])
            print("Serial.:", elemento[2])

def depreciar_por_nome(lista, porcentagem):
    depreciacao=input("\nDigite o nome do equipamento que será depreciado: ")
    for elemento in lista:
        if depreciacao==elemento[0]:
            print("Valor antigo: ", elemento[1])
            elemento[1] = elemento[1] * (1-porcentagem/100)
            print("Novo valor: ", elemento[1])

def excluir_por_serial(lista):
    serial=int(input("\nDigite o serial do equipamento que será excluído: "))
    for elemento in lista:
        if elemento[2]==serial:
            lista.remove(elemento)
    return "** ITENS EXCLUIDOS **"

# A  função  excluir_por_serial()  retorna  uma string,  ou  seja,  quando  formos chamar  essa função,  devemos  fazê-la  dentro  de  um  comando  print(),  para  que possamos ver a mensagem

def resumir_valores(lista):
    for elemento in lista:
        print("Nome.........: ", elemento[0])
        print("Valor........: ", elemento[1])
        print("Serial.......: ", elemento[2])
        print("Departamento.:",  elemento[3])