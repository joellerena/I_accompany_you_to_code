Algoritmo mayorde3
	Escribir "Ingrese a: "
	Leer a
	Escribir "Ingrese b: "
	Leer b
	Escribir "Ingrese c: "
	Leer c
	Si (a>b)Y(a>c) Entonces
		Escribir a," es mayor"
	SiNo
		Si (b>a)Y(b>c) Entonces
			Escribir b," es mayor"
		SiNo
			Si (c>a)Y(c>b) Entonces
				Escribir c," es mayor"
			SiNo
				Escribir " son iguales"
			Fin Si
		Fin Si
	Fin Si
FinAlgoritmo
