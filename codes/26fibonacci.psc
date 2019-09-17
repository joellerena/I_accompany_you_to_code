Algoritmo fibonacci
	Escribir "Ingrese n: "
	Leer n
	a <- -1
	b <- 1
	Para i<-1 Hasta n Con Paso 1 Hacer
		c <- a + b
		Escribir c
		a <- b
		b <- c
	Fin Para
FinAlgoritmo
