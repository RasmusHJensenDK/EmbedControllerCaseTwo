from Service import Service
import flask as fk
from flask import render_template, request, url_for, flash, redirect
import Service as svc
from werkzeug.exceptions import abort

app = fk.Flask(__name__)
app.config["DEBUG"] = False
app.config['SECRET_KEY'] = 'PillarsOfWisdom'

@app.route('/', methods=['GET'])
def Home():
    #Sender data igennem her - Her skal modtages data fra Servicen og opdatere siden.
    _Post = ["Test Title", "Test Created"]
    flash("Wtf is flash")
    return render_template('Web/index.html', posts=_Post)

@app.route('/Temperature/Room/<int:id>', methods=['GET'])
def Temp(id):
    newService = svc.Service(id, "Temp")
    if newService._Outcome() is None:
        abort(404)
    return newService._Outcome()

@app.route('/Sound/Room/<int:id>', methods=['GET'])
def Sound(id):
    newService = svc.Service(id, "Sound")
    if newService._Outcome() is None:
        abort(404)
    return newService._Outcome()

@app.route('/AabnVinduer/Room/<int:id>', methods=['GET'])
def AabnVinduer(id):
    newService = svc.OpenWindows(id)
    if newService._Outcome() is None:
        abort(404)
    return newService._Outcome()

app.run()