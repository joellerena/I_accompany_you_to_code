Algoritmo mayorde3
	Escribir "Ingrese a: "
	Leer a
	Escribir "Ingrese b: "
	Leer b
	Escribir "Ingrese c: "
	Leer c
	Si a>b Entonces
		Si a>c Entonces
			Escribir a," es mayor"
		SiNo
			Escribir c," es mayor"
		Fin Si
	SiNo
		Si b>c Entonces
			Escribir b," es mayor"
		SiNo
			Escribir c," es mayor"
		Fin Si
	Fin Si
FinAlgoritmo
