'''
这个网页是用来测试验证码功能的，已测试成功
'''
from flask import Flask, render_template, request, url_for, redirect, session,views
from pymongo import MongoClient
from flask_wtf import CSRFProtect
import random
import time
import auth, costants,data_storing,data_acquisition,data_delete,data_update
from io import BytesIO
from flask import Blueprint, make_response, session
from utility import ImageCode

# from module.users import Users
from threading import Thread
import os
from authlogin import login_required
# import bcrypt
# set app as a Flask instance
app = Flask(__name__)
# encryption relies on secret keys so they could be run
app.secret_key = "testing"
CSRFProtect(app)
user = Blueprint('user', __name__)
# #connect to your Mongo DB database
def MongoDB():
    # client = MongoClient("mongodb+srv://xmj_jessie:123098111@cluster0.ohtke6p.mongodb.net/?retryWrites=true&w=majority")
    # client = MongoClient("mongodb+srv://newuserhello:IoTproject@cluster0.ohtke6p.mongodb.net/?retryWrites=true&w=majority")

    client = data_storing.connect_cluster_mongodb(
        costants.CLUSTER_NAME, auth.MONGODB_USERNAME, auth.MONGODB_PASSWORD
    )
    db = client.get_database('security')
    records = db.user
    return records


records = MongoDB()


##Connect with Docker Image###
# def dockerMongoDB():
#     client = MongoClient(host='test_mongodb',
#                             port=27017,
#                             username='root',
#                             password='pass',
#                             authSource="admin")
#     db = client.users
#     pw = "test123"
#     hashed = bcrypt.hashpw(pw.encode('utf-8'), bcrypt.gensalt())
#     records = db.register
#     records.insert_one({
#         "name": "Test Test",
#         "email": "test@yahoo.com",
#         "password": hashed
#     })
#     return records

# records = dockerMongoDB()

# pw = "test123"
# hashed = bcrypt.hashpw(pw.encode('utf-8'), bcrypt.gensalt())
# records.insert_one({
#         "name": "Test Test",
#         "email": "test@yahoo.com",
#         "password": hashed
#     })

# assign URLs to have a particular route
@app.route("/",methods=["POST", "GET"])
def index():
    message='请登录'
    Vcode=request.form.get("Vcode")
    print(Vcode)
    print(session.get('image'))
    if Vcode:
        if session.get('image') != Vcode:
            message = '验证码错误'
            print('错误')
            return render_template("image.html", message=message)
        else:
            message = '验证码正确'
            print('正确')
            return render_template("image.html", message=message)
    else:
        return render_template("image.html", message=message)




@app.route('/vcode')
def vcode():
    image, str = ImageCode().draw_verify_code()
    # print(code,bstring)
    buf = BytesIO()
    image.save(buf, 'jpeg')
    buf_str = buf.getvalue()
    # 把二进制作为response发回前端，并设置首部字段
    response = make_response(buf_str)
    response.headers['Content-Type'] = 'image/gif'
    # 将验证码字符串储存在session中
    session['image'] = str
    return response


@app.route("/login", methods=["POST", "GET"])
def login():
    message = 'Please login to your account'
    if "email" in session:
        return redirect(url_for("logged_in2"))

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        # check if email exists in database
        email_found = records.find_one({"email": email})
        if email_found:
            email_val = email_found['email']
            passwordcheck = email_found['password']
            # encode the password and check if it matches
            # if bcrypt.checkpw(password.encode('utf-8'), passwordcheck):
            if password == passwordcheck:
                session["email"] = email_val
                return redirect(url_for('logged_in2'))
            else:
                if "email" in session:
                    return redirect(url_for("logged_in2"))
                message = 'Wrong password'
                return render_template('login.html', message=message)
        else:
            message = 'Email not found'
            return render_template('login.html', message=message)
    return render_template('login.html', message=message)


@app.route('/logged_in2')
def logged_in2():
    if "email" in session:
        email = session["email"]
        # 因为登录的时候用的email和密码所以session里只有这些
        # 也需要将表格数据刷新
        row = data_acquisition.acquire_data_from_message()
        # data = data_acquisition.acquire_data_from_message(conditionproduct={"nikename":"mike"})
        # print(data)
        # return render_template('logged_in2.html', data=row)
        return render_template('logged_in2.html', email=email,data=row)
    else:
        return redirect(url_for("login"))


@app.route("/logout", methods=["POST", "GET"])
def logout():
    if "email" in session:
        session.pop("email", None)
        return render_template("signout.html")
    else:
        return render_template('index.html')



# 定义视图 显示留言添加的页面，这里类似于转账那个界面根据那个逻辑来
@app.route('/add1')
def add():
    # 看一下怎么阻止直接访问
    if session.get("email"):
        # 当前处于登陆状态
        print(session.get('email'))
        return render_template('add.html')
    else:
        # 加一个请先登录？？？
        return redirect(url_for("login"))


# 定义视图函数 接收表单数据，完成数据的入库，这里类似于转账那个界面根据那个逻辑来
@app.route('/insert', methods=['POST'])
def insert():
    # 1.接收表单数据
    data_dict = request.form.to_dict()
    print(data_dict['info'])
    data_info=data_dict['info'].replace('\n', '')
    data_info=data_info.replace(' ','')
    data_info = data_info.replace('\r', '')
    data_info = data_info.replace('\t', '')
    if data_info:
        date = time.strftime('%Y-%m-%d %H:%M:%S')
        data_dict['date'] = str(date)
        num = data_acquisition.acquire_rnum_from_message()
        data_dict['id'] = str(num + 1)
        email = session.get("email")
        # print(email)
        # print(data_dict)
        data_dict['nikename'] = email
        # 2.把数据添加到数据库
        data_storing.store_dict_into_mongodb(costants.CLUSTER_NAME, costants.DATABASE_NAME, costants.COLLECTION_MESSAGE,
                                             data_dict)
        return '<script>alert("留言成功！");location.href="/"</script>'

    else:
        return '<script>alert("留言为空发布失败！");location.href="/add1"</script>'


# 只能删除自己的留言，所以需要验证登录

# 删除 一行留言,修改
@app.route("/delete")
def delete():
    id = request.args.get('id')
    # 根据id从数据库中获取nikename
    res = data_acquisition.acquire_data_from_message({'id': id})
    print(res[0])
    res=res[0]
    nikename=res['nikename']
    # nikename=request.args.get('nikename')
    email = session.get("email")
    print(nikename)
    print(email)
    if email==nikename:
        data_delete.delete_one_record({'id': id})
        return '<script>alert("删除成功！");location.href="/"</script>'
    else:
        return '<script>alert("删除失败！无法删除他人留言");location.href="/"</script>'
    print("等待完成删除")


# 修改留言视图界面  不能修改id 即使在text文本框中修改了也没用
@app.route("/update")
def update():
    print("等待完成更新")
    # 看一下怎么阻止直接访问
    if session.get("email"):
        id = request.args.get('id')
        res=data_acquisition.acquire_data_from_message({'id':id})
        return render_template('update.html', data=res)
    else:
        # 加一个请先登录？？？
        return redirect(url_for("login"))


# 只能修改自己的留言，更改一下自己的留言
# 修改留言视图函数 在数据库中修改留言内容
@app.route('/modify', methods=['POST'])
def modify():
    # 1.接收表单数据
    # 1.接收表单数据
    data_dict = request.form.to_dict()
    print(data_dict['info'])
    data_info = data_dict['info'].replace('\n', '')
    data_info = data_info.replace(' ', '')
    data_info = data_info.replace('\r', '')
    data_info = data_info.replace('\t', '')
    if data_info:
        data = request.form.to_dict()
        date = time.strftime('%Y-%m-%d %H:%M:%S')
        data['date'] = str(date)
        email = session.get("email")
        id=data['id']
        # print(email)
        # print(data_dict)
        data['nikename'] = email
        # 2.把数据添加到数据库
        data_update.update_one_record(info=data['info'],date=data['date'],nikename=data['nikename'],condition={'id':data['id']})
        return '<script>alert("修改成功！");location.href="/"</script>'
    else:
        data = request.form.to_dict()
        id = data['id']
        return f'<script>alert("留言修改失败！");location.href="update?id={id}"</script>'
    print("modify等待完成")

@app.route('/changepassword')
def changepassword():
    # 看一下怎么阻止直接访问
    if session.get("email"):
        # 当前处于登陆状态
        print(session.get('email'))
        return render_template('changepassword.html')
    else:
        # 加一个请先登录？？？
        return redirect(url_for("login"))

@app.route('/modifypw', methods=['POST'])
def modifypw():
    # 如果获得的修改密码的逻辑问题（看之前咋写的）
    # 如果符合逻辑就对密码进行修改

    # 获得表单数据
    password1 = request.form.get("password1")
    password2 = request.form.get("password2")
    # 获得当前用户的email
    email=session.get('email')
    # if found in database showcase that it's found
    email_found = records.find_one({"email": email})
    # 如果获得的修改密码的逻辑问题（看之前咋写的）-----可以修改一下检验是否符合格式
    if email_found:
        if password1 != password2:
            message = 'Passwords should match!'
            return render_template('changepassword.html', message=message)
        elif (password1==''or password2==''):
            message = 'Passwords should not be empty'
            return render_template('changepassword.html',message=message)
        else:
            records.update_one({'email': email}, {'$set': {'password': password2}})
            # find the new created account and its email
            user_data = records.find_one({"email": email})
            new_email = user_data['email']
            message = '修改成功'
            row = data_acquisition.acquire_data_from_message()
            # if registered redirect to logged in as the registered user
            return render_template('logged_in2.html', email=new_email, message=message,data=row)

    else:
        message = 'This email does not already exist in database'
        return render_template('changepassword.html', message=message)



# Thread(target=lambda: app.run(port=5001)).start()
#
#  # ----------服务2-----------------
# app2 = Flask('app2')
#
# @app2.route('/hacker')
# def hacker():
#     return render_template('hackerB.html')
#
# app2.run(port=5002)

if __name__ == "__main__":
    app.register_blueprint(user)
    app.run(debug=True, host='0.0.0.0', port=5000)
    # os.environ["WERKZEUG_RUN_MAIN"] = 'true'
    # Thread(target=app).start()
    # app2()
