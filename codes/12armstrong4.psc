Algoritmo Armstrong 
	Escribir "Ingrese un número de 4 cifras: "
	Leer num
	u <- (num mod 10)
	d <- Trunc((num mod 100) / 10)
	c <- Trunc(num / 100 ) mod 10
 	m <- Trunc(num / 1000 )
	Escribir "Unidad: ",u
	Escribir "Decena: ",d
	Escribir "Centena: ",c
	Escribir "Miles: ",m
	Arms <- u*u*u*u + d*d*d*d + c*c*c*c + m*m*m*m
	Escribir "Número: ",num," = ",Arms
	Escribir "Es Armstrong!!!"
FinAlgoritmo
