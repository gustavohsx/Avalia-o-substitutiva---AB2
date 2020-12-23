print("Você pode ser doador de sangue?")
idade = int(input("Quantos anos você tem? "))

if idade < 16:
	print("Impedimento: menor de 16 anos.")
elif idade > 69:
	print("Impedimento: maior de 69 anos.")
elif 16 <= idade < 18:
	print("Restrição: requer autorização do responsável.")
elif 60 <= idade <= 69:
	print("Restrição: não pode ser a primeira doação.")
else:
	print("Sem impedimentos ou restrições.")