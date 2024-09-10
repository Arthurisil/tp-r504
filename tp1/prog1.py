
while True:
	try:
		nombre = float(input("Entrez un nombre : "))
		carre = nombre ** 2
		print(f"Le carré de {nombre} est {carre}")
	except KeyboardInterrupt:
		print("\nÀ bientôt !")
		break
