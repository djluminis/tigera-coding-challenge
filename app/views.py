# views.py
#
# Flask request views

from app import app, fetcher
from flask import render_template, make_response

# Misc constants
FIRST_NAME = 0
LAST_NAME  = 1

# Index page
@app.route('/')
def index():
	name = fetcher.fetch_name()
	joke = fetcher.fetch_joke(name[FIRST_NAME], name[LAST_NAME])

	with app.app_context():
		return make_response(joke)
