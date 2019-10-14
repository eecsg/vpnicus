from flask import Flask
app = Flask(__name__)

# This part is optional
@app.route('/')
def home():
    content = '''<h1>VPNicus</h1>'''
    return render_template('default.html', content=content)

# This part is optional and can be removed
@app.route('/buy')
def billing():
    content = '''Soon!'''
    return render_template('default.html', content=content)

# This part is required for authentication
@app.route('/verify/<token>')
def verify():
    return 'Soon!'

# This part is required for managing users.
@app.route('/admin')
def admin():
    return 'Soon!'
