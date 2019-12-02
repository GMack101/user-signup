
from flask import Flask,request,render_template,redirect
app = Flask(__name__)
app.config['DEBUG'] = True
@app.route("/")
def index():
    return render_template('index.html')
@app.route("/index", methods=['GET', 'POST'])
def signup():
    username= request.form['username']
    password= request.form['password']
    verify= request.form['verify']
    email= request.form['email']
    username_error=''
    password_error=''
    verify_error=''
    email_error=''
    if request.method == 'POST':
        if int(len(username)) <= 0 :
            username_error="That's not a valid username"
            username=''
        else:
            if int(len(username)) < 3 or int(len(username)) > 20 or " " in username :
                username_error = 'Thats not a valid username'
                username = ''
        if int(len(password)) <= 0:
                password_error="That's not a valid password"
                password=''
        elif int(len(password)) < 3 or int(len(password)) > 20:
                password_error="That's not a valid password"
                password=''
        if verify != password:
            verify_error="passowrd do not match"
            verify=''
        if int(len(email)) > 0:
            if "@" not in email or '.' not in email or " "  in  email:
                email_error="That's not a valid email"
                email=''
            elif int(len(email)) < 3 or int(len(email)) > 20:
                    email_error="That's not a valid email"
                    email=''
        if not username_error and not password_error and not verify_error and not email_error:
            return redirect('/homepage?username={0}'.format(username))
        else:
            return render_template('index.html',username_error=username_error,password_error=password_error,verify_error=verify_error,email_error=email_error,username=username,password=password,verify=verify,email=email)
@app.route('/homepage')
def greeting():
    username=request.args.get('username')
    return render_template('homepage.html',username=username)
app.run()   




    



