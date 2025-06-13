from flask import Flask, render_template, request, send_file
import qrcode
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('formulario.html')

@app.route('/generar', methods=['POST'])
def generar():
    data = request.form['data']
    img = qrcode.make(data)
    buffer = io.BytesIO()
    img.save(buffer, 'PNG')
    buffer.seek(0)
    return send_file(buffer, mimetype='image/png', download_name='codigoqr.png')

if __name__ == '__main__':
    app.run(debug=True)