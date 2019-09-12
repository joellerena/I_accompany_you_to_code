Algoritmo Armstrong 
	Escribir "Ingrese un número de 3 cifras: "
	Leer num
	u <- (num mod 10)
	d <- Trunc((num mod 100) / 10)
	c <- Trunc(num / 100)
	Escribir "Unidad: ",u
	Escribir "Decena: ",d
	Escribir "Centena: ",c
	Arms <- u*u*u + d*d*d + c*c*c
	Escribir "Número: ",num," = ",Arms
	Escribir "Es Armstrong!!!"
FinAlgoritmo
