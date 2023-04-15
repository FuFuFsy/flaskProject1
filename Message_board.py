'''
这个页面是用来测试留言板功能的，所以纯测试的
'''
from flask import Flask,render_template,request
import time
import auth, costants,data_storing,data_acquisition

app = Flask(__name__)


# 留言板列表 显示留言信息
@app.route("/")
def hello():
    # 1.获取所有的留言板数据
    # 2.把数据分配到模板中(html页面)
    # row = model("select * from lyb")
    # return render_template('index.html',data=row)
    row= data_acquisition.acquire_data_from_message()
    # data = data_acquisition.acquire_data_from_message(conditionproduct={"nikename":"mike"})
    # print(data)
    return render_template('logged_in2.html', data=row)

# 定义视图 显示留言添加的页面
@app.route('/add')
def add():
    return render_template('add.html')


# 定义视图函数 接收表单数据，完成数据的入库
@app.route('/insert', methods=['POST'])
def insert():
    # 1.接收表单数据
    data_dict = request.form.to_dict()
    date=time.strftime('%Y-%m-%d %H:%M:%S')
    data_dict['date'] = str(date)
    print(data_dict)
    # 2.把数据添加到数据库
    data_storing.store_dict_into_mongodb(costants.CLUSTER_NAME, costants.DATABASE_NAME, costants.COLLECTION_MESSAGE,data_dict)
    # 3.成功后页面跳转到 留言列表界面
    if 1:
        return '<script>alert("留言成功！");location.href="/"</script>'
    else:
        return '<script>alert("留言发布失败！");location.href="/add"</script>'


# 删除 一行留言
@app.route("/delete")
def delete():
    id = request.args.get('id')
    # sql = f'delete from lyb where id={id}'
    # res = model(sql)
    # if res:
    #     return '<script>alert("删除成功！");location.href="/"</script>'
    # else:
    #     return '<script>alert("删除失败！");location.href="/"</script>'
    print("等待完成删除")


# 修改留言视图界面  不能修改id 即使在text文本框中修改了也没用
@app.route("/update")
def update():
    print("等待完成更新")
    # id = request.args.get('id')
    # sql = f'select * from lyb where id={id}'
    # res = model(sql)
    # return render_template('update.html', data=res)


# 修改留言视图函数 在数据库中修改留言内容
@app.route('/modify', methods=['POST'])
def modify():
    # # 1.接收表单数据
    # data = request.form.to_dict()
    # data['date'] = time.strftime('%Y-%m-%d %H:%M:%S')
    # # 2.把数据添加到数据库
    # sql = f'update lyb set nikename="{data["nikename"]}",info="{data["info"]}",date="{data["date"]}" where id={int(data["id"])}'
    # res = model(sql)
    # # 3.成功后页面跳转到 留言列表界面
    # if res:
    #     return '<script>alert("修改成功！");location.href="/"</script>'
    # else:
    #     return '<script>alert("留言修改失败！");location.href="/"</script>'
    print("modify等待完成")


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port='8080')
