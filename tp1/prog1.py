import fonctions as f

while True:
	try:
		a = int(input("La base : "))
		b = int(input("L'exposant : "))
        
		resultat = f.puissance(a, b)
		print(f"{a} élevé à la puissance {b} est {resultat}")

	except KeyboardInterrupt:
		print("\nÀ bientôt !")
		break

	except TypeError as e:
		print(f"Erreur : {e}")
