from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_word():
	return 'Hellowiord!'

app.run(host='0.0.0.0')
