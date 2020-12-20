from flask import *

app = Flask(__name__)

@app.route("/<string:browser>/<int:version>/<string:region>")
def version_check(browser, version, region):
    return "0"

@app.route("/")
def index():
    return "Welcome to the 3DS Browser Update Bypass CBVC CDN server!"
