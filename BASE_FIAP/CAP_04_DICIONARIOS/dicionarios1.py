#a representacao de um dicionario de dados é a chaves {}
usuarios ={}
usuarios={
    "Chaves":["Chaves Silva","17/06/2017","Recep_01"],
    "Quico":["Enrico FLores","03/06/2017","Raiox_02"]
}

#podemos adicionar objetos no dicionario
usuarios["Florinda"]=["Florinda Flores","26/11/2017","Recep_01"]

#podemos  retornar  os  dados  de  um  objeto  da  lista
print(usuarios)
print("##############========#########")
user = input("Digite o nome do usuario: ").lower().capitalize()
print("Dados: ",usuarios.get(user))