'''
 ███╗   ███╗  █████╗  ██╗ ███╗   ██╗ 
 ████╗ ████║ ██╔══██╗ ██║ ████╗  ██║ 
 ██╔████╔██║ ███████║ ██║ ██╔██╗ ██║ 
 ██║╚██╔╝██║ ██╔══██║ ██║ ██║╚██╗██║ 
 ██║ ╚═╝ ██║ ██║  ██║ ██║ ██║ ╚████║ 
 ╚═╝     ╚═╝ ╚═╝  ╚═╝ ╚═╝ ╚═╝  ╚═══╝ 
 
  █████╗  ██╗ 
 ██╔══██╗ ██║ 
 ███████║ ██║ 
 ██╔══██║ ██║ 
 ██║  ██║ ██║ 
 ╚═╝  ╚═╝ ╚═╝ 
'''

 #-----L I B R A R I E S-----
from DATA import *
#-----L  O  C  A   L-----
import ___DataBase___ 
import telebot
from External_Code import anti_offence
from External_Code import Recommend
 # _ - _ - _ - _ - _ - _ - _ - _ - _ -


def Ai(text):
    reload(___DataBase___) 
    
    print ("Text : ",text)
            
    Answer=Data().Analyse_Function(text,DATA_intents(text))
    if not(not Answer and text!=""): return Answer 
    
    Answer=Data().ExtraAi(text)
    if (Answer!=False and text!=""): return Answer
    
    Answer=Data().Analyse_Closest(text,___DataBase___.DataBase)
    if (Data().WHQ(text) and text!="" and Answer): return Answer
    else : Data().AddToDataBase(text)

    Answer=(anti_offence.anti_offence(text))
    if (Answer!=False and text!=""): return Answer

    if text!="": Data().AddToDataBase(text)
    
    Message=Audio().IDK_Text_Return()+'|||'+Recommend.Rec(); return Message
    #return (Message,Audio().ApiLink(Message))

def Response_Voice(Text):
    return Audio().ApiLink(Text)    
    
def SendTelMes(Text):
    bot_token = '1367451572:AAHxjR9P7imVqNnQ_l0ea661Zl6LLDUF2Ps'
    bot_chatID = '-445001984'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + Text
    response = requests.get(send_text)
    print (response)


