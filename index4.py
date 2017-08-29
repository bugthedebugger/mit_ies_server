#! /usr/bin/python3

from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/<user>', methods=['GET', 'POST'])
def index_user(user):
	print("------------------")
	methods = request.args.items().to_dict()
	print(methods)
	print(request.args)
	print("------------------")
	return 'user: %s' %user

@app.route('/')
def index():
	return render_template('index.php')

@app.errorhandler(404)
def page_not_found(error):
	return "<h1>Oops! Page not found!</h1>"

if __name__ == '__main__':
	app.run('45.118.134.33', 80)
