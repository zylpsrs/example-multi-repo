import os
import requests
from flask import Flask, request

_greeter   = "http://localhost:9082" if (os.environ.get("GREETER") is None) else os.environ.get("GREETER")
_port      = 9080 if (os.environ.get("PORT") is None) else os.environ.get("PORT")

app = Flask(__name__)

@app.route('/hello')
def hello():
    hello_to = request.args.get('To')
    messages=greeter(_greeter, 'To', hello_to)
    return "{}\n".format(messages)

def greeter(url, param, value):
    r = requests.get(url, params={param: value})
    assert r.status_code == 200
    return r.text

@app.route('/healthz')
def healthz():
    return 'OK!'

if __name__ == "__main__":
    app.run(host='::', port=_port, debug=True, threaded=True)
