import os
import importlib.util
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = './uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    filename = secure_filename(file.filename)
    save_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(save_path)

    if filename.endswith('.py'):
        spec = importlib.util.spec_from_file_location("mod", save_path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)

    return f"File {filename} uploaded!"

@app.route('/flag')
def show_flag():
    with open("static/creds.json") as f:
        creds = json.load(f)
        return creds

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
