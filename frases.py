@bot.message_handler(commands=['calc'])
def command_calc(m):
    cid = m.chat.id
    token = m.text[5:].split()
    if len(token) < 3:
        if token[2] is '+':
            bot.send_message(cid, token[1] + "+" +  token[2] + " = " + (int(token[1]) + int(token[2])))
        elif token[2] is '-':
            bot.send_message(cid, token[1] + "-" +  token[2] + " = " + (int(token[1]) - int(token[2])))
        elif token[2] is '*':
            bot.send_message(cid, token[1] + "*" +  token[2] + " = " + (int(token[1]) * int(token[2])))
        elif token[2] is '/':
            bot.send_message(cid, token[1] + "/" + token[2] + " = " + (int(token[1]) / int(token[2])))
        elif token[2] is '%':
            bot.send_message(cid, token[1] + "%" + token[2] + " = " + (int(token[1]) % int(token[2])))
    else:
        bot.send_message("Tienen que ser operaciones binarias.\nNo puedo operar tres elementos.")
