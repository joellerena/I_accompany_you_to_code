Algoritmo ulam1
	Escribir "Ingrese un número: "
	Leer n
	Mientras n > 1 Hacer
		Si (n mod 2 == 0) Entonces
			n <- n / 2
		SiNo
			n <- n * 3 + 1
		Fin Si
		Escribir n
	Fin Mientras
FinAlgoritmo
