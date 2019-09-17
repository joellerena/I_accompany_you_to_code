Algoritmo parimpar
	Escribir "Ingrese su edad: "
	Leer edad
	Si (edad < 0) Entonces
		Escribir " eres bebé"
	SiNo
		Si (edad < 12) Entonces
			Escribir " eres niño"
		SiNo
			Si (edad < 18) Entonces
				Escribir " menor de edad"
			SiNo
				Si (edad < 25) Entonces
					Escribir " adolescente"
				SiNo
					Si (edad < 60) Entonces
						Escribir " adulto"
					SiNo
						Escribir " adulto mayor"
					Fin Si
				Fin Si
			Fin Si
		Fin Si
	Fin Si
FinAlgoritmo
