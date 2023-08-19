from flask import Flask, render_template, request, session
# First we imported the Flask class.

app = Flask(__name__)  # Next we create an instance of this class.
app.secret_key = '_5#y2L"F4Q_MY_SESSION_KEY_8z/n/xec]/'
# Set the secret key to some random bytes.


@app.route("/", methods=['GET', 'POST'])  # Decorator
def home():
    if 'user_id' in session:
        user_id = session['user_id']
        return render_template('home.html', user_id=user_id)
    else:
        return render_template('home.html')
# We use the route() decorator to tell Flask what URL should trigger our function.


@app.route('/search', methods=['GET', 'POST'])
def search():
    search = request.args.get('search')
    return render_template('search.html', search=search)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['user_id'] = request.form['user_id']
        user_id = session['user_id']
        return render_template('home.html', user_id=user_id)
    else:
        return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return render_template("home.html")


if __name__ == '__main__':
    # This conditional statement is used to distinguish
    # when a script file is used as a main program and when used as a module.
    app.run()
