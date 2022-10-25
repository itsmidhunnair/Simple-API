from flask import Flask, request, render_template
app = Flask("SimpleAPI")

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        #check user details from db
        login_user = ()
    elif request.method == 'GET':
        #serve login page
        serve_login_page()
        
@app.route('/')
def index():
    return "Hey there! I'm Server."

@app.route('/hello', methods=['GET','POST'])
def sayHello():
    return 'Hello User! How are you?'

#adding variables
@app.route('/user/<username>')
def show_user(username):
    #returns the username
    return 'username: %s' % username

@app.route('/user-template/<name>')
def user(name=None):
    #name=None ensures the code runs even when no name is provided
    return render_template('user-profile.html', name=name)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    #returns the post, the post_id should be an integer
    return str(post_id)