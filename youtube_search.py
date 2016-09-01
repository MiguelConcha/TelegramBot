import urllib
import json

@bot.message_handler(commands=['yt'])
def command_youtube(m):
    cid = m.chat.id
    query = m.text[3:]
    # sustituir CLAVE API por tu API    
    link = urllib.urlopen("https://www.googleapis.com/youtube/v3/search?part=snippet&q=%s&key={CLAVE API}" % query)
    data = json.loads(link.read())
    """Coge un video aleatorio del primero al tercero,
    este rango se puede modificar o incluso dejar fijo"""
    rnd_no = random.randrange(0,3)
    id = data['items'][rnd_no]['id']['videoId'] 
    bot.send_message(cid, "http://www.youtube.com/watch?v=" + id)
    
@bot.message_handler(commands=['rickrolled'])
def command_rickrolled(rick):
    cid = m.chat.id    
    link = urllib.urlopen("https://www.googleapis.com/youtube/v3/search?part=snippet&q=rickrolled&key={CLAVE API}")
    data = json.loads(link.read())
    """Coge un video aleatorio del primero al quinto,
    este rango se puede modificar o incluso dejar fijo.
    Obviamente los videos encontrados serán los de Rickrolled."""
    rnd_no = random.randrange(0,5)
    id = data['items'][rnd_no]['id']['videoId'] 
    #Mandando el video al chat.
    bot.send_message(cid, "http://www.youtube.com/watch?v=" + id)