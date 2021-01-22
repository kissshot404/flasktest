from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	name = 'kiss'
	return render_template('index.html',**locals())



if __name__ == '__main__':
	app.run(debug=True,host='192.168.11.7',port='8888')