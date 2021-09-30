import os
from flask import Flask, request
app = Flask(__name__)
import requests

UPLOAD_FOLDER = r'upload'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file1' not in request.files:
            return 'there is no file1 in form!'
        file1 = request.files['file1']
        path = os.path.join(app.config['UPLOAD_FOLDER'], file1.filename)
        file1.save(path)
        print(path)
        r = requests.post(
            "https://api.deepai.org/api/colorizer",
            files={
                'image': open(path, 'rb'),
            },
            headers={'api-key': '3a1506b8-06bd-44a2-9bdf-305964d21330'}
        )

        return r.json()
    return '''
    <h1>Upload new File</h1>
    <form method="post" enctype="multipart/form-data">
      <input type="file" name="file1">
      <input type="submit">
    </form>
    '''

