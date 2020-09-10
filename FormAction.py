
from flask import Flask, render_template, request,redirect
from time import sleep
import threading
from MainAiFunction import *

def Adder(Tag,Writer,MustBe,First,Secound,Answer,Action):
    


    A='        {'+'''"Tag": '{}','''.format(Tag)
    A_='''        "Writer": '{}','''.format(Writer)
    B='''        "MustBeKeywords": {},'''.format(MustBe)
    C='''        "FirstLayerKeywords": {},'''.format(First)
    D='''        "SecoundLayerKeywords": {},'''.format(Secound)
    E='''        "Answers": {},'''.format(Answer)
    F='''        "Actions": {},'''.format(Action)
    G='        },'
    
    A=(A+'\n')
    A_=(A_+'\n')
    B=(B+'\n')
    C=(C+'\n')
    D=(D+'\n')
    E=(E+'\n')
    F=(F+'\n')
    G=(G+'\n\n\n')
    Block=A+A_+B+C+D+E+F+G
    
    a_file = open("DATA.py", "r")
    list_of_lines = a_file.readlines()
    Length = (len(list_of_lines))
    list_of_lines[Length-2-1] = Block

    a_file = open("DATA.py", "w")
    a_file.writelines(list_of_lines)
    a_file.close()

app=Flask (__name__,static_url_path="/static")

@app.route('/Update', methods=['POST'])
def handle_data():
    global FormMessage
    FormMessage=''
    Tag = request.form.get('Tag') 
    MustBe = request.form.get('MustBe') 
    First = request.form.get('First')  
    Secound = request.form.get('Secound')  
    Answer = request.form.get('Answer')  
    Action = request.form.get('Action')  
    Writer = request.form.get('Writer')
    if Tag=="":
        FormMessage+=' '+'Tag is an essential '
    if First=="":
        FormMessage+=' '+'FirstLayer is an essential'
    if Answer == '' and Action=='':
        FormMessage+=' '+'At least one of [Action,Answer] must be filled'
    if Writer=='':
        FormMessage+=' '+'Writer is an essential'
    if Writer not in ['Ali','Mehrshad','Parsa']:
        FormMessage+=' '+"Writer must be one of ['Ali','Mehrshad','Parsa']"
    if MustBe=="": MustBe='[]'
    if Secound=="": Secound='[]'
    if Answer=="": Answer='[]'
    if Action=="": Action='[]'
    if FormMessage=='':
        
        FormMessage="--- Fine ---"
        Adder(Tag,Writer,MustBe,First,Secound,Answer,Action)
        SendTelMes(str('Added Block : '+Tag+Writer+MustBe+First+Secound+Answer+Action))

    
    
    return redirect('/')

   
   
@app.route('/', methods=['post', 'get'])
def Main(Message=""):
    def Delete():
        sleep(0.001)
        global FormMessage
        del FormMessage
    
    if "FormMessage" in globals():

        x = threading.Thread(target=Delete, args=())
        x.start()
        return render_template('index.html', message=FormMessage)
    else:
        return render_template('index.html', message='')
    
if __name__== '__main__':
    #app.send_static_file("index.html")
    app.run(debug=True,port=9999)
