# config                    
#from flask import Flask
#app = Flask(__name__)

#@app.route('/')
#def index2():
    #return 'Hello world!!!'

#@app.route('/pets')
#def pets():
    #return 'This is where we keep our pets info'

from petfax import create_app
app = create_app()
