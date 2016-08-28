@bot.message_handler(commands=['ordenar'])
def command_sort(m):
    cid = m.chat.id
    bot.send_message(bubble_sort(cid))

def bubble_sort(x):
	s = len(x)
    for i in range(0, s):
        for j in range(i, s):
            if x[i]>x[j]:
                x[i], x[j] = x[j], x[i]
    return x
