# “Declaro  para  o  senhor  Gonçalves  Dias  que  o  senhor  Humberto  Delgado esteve  presente  no  evento  SecurityCup  e  gastou  o  valor  de  R$  30,00  com  a entrada.”Identifique  o  que  pode  ser  variável  no  texto  acima  e  monte  um  projeto  no Python.


responsavel = input('Digite o responsavel: ')
funcionario = input('Digite o funcionario: ')
evento = input('Digite o nome do evento: ')
valor = float(input('Digite o valor do evento: '))


print(f'Declaro para o senhor {responsavel}, que o senhor(a) {funcionario} esteve presente no evento, {evento} e gastou um valor de R${valor} com a entrada.')