def puiss(a, b):
	if not type(a) is int or not type(b) is int:
		raise TypeError("Only integers are allowed")
	if b < 0:
		if a == 0:
			raise ZeroDivisionError("0 ne peut pas être élevé à une puissance négative.")
		raise ValueError("L'exposant doit être un entier positif ou zéro.")

	resultat = 1
	for _ in range(b):
		resultat *= a
		
	return resultat
