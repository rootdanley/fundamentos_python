def verificar_orcamento(salario, gastos):
    if gastos <= salario:
        print("Gastos dentro do orçamento")
    else:
        print("Orçamento estourado")

salario = float(input("Digite o valor do salário recebido: "))
gastos = float(input("Digite o total gasto com despesas: "))

verificar_orcamento(salario, gastos)
