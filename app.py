from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    content = '''<h1>VPNicus</h1>'''
    return render_template('default.html', content=content)

# This part is optional and can be removed
@app.route('/buy')
def billing():
    return 'Soon!'

@app.route('/verify')
def verify():
    return 'Soon!'

@app.route('/admin')
def admin():
    return 'Soon!'
