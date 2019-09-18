Algoritmo ruso
	Escribir "Ingrese un n1: "
	Leer n1
	Escribir "Ingrese un n2: "
	Leer n2
	Mientras n1 >= 1 Hacer
		Escribir n1," ",n2
		Si ((n1 mod 2) == 1) Entonces
			acum <- acum + n2
		Fin Si
		n1 <- trunc(n1 / 2)
		n2 <- n2 * 2
	Fin Mientras
	Escribir acum
FinAlgoritmo
