from flask import Flask
from flask import request
app = Flask(__name__)
import os
@app.route("/")
def hello():
    return "Hello leo!"
@app.route('/query-example')
def query_example():
    language = request.args.get('language') #if key doesn't exist, returns None

    return '''<h1>The language value is: {}</h1>'''.format(language)
if __name__ == "__main__":
    port = int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0', port=port)
