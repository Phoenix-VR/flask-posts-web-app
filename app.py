
from flask import Flask,render_template,request
from model import create_post,get_posts

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='GET':
        pass
    if request.method=='POST':
        name = request.form.get('name')
        post = request.form.get('post')
        create_post(name,post)
    posts = get_posts()
    return render_template('home.html',posts = posts)

if __name__=='__main__':
    app.run(debug=True)