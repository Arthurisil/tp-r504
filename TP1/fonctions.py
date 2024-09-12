def puiss(a, b):
	if type(a) not in (int, float) or type(b) not in (int, float):
		raise TypeError("Les arguments doivent être des entiers.")

	if b < 0:
		if a == 0:
			raise ZeroDivisionError("0 ne peut pas être élevé à une puissance négative.")
		return 1 / puiss(a, -b)

	resultat = 1
	for _ in range(b):
		resultat *= a

	if b != int(b):
		return resultat * (a ** (b - int(b)))
		
	return resultat
