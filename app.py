from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    content = '''<h1>vpnicus</h1>'''
    return render_template('default.html', content=content)

@app.route('/verify')
def verify():
    return 'Soon!'

@app.route('/admin')
def admin():
    return 'Soon!'
