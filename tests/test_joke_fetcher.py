# -*- coding: utf-8 -*-

# test_joke_fetcher.py
#
# Unit tests for joke fetcher

import pytest, sys
sys.path.append('../')

from app import views, fetcher

# Test main application
def test_main_app():

    # Fetch index
    resp = views.index()

    # Check that app returns 200 with response content length > 0
    assert resp.status_code == 200
    assert len(resp.data) > 0

# Test name fetcher
def test_fetch_name():

    # Fetch name once to avoid rate limiting
    name = fetcher.fetch_name()

    # Check that first and last name were returned
    assert len(name) == 2

    # Check that first name is a string and length > 0
    assert isinstance(name[0], basestring)
    assert len(name[0]) > 0

    # Check that last name is a string and length > 0
    assert isinstance(name[1], basestring)
    assert len(name[1]) > 0

# Test joke fetcher
def test_fetch_joke():

    # Fetch joke once to avoid rate limiting
    joke = fetcher.fetch_joke('fname', 'lname')

    # Check that joke is a string, length > 0, and contains provided names
    assert isinstance(joke, basestring)
    assert len(joke) > 0
    assert 'fname' in joke
    assert 'lname' in joke

    # Test UTF8
    joke = fetcher.fetch_joke('ȚȋɠȄʀΔ','ʀɥɭɆȿ')
    assert u'ȚȋɠȄʀΔ' in joke
    assert u'ʀɥɭɆȿ' in joke

# Test joke URI builder
def test_joke_uri_builder():

    # Test happy path
    assert fetcher.build_joke_uri('fname','lname')  == 'http://api.icndb.com/jokes/random?firstName=fname&lastName=lname&limitTo=[nerdy]'

    # Test blank values
    assert fetcher.build_joke_uri('','lname')       == 'http://api.icndb.com/jokes/random?firstName=&lastName=lname&limitTo=[nerdy]'
    assert fetcher.build_joke_uri('fname','')       == 'http://api.icndb.com/jokes/random?firstName=fname&lastName=&limitTo=[nerdy]'

    # Test UTF8
    assert fetcher.build_joke_uri('ȚȋɠȄʀΔ','ʀɥɭɆȿ') == 'http://api.icndb.com/jokes/random?firstName=ȚȋɠȄʀΔ&lastName=ʀɥɭɆȿ&limitTo=[nerdy]'
