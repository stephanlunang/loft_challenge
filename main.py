import requests 
from pprint import pprint

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	return "Hey, you're not supposed to be here! Try /satellite_id instead."

@app.route("/<satellite_id>")
def latest_tle(satellite_id):

	user = "stephanng1234@gmail.com"
	password = "loftchallenge2019"
	host_name = "www.space-track.org"

	tle_api = (
		"https://{}/basicspacedata/query/class/"
		"tle_latest/ORDINAL/1/NORAD_CAT_ID/{}/orderby/"
		"TLE_LINE1 ASC/format/tle"
	).format(host_name, satellite_id)

	post_address = "https://{}/ajaxauth/login".format(host_name)

	data = {
		"identity": user,
		"password": password,
		"query": tle_api
	}

	resp = requests.post(url=post_address, data=data)

	tle = resp.text

	return tle
