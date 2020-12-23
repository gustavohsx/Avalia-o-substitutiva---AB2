perguntas = ["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?"]
cont = 0

print("Responda as perguntas com 'SIM' ou 'NÃO'.")
print("")

for i in range(len(perguntas)):
	print(perguntas[i])
	resp = input().upper()
	if resp == "SIM":
		cont += 1

print("Responde positivamente a: ", cont, " perguntas.")
print("")
print("CLASSIFICAÇÃO:")
if cont == 2:
	print("Supeita")
elif cont == 3 or cont == 4:
	print("Cúmplice")
elif cont == 5:
	print("Assassino")
else:
	print("Inocente")