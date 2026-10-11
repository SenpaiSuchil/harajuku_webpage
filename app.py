from flask import Flask, render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/fashion')
def fashion():
    return render_template('1_fashion.html')

@app.route('/beauty')
def beauty():
    return render_template('2_beauty.html')

@app.route('/vlog')
def vlog():
    return render_template('3_vlog.html')

@app.route('/snap')
def snap():
    return render_template('4_snap.html')

@app.route('/resources')
def resources():
    return render_template('5_resources.html')

@app.route('/magazine')
def magazine():
    return render_template('6_magazine.html')

@app.route('/models')
def models():
    return render_template('7_models.html')

@app.route('/contact')
def contact():
    return render_template('8_contact.html')

@app.route('/shoplist')
def shoplist():
    return render_template('9_shoplist.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)