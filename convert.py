import os
from flask import Flask, flash, request, redirect, url_for, send_file, render_template
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
from rembg import remove, new_session
from PIL import Image
from separate import most_interesting_third

UPLOAD_FOLDER = 'PYTHON_UPLOADS'
TRANSFORM_FOLDER = "TRANSFORMS"
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['TRANSFORM_FOLDER'] = TRANSFORM_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS 

app.config['MAX_CONTENT_LENGTH'] = 4 * 1024 * 1024

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print("diagnostic info:")
            print(url_for('download_file'))
            return redirect(url_for('download_file',filename=filename),code=301 )#+ f"?=filename={filename}", code=301)
            # redirect(url_for('download_file'), filename=filename)

def remove_bg(filename):
    input_path = os.path.join(app.config['UPLOAD_FOLDER'] + "/") + filename
    output_path = os.path.join(app.config['TRANSFORM_FOLDER'] + "/" + filename + ".png")
    print(f"input path: {input_path}")
    print(f"output path: {output_path}")
    input = Image.open(input_path)
    session = new_session('u2net_cloth_seg')
    output = remove(input, 
        session=session, 
        alpha_matting=True, 
        alpha_matting_foreground_threshold=190,
        alpha_matting_background_threshold=4,
        alpha_matting_erode_size=14,
        )
    print(output)
    output = most_interesting_third(output)
    output.save(output_path)
    return output_path

@app.route('/download', methods=['GET']) #web interface
def download_file():
    print(f"diagnostic info. {request.args.get('filename')}")
    temp_path = f"{UPLOAD_FOLDER}/{request.args.get('filename')}"
    final_path = remove_bg(temp_path)
    return send_file(final_path, as_attachment=True)
    #return "Hello world"

@app.route('/transform', methods=['POST']) #direct POST request
def transform():
    print('request data?')    
    print(request)
    for i in request.files:
        print(i)
    file = FileStorage(request.files['data'])
    filename = request.files['data'].filename
    print(filename)
    temp_path = os.path.join(app.config['UPLOAD_FOLDER'] + "/") + filename
    print('temp path:')
    print(temp_path)
    file.save(temp_path)
    final_file = remove_bg(filename)
    return send_file(final_file, as_attachment=True)



app.run('0.0.0.0', 97, use_reloader=True)
