from flask import app, flash, request, redirect, render_template, session, url_for, Blueprint

userbp = Blueprint('user', __name__)

USER = [
	{
		'name': 'admin',
		'email': '2261108841@qq.com',
		'password': '123456'
	},
]


# 登陆路由
@userbp.route('/login', methods=['GET', 'POST'])
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
				# return render_template(url_for('main.index'))
				return redirect(url_for("main.index"))
			else:
				flash('邮箱或密码错误')
		return redirect(url_for("user.login"))


@userbp.route("/logout")
def logout():
	session.pop('user')
	return redirect(url_for("main.index"))


@userbp.route("/regist", methods=["GET", "POST"])
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
					return redirect(url_for('user.regist'))
			USER.append({
				'name': name,
				"email": email,
				"password": password
			})
			session['user'] = name
			# return render_template(url_for('main.index'))
			return redirect(url_for('main.index'))
		flash('密码不一致')
		return redirect(url_for('user.regist'))
