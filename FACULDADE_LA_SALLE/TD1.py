# Autor: Danley Alves
# Data: 09-02-2023
# Disciplina: Desenvolvimento Web III

# 1. Escreva um programa que imprima 2 números de sua escolha e que depois
# imprima a soma, a subtração, multiplicação, divisão, divisão inteira, o resto da
# divisão do maior pelo menor e coloque na mensagem a palavra resto ao invés de
# símbolo %.

num_um = int(input('Digite o numero um: '))
num_dois = int(input('Digite o numero um: '))

def calculo(num_um, num_dois):
    maior = 0
    menor = 0    
    if num_um > num_dois:
        maior = num_um
        menor = num_dois
    else:
        maior = num_dois
        menor = num_um
    
    print(f'A soma dos numeros = {maior+menor}')
    print(f'A subtracao dos numeros = {maior-menor}')
    print(f'A multiplicacao dos numeros = {maior*menor}')
    print(f'A divisao dos numeros = {maior/menor}')
    print(f'A divisao inteira dos numeros = {maior//menor}')
    print(f'O resto divisao inteira dos numeros = {maior%menor}')

calculo(num_um,num_dois)


# 2. Faça um programa que peça as 4 notas bimestrais e mostre a média do aluno

notas = []
for indice in range(0,4,1):
    notas.append(float(input('Digite nota')))

total = sum(notas)

print(f'A media do aluno: {total/4}')

# 3. Crie um script Python que leia o dia, mês e ano de nascimento de uma pessoa e
# mostre uma mensagem com a data formatada.

data = []
aniversario =[]

for indice in range(0,1,1):
    data = [int(input('Digite o dia:')),
            int(input('Digite o mes:')),
            int(input('Digite o ano:'))
            ]
    
    aniversario.append(data)

for elemento in aniversario:
    print(f'{elemento[0]}/{elemento[1]}/{elemento[2]}')
