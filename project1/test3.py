from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)

TESTS = [
	{
		'id': 1,
		'name': 'kissshot',
		'content': 'kissshot·acerolaorion·heartunderblade'
	},
	{
		'id': 2,
		'name': '冷血的',
		'content': '《物语系列》是由日本轻小说作家西尾维新创作、中国台湾插画家VOFAN（本名戴源亨）负责插画的轻小说系列，分为First Season、Second Season、Final Season、Off Season和Monster Season五季。'
	},
	{
		'id': 3,
		'name': '热血的',
		'content': '作品以21世纪初的日本直江津镇为舞台，描述一名高中少年阿良良木历与少女们遇到许多日本民间传说的怪谭故事。本作品跟一般怪谭故事不同，不以击退妖怪或寻找事发原因之类的解谜作为主线。作品主要透过对话，为男主角和少女们之间的内心作深刻描写。'
	},
	{
		'id': 4,
		'name': '铁血的',
		'content': '西尾维新以其特有的“话痨”风格，将大量的对话和心理描写穿插到主线事件中，同时还加入了许多后设以及对社会和其他作品的讽刺。故事之中既有恋爱喜剧，又有热血的动作描写，可见作者把想要的东西都写进作品中去。所以，作者将“物语系列”自评本作为他的自信作，亦称之为“以很难媒体化为目的而写的小说”。'
	},
]

USER = [
	{
		'name': 'admin',
		'email': '2261108841@qq.com',
		'password': '123456'
	},
]

app.secret_key = 'qsdfghasidoahsoiahdiaoshjoiafswahfioahfiowa'


@app.route('/')
def index():
	tests = TESTS

	return render_template('index.html', **locals())


@app.route('/<int:pk>/')
def default(pk):
	test = TESTS[pk - 1]
	return render_template('detault.html', **locals())


# 登陆路由
@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'GET':
		return render_template('login.html', **locals())
	elif request.method == 'POST':
		email = request.form.get('email')
		password = request.form.get('password')
		for u in USER:
			if u['email'] == email and u['password'] == password:
				session['user'] = u['name']
				return redirect(url_for("index"))
			else:
				flash('邮箱或密码错误')
		return redirect(url_for("login"))


@app.route("/logout")
def logout():
	session.pop('user')
	return redirect(url_for("index"))


@app.route("/regist", methods=["GET", "POST"])
def regist():
	if request.method == "GET":
		return render_template("regist.html", **locals())
	elif request.method == "POST":
		name = request.form.get('name')
		email = request.form.get("email")
		password = request.form.get("password")
		password1 = request.form.get("password1")
		if password == password1:
			for i in USER:
				if i['email'] == email:
					flash('邮箱重复')
					return redirect(url_for('regist'))
			USER.append({
				'name': name,
				"email": email,
				"password": password
			})
			session['user'] = name
			return redirect(url_for('index'))
		flash('密码不一致')
		return redirect(url_for('regist'))


if __name__ == '__main__':
	app.run(debug=True, host='192.168.11.7', port='8888')
