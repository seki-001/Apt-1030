from flask import Flask, request, render_template_string

app = Flask(__name__)

class User:
    users = {
        'user1': 'pass1',
        'user2': 'pass2'
    }

    @classmethod
    def check_login(cls, username, password):
        return cls.users.get(username) == password

@app.route('/')
def index():
    return render_template_string(open('login.html').read())

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if User.check_login(username, password):
        return "Login successful!"
    else:
        return "Invalid username or password."

if __name__ == '__main__':
    app.run(debug=True)
