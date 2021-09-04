
import os

from flask import Flask,jsonify
import json

app = Flask(__name__)

local_version = "0.01"

@app.route("/")
@app.route("/<name>")
def hello_world(name = "World"):
    return "<H2>Hello {}!</h2>".format(name)


@app.route("/version")
def version():
    return jsonify({"version":local_version})

@app.route("/fuka")
def fuka():
    def fibo2():
        slowfibo(2)
    def fibo20():
        slowfibo(20)
    def fibo30():
        slowfibo(30)
    fibo20()
    fibo2()
    fibo30()
    return "There is something high loaded by slow fibo"
    
def slowfibo(n):
	if n < 2 :
		return n
	return slowfibo(n-2) + slowfibo(n-1)
    
        
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))