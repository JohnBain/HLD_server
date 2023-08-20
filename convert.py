import os
from flask import Flask, flash, request, redirect, url_for, send_file
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'PYTHON_UPLOADS'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS 

@app.route('/', methods=['GET'])
def index():
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="{{url_for('upload_file')}}" method="POST" enctype="multipart/form-data">
      <input type=file name=file>
      <input type=submit value=Upload id="myinput">
    </form>
    '''

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


@app.route('/download', methods=['GET'])
def download_file():
    print(f"diagnostic info. {UPLOAD_FOLDER}/{request.args.get('filename')}")
    return send_file(f"{UPLOAD_FOLDER}/{request.args.get('filename')}",as_attachment=True)
    #return "Hello world"

app.run('0.0.0.0', 97, use_reloader=True)