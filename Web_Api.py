"""
 ███╗   ███╗  █████╗  ██╗ ███╗   ██╗ ██╗ 
 ████╗ ████║ ██╔══██╗ ██║ ████╗  ██║ ██║ 
 ██╔████╔██║ ███████║ ██║ ██╔██╗ ██║ ██║ 
 ██║╚██╔╝██║ ██╔══██║ ██║ ██║╚██╗██║ ╚═╝ 
 ██║ ╚═╝ ██║ ██║  ██║ ██║ ██║ ╚████║ ██╗ 
 ╚═╝     ╚═╝ ╚═╝  ╚═╝ ╚═╝ ╚═╝  ╚═══╝ ╚═╝ 
"""

#-----M   A   I   N-----
from MainAiFunction import *
 # _ - _ - _ - _ - _ - _ - _ - _ - _ -
from flask import Flask, render_template, request
import os

from flask_cors import CORS,cross_origin
from flask import send_file
import string
from flask import *


app=Flask (__name__,static_folder='static')
cors = CORS(app, resources={r"*": {"origins": "*"}})
@app.route("/Text/<message>", methods=['GET'])
def Text_Api(message):
    #SendTelMes("Web : "+str(message))
    return str(Ai(message))


@app.route("/<message>/", methods=['GET'])
def None_Api(message):
    if message=='Text':
       return 'پیام خالی جوابی نداره : )'
   
@app.route("/<message>", methods=['GET'])
def None_Api2(message):
    if message=='Text':
       return 'پیام خالی جوابی نداره : )'

@app.route("/Voice/<message>", methods=['GET'])
def Voice_Api(message):
    return Response_Voice(message)

if __name__== '__main__':
    app.run(debug=True, port=2223)












#@app.route('/Media/music/<filename>', methods=['GET', 'POST'])
#def Music(filename):
#    return send_file('static//Media/music/'+filename, as_attachment=True)
#
#@app.route('/Media/gif/<filename>', methods=['GET', 'POST'])
#def gif(filename):
#    return send_file('static//Media/gif/'+filename, as_attachment=True)
#
#@app.route('/Media/images/<filename>', methods=['GET', 'POST'])
#def images(filename):
#    return send_file('static//Media/images/'+filename, as_attachment=True)
#
#@app.route('/Media/instrumental/<filename>', methods=['GET', 'POST'])
#def instru(filename):
#    return send_file('static//Media/instrumental/'+filename, as_attachment=True)
#@app.route('/Media/nature_sounds/<filename>', methods=['GET', 'POST'])
#def nature(filename):
#    return send_file('static//Media/nature_sounds/'+filename, as_attachment=True)










#return Ai(message)[0]+'@'+'sec  i am'+'@'+"http://del.shiksong.ir/Mp3-Music/En/Mordad-98/DJ%20Shadow%20-%20'Rocket%20Fuel'%20MP3%20-%20ShikSong.mp3"+'@'+'https://ondemo.tmsimg.com/assets/p14185147_bd_h8_aa.jpg'+'@'+'https://hw19.cdn.asset.aparat.com/aparat-video/5ca1d475b2d89981a1f85b7b602a9bf224963964-1080p.mp4'+'@'+'href,'+'سلاااااااااام'+','+'https://app.madadbot.ir'
