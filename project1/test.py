from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return 'Hello World!'

@app.route('/<int:pk>')
def detail(pk):
	return f'Hello World!{pk}'


if __name__ == '__main__':
	app.run(debug=True,host='192.168.11.7',port='8888')