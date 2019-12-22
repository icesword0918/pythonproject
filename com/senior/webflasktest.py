# 第一个flask程序
from flask import Flask,url_for
import requests
app=Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'
# 变量规则
@app.route('/user/<username>')
def shou_user_profile(username):
    # 显示改用户名的用户信息
    return 'User %s' % username
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # 根据ID显示文章，DI是整型数据
    return 'Post %d' % post_id

#构造url
@app.route('/url/')
def get_url():
    # 根据ID显示文章，ID是整型数据
    return url_for('show_post',post_id=2)

# http方法
def do_the_login():
    pass


def show_the_login_from():
    pass


@app.route('/login',methods=['GET','POST'])
def login():
    if requests.method=='POST':
        do_the_login()
    else:
        show_the_login_from()

if __name__=='__main__':
    app.run(debug=True)