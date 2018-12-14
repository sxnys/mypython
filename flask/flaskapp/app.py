from flask import Flask, request, url_for, render_template, flash, abort
from models import User

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/user', methods=['POST'])
def hello_user():
    return 'Hello User!'


# 通过路由获取参数
@app.route('/user/<name>')
def user_name(name):
    return 'hello user: %s' % name


# 通过request参数获取
@app.route('/query_user')
def query_User():
    id = request.args.get('id')
    return 'hello user: %s' % id


# 反向路由 —— 通过视图函数反导出url地址，url_for(view_function_name)
@app.route('/query_url')
def query_url():
    return 'query url: %s' % url_for('user_name', name='sxn')


''' ==========  下面的视图函数中使用模板  =========='''
''' 模板文件必须放在同目录下的templates目录下 '''
# 模板文件中使用普通变量
@app.route('/index')
def hello_world1():
    content = 'Hello World!'
    return render_template('index.html', content=content)


# 模板文件中使用对象
@app.route('/user_index')
def user_index():
    user = User(117106010747, '桑笑楠')
    return render_template('user_index.html', user=user)


# 模板文件中使用条件语句
@app.route('/query_user/<id>')
def query_user(id):
    user = None

    if int(id) == 1:
        user = User(1, '桑笑楠')

    return render_template('user_id.html', user=user)


# 模板文件中使用循环语句
@app.route('/users')
def user_list():
    users = [User(i, 'njust%d' % i) for i in range(1, 11)]

    return render_template('users.html', users=users)


# 模板继承
@app.route('/one')
def one_base():
    return render_template('one_base.html')


@app.route('/two')
def two_base():
    return render_template('two_base.html')


# 消息提示机制
app.secret_key = '123'   # 用于信息加密

@app.route('/login_index')
def login_index():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    flag = -1

    if not username:
        flag = 1
        flash('请输入用户名')
    elif not password:
        flag = 2
        flash('请输入密码')
    elif username == 'sxn' and password == '941205':
        flag = 3
        flash('登录成功')
    else:
        flag = 3
        flash('用户名或密码错误')

    return render_template('login.html', flag = flag)


# 异常处理机制
@app.errorhandler(404)
def not_found(e):
    print(e)
    return render_template('404.html')


# 主动抛出异常
@app.route('/games/<game_id>')
def games(game_id):
    if int(game_id) == 1:
        return render_template('games.html')
    else:
        abort(404)


if __name__ == '__main__':
    app.run()
