Algoritmo primo
	num <- 1
	cont <- 0
	Mientras (num <= 100) Hacer
		p <- num
		i <- 1
		Mientras (i <= p) Hacer
			r <- trunc(p mod i)
			Si (r == 0) Entonces
				cont <- cont + 1
			Fin Si
			i <- i + 1
		Fin Mientras
		Si (cont <= 2) Entonces
			Escribir p
		Fin Si
		cont <- 0
		i <- 0
		num <- num + 1
	Fin Mientras
FinAlgoritmo
