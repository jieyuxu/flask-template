from flask import Flask

app = Flask(__name__)

@app.route("/") 
def home():
	return "hello it's me."

@app.route("/cat")
def cat():
	return "hello it's me, the kitty."

@app.route("/whale")
def whale():
	return "whale are you now that I need ya"

if __name__ == "__main__":
        app.run()
