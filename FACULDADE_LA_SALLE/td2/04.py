

def verificar_ano_bissexto(ano):
    if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
        print(ano, "é um ano bissexto!")
    else:
        print(ano, "não é um ano bissexto!")
        
ano = int(input("Digite um ano: "))

verificar_ano_bissexto(ano)
