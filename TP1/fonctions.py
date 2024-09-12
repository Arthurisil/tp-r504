def puiss(a, b):
	if type(a) is not  int or type(b) is not int:
		raise TypeError("Les arguments doivent être des entiers.")

	if b < 0:
		if a == 0:
			raise ZeroDivisionError("0 ne peut pas être élevé à une puissance négative.")
		raise ValueError("L'exposant doit être un entier positif ou zéro.")

	resultat = 1
	for _ in range(b):
		resultat *= a
		
	return resultat
