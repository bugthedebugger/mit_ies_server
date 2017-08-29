#! /usr/bin/python3

from flask import Flask
from flask import request
from flask import render_template
import subprocess
import participants
from werkzeug import secure_filename
import os
import time


#INITIALIZE THE FLASK OBJECT
app = Flask(__name__)


#GET THE USER FOLDER NAMES
user_folder = participants.getFile()


#CONFIGURATOINS FOR FILE
app.config['MAX_CONTENT_PATH'] = 10737418240
app.config['ALLOWED_EXTENSIONS'] = ['py']

logfile = open('logfile.txt', 'a')

#DEFAULT APP ROUTE (INDEX)
@app.route('/')
def index():
	users = user_folder
	keys = sorted(users.keys())
	ip = request.remote_addr;
	loginTime = time.asctime( time.localtime(time.time()) )
	log = str(loginTime)  + ': ' + str(ip) + " accessed /\n"
	#print(log)

	logfile.write(log)

	return render_template('index.html', users=users, keys=keys)


#UPLOADING FILE ROUTE
@app.route('/data', methods=["GET", "POST"])
def return_data():

	user = request.args.get('user')
	filename = request.args.get('filename')
	filepath = "/var/www/test/uploads/"+user+"/"
	python_env = "python3"

	if os.path.isdir(filepath) and os.path.exists(filepath+filename):

		if request.method == 'GET':
			requests = request.args.to_dict()
		elif request.method == 'POST':
			requests = request.form.to_dict()

		requests["REQUEST_METHOD"] = request.method
		userarg = str(requests)
		#a = subprocess.call(filepath+filename+userarg, shell=True)
		# print(userarg)

		process1 = subprocess.Popen([python_env, filepath+filename, userarg], stdout=subprocess.PIPE)
		a = process1.communicate()[0]

		return str(a)

	else:
		return "<h1>Error! requested file doesn't exist</h1>"



#404 PAGE NOT FOUND HANDLER
#@app.errorhandler(404)
#def page_not_found(e):
#	return("<h1>Oops! Something went wrong!</h1>")


#FILE VALIDATOR FUNCTION
def file_validator(filename):
	#print(filename.rsplit('.'))
	return filename.split('.')[1] in app.config['ALLOWED_EXTENSIONS']  and \
			'.' in filename


#HANDLE THE /upload ROUTE
@app.route('/upload', methods=["POST"])
def upload_file():
	
	if request.method == 'POST':
		print(request.form.to_dict())
		try:
			f = request.files['file']

			if f and file_validator(f.filename):
				user = request.form.get('user')
				path = 'uploads/' + user + '/'

				print(path+f.filename)
				f.save(path+f.filename)

				url_path = "45.118.134.33/"+path+f.filename
				return "<h1>File Uploaded successfully! to %s</h1>" %url_path

			else:
				return "<h1>Error: Only Pthon files are accpeted!</h1>"

		except:
			return "<h1>Something went wrong while uploading the file! only python file accepted!</h1>"

	else:
		return "<h1>Invalid Request Type</h1>"


#ONLY RUN IF THIS IS THE MAIN INSTANCE
if __name__ == '__main__':
	app.run("45.118.134.33", 80, threaded=True)
#45.118.134.33
