import os
from flask import Flask, flash, request, redirect, url_for, render_template, session, Session
import time
import facerecognition as face

UPLOAD_FOLDER = 'uploads'

app = Flask(__name__)
sess = Session()
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024

def detections():
	return face.run()

@app.route('/', methods=['GET', 'POST'])

def hello_world():
	if request.method == 'GET':
		return render_template('index.html')
	if request.method == 'POST':
		if 'file' not in request.files:
			flash('File not uploaded')
			return render_template('index.html')
		file = request.files['file']
		if file.filename == '':
			flash('No selected file')
			return render_template('index.html')
		file.filename='sample.jpg'
		file.save('uploads/sample.jpg')
		return render_template('result.html', result=detections())

if __name__ == '__main__':
	app.secret_key = 'super secret key'
	app.config['SESSION_TYPE'] = 'filesystem'
	sess.init_app(app)
	app.debug = True
	app.run()