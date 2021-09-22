import flask as fk 
from flask import render_template, request, url_for, flash, redirect
import Service as svc
from werkzeug.exceptions import abort
from Measurement import Temp as tp

app = fk.Flask(__name__)
app.config["DEBUG"] = False
app.config['SECRET_KEY'] = 'PillarsOfWisdom'

@app.route('/', methods=['GET'])
def Home():
    newRooms = svc.get_rooms()
    newDevices = svc.get_devices()
    _FirstThree = []
    _SecondThree = []
    _Devices = []
    _MeasuredTemperatureList = []
    for item in newRooms[:3]:
        _FirstThree.append(item)
    for item in newRooms[3:6]:
        _SecondThree.append(item)
    for item in newDevices:
        _Temperature = tp.Temperature(item)
        _MeasuredTemperature = _Temperature.get_temp()
        _MeasuredTemperatureList.append(_MeasuredTemperature)
        _Devices.append(item)
    return render_template('index.html', devices = _FirstThree, secondDevices = _SecondThree, thirdDevices = _Devices, temps = _MeasuredTemperatureList)

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
    if newService.outcome is None:
        abort(404)
    return newService.outcome()

app.run()