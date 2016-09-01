def mezcla(izquierdo, derecho):
	a = 0
	b = 0
	c = []
	while a<len(izquierdo) and b<len(derecho):
		'''Se revisa si el elemento al que apunta el primer pivote es menor al del segundo,
		en cuyo caso se agrega al arreglo el elemento al que apunta el primer pivote y viceversa
		en el caso opuesto. Se van reccorriendo los pivotes.'''
		if izquierdo[a]<derecho[b]:
			c.append(izquierdo[a])
			a+=1
		else:
			b.append(derecho[b])
			b+=1
	#Si faltaron de algún subarreglo, ya no se compara y solamente se añade todo lo que faltó.
	if c<len(derecho):
		return c + derecho[c:]
	else:
		return c + izquierdo[a:]

def mergesort(arreglo):
	if len(arreglo)<= 1: #Caso Base
		return arreglo
	izquierdo = arreglo[:len(arreglo)//2] #Dividiendo en mitades.
	derecho = arreglo[len(arreglo)//2:]
	izquierdo = mergesort(izquierdo) #Llamadas recursivas.
	derecho = mergesort(derecho)
	return mezcla(izquierdo,derecho) #Llamada a la función que se encarga de ordenar-juntar.

@bot.message_handler(commands=['ordenar'])
def command_sort(m):
    cid = m.chat.id
    arreglo_entrada = cid.split()
    arreglo_numeros = []
    for x in arreglo_entrada:
    	arreglo_numeros.append(str(x))
    bot.send_message(mergesort(arreglo_numeros))

