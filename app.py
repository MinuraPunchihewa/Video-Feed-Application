from flask import Flask, render_template, Response, request
from camera import VideoCamera
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/feed', methods=['POST'])
def feed():
    file = request.files['file']
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return render_template('feed.html', filename=filename)


@app.route('/generate/<string:filename>')
def generate(filename: str):
    video_stream = VideoCamera(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return Response(generate_video(video_stream), mimetype='multipart/x-mixed-replace; boundary=frame')


def generate_video(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

