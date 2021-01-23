from flask import app, render_template, Blueprint

mainbp = Blueprint('main', __name__)

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


@mainbp.route('/')
def index():
	tests = TESTS

	return render_template('index.html', **locals())


@mainbp.route('/<int:pk>/')
def default(pk):
	test = TESTS[pk - 1]
	return render_template('detault.html', **locals())
