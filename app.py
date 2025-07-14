from flask import Flask, render_template, request

app = Flask(__name__)

# Homepage route
@app.route('/')
def home():
    return render_template('index.html')

# Registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
