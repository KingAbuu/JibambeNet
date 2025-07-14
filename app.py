from flask import Flask, render_template, request

app = Flask(__name__)

# Homepage route
@app.route('/')
def home():
    return render_template('index.html')

# Registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['password']

        print("New registration:")
        print("Email:", email)
        print("Phone:", phone)
        print("Password:", password)

        return f"<h2>Thanks for registering, {email}!</h2>"

    return render_template('register.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        print("Login attempt:")
        print("Email:", email)
        print("Password:", password)

        return f"<h2>Welcome back, {email}!</h2>"

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
