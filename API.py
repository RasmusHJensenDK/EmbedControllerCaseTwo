import flask as fk
import threading


app = fk.Flask(__name__)
app.config["DEBUG"] = False

class APP(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    @app.route('/', methods=['GET'])
    def Home():
        return "<h1>TEST</h1>"

    @app.route('/Somethingelse', methods=['GET'])
    def NotHome():
        return "<h1>Something Else</h1>"

app.run()