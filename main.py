from flask import Flask, render_template, request, send_file
import pyqrcode
import os


app = Flask(__name__)

@app.route('/', methods= ['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        qr_code = pyqrcode.create(url)
        qr_code.png('static/qr_code.png', scale=8)
        return render_template('index.html', qr_generated =True)
    return render_template('index.html', qr_generated=False)
@app.route('/download')
def download_qr():

    path= "static/qr_code.png"
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, port= 8000)
