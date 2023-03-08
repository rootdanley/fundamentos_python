# Escreva um programa em python utilizadno funçoes que leia a capacidade de um elevador e o peso de 5
# pessoas. Informar se o elevador está liberado para subir ou se excedeu a carga
# máxima.


def verificar_elevador(capacidade_elevador, pesos_pessoas):
    peso_total = sum(pesos_pessoas)
    if peso_total <= capacidade_elevador:
        print("Elevador liberado para subir!")
    else:
        print("Excedeu a carga máxima do elevador!")
        
capacidade = int(input("Digite a capacidade do elevador: "))
pesos = []
for i in range(5):
    peso = int(input("Digite o peso da pessoa {}: ".format(i+1)))
    pesos.append(peso)

verificar_elevador(capacidade, pesos)
