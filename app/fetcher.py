# fetcher.py
#
# Fetch names / jokes from the internet

import requests, json

# Name/joke list URIs
URI_NAME = 'http://uinames.com/api/'
URI_JOKE = 'http://api.icndb.com/jokes/random'

# Default names to use if name generator fails
DEFAULT_FIRST_NAME = 'default_first_name'
DEFAULT_LAST_NAME  = 'default_last_name'

# HTTP status codes
HTTP_OK = 200

# Fetch random first & last name
def fetch_name():

    # Get name from internet name list
    name_data = _get(URI_NAME)

    # Handle case where request to name list fails
    if not name_data:
        return [DEFAULT_FIRST_NAME, DEFAULT_LAST_NAME]

    # Return array containing first & last name
    return [name_data['name'], name_data['surname']]

# Fetch random joke, or False if request to joke list fails
def fetch_joke(first_name, last_name):

    # Build URI for requesting joke
    joke_uri = build_joke_uri(first_name, last_name)

    # Get joke from internet joke list
    joke_data = _get(joke_uri)

    # Handle case where request to joke list fails
    if not joke_data:
        return "Knock knock. Who's there? " + first_name + ' ' + last_name

    # Return joke text
    return joke_data['value']['joke']

# Build joke URI
def build_joke_uri(first_name, last_name):
    return URI_JOKE + '?firstName=' + first_name + '&lastName=' + last_name + '&limitTo=[nerdy]'

# Get requested URI; return parsed JSON data on success or False on failure
def _get(uri):
    resp = requests.get(uri)

    # Return false if request fails
    if resp.status_code != HTTP_OK:
        return False

    # Return dict containing parsed JSON data
    return json.loads(resp.text)
