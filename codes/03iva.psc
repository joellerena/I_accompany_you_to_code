Algoritmo Total_a_pagar
	Escribir "Ingrese la cantidad del producto: "
	Leer cantidad
	precio <- 1
	subtotal <- cantidad * precio
	IVA <- subtotal * 0.12
	total <- subtotal + IVA
	Escribir "Subtotal: ",subtotal
	Escribir "IVA: ", IVA
	Escribir "Total: ", total
FinAlgoritmo
