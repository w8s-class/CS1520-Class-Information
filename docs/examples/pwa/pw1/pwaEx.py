# Copyright 2015, Kevin Burke, Kyle Conroy, Ryan Horn, Frank Stratton, Guillaume Binet
# Created as documentation for Flask-RESTful Flask extension

from flask import Flask, render_template, request
import re

app = Flask(__name__)

#app.config.update(dict(SEND_FILE_MAX_AGE_DEFAULT=0))

@app.route("/")
def root_page():
	return render_template("homepage.html")

@app.after_request
def add_headers_to_fontawesome_static_files(response):
    """
    Fix for font-awesome files: after Flask static send_file() does its
    thing, but before the response is sent, add an
    Access-Control-Allow-Origin: *
    HTTP header to the response (otherwise browsers complain).
    """
    
    if (request.path and
        re.search(r'service-worker.js$', request.path)):
        response.headers.add('Service-Worker-Allowed', '/')
        print(response.headers)

    return response


if __name__ == '__main__':
	app.run(debug=True)
