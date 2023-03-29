from flask import Flask, request, render_template
import datetime

app = Flask(__name__)

# 留言列表
messages = []

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html.jinja2", messages=messages)

@app.route("/post/add/", methods=["POST"])
def add_message():
    # 获取用户提交的数据
    content = request.form.get("content")
    
    # 将新的留言添加到留言列表
    messages.append({"content": content, "timestamp": datetime.datetime.now()})
    
    return index()

if __name__ == "__main__":
    app.run()