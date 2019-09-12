Algoritmo residuo
	Escribir "Ingrese un número: "
	Leer n1
	Escribir "Ingrese otro número: "
	Leer n2
	cociente1 <- n1 / n2
	cociente2 <- TRUNC(n1 / n2)
	residuos <- (n1 MOD n2)
	Escribir "Cociente: ", cociente1
	Escribir "Cociente: ", cociente2
	Escribir "Residuo: ", residuos
FinAlgoritmo
