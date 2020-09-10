'''

  █████╗  ██████╗  ██╗ 
 ██╔══██╗ ██╔══██╗ ██║ 
 ███████║ ██████╔╝ ██║ 
 ██╔══██║ ██╔═══╝  ██║ 
 ██║  ██║ ██║      ██║ 
 ╚═╝  ╚═╝ ╚═╝      ╚═╝ 

 ████████╗ ███████╗ ██╗      
 ╚══██╔══╝ ██╔════╝ ██║      
    ██║    █████╗   ██║      
    ██║    ██╔══╝   ██║      
    ██║    ███████╗ ███████╗ 
    ╚═╝    ╚══════╝ ╚══════╝ 

'''

#-----M   A   I   N-----
from MainAiFunction import *
from os import remove
from telegram.ext import *



updater = Updater('1294204553:AAFPV-LXjFvr2aTAgH3S9nMdIbAYwiGx5Fs', use_context=True)


def unknown(update, context):
    Answer=Ai(update.message.text)
    SendTelMes(str("Telegram : "+str(update.message.text)))
    print (Answer)
    update.message.reply_text(Answer[0])
    with open("Audios/Talks/Telegram/Talk.mp3",'wb') as f:
        Response = requests.get(Answer[1])
        f.write(Response.content)


    
    update.message.reply_voice(open("Audios/Talks/Telegram/Talk.mp3","rb"))
    remove('Audios/Talks/Telegram/Talk.mp3')
    
    
unknown_handler = MessageHandler(Filters.text , unknown)

updater.dispatcher.add_handler(unknown_handler)

updater.start_polling()






