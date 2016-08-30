@bot.message_handler(commands=['contar'])

def imprimir_diccionario(dictio):
	for keys, values in dictio.items():
		print(keys,":",values)

def command_repetir(m):
    diccionario = {}
    cid = m.chat.id
    texto = m.text[8:]
    for palabra in texto:
    	if palabra in diccionario:
			diccionario[x] += 1
		else:
			diccionario[x] = 1
	bot.send_message(cid, "Las ocurrencias de cada palabra en tu texto fueron:\n" + str(imprimir_diccionario(diccionario)))


