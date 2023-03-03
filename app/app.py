
import flask
app = flask.Flask(__name__)
@app.route("/")
def hw():
    return "hw"
app.run(host = "0.0.0.0", port=8000)
