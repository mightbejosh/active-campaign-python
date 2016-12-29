import json

from .ActiveCampaign import ActiveCampaign
from .Config import ACTIVECAMPAIGN_URL, ACTIVECAMPAIGN_API_KEY

try:
    from urllib.parse import urlparse, urlencode
    from urllib.request import urlopen, Request
    from urllib.error import HTTPError
except ImportError:
    from urlparse import urlparse
    from urllib import urlencode
    from urllib2 import urlopen, Request, HTTPError


class User(ActiveCampaign):
    def __init__(self, url, api_key):
        self.url = url
        self.api_key = api_key
        ActiveCampaign.__init__(self, url, api_key)

    def add(self, params, post_data):
        request_url = '%s&api_action=user_add&api_output=%s' % (
            self.url, self.output)
        post_data = urlencode(post_data)
        req = Request(request_url, post_data)
        response = json.loads(urlopen(req).read())
        return response

    def delete_list(self, params, _):
        request_url = '%s&api_action=user_delete_list&api_output=%s&%s' % (
            self.url, self.output, params)
        response = json.loads(urlopen(request_url).read())
        return response

    def delete(self, params, _):
        request_url = '%s&api_action=user_delete&api_output=%s&%s' % (
            self.url, self.output, params)
        response = json.loads(urlopen(request_url).read())
        return response

    def edit(self, params, post_data):
        request_url = '%s&api_action=user_edit&api_output=%s' % (
            self.url, self.output)
        post_data = urlencode(post_data)
        req = Request(request_url, post_data)
        response = json.loads(urlopen(req).read())
        return response

    def list_(self, params, _):
        request_url = '%s&api_action=user_list&api_output=%s&%s' % (
            self.url, self.output, params)
        response = json.loads(urlopen(request_url).read())
        return response

    def me(self, params, _):
        request_url = '%s&api_action=user_me&api_output=%s' % (
            self.url, self.output)
        response = json.loads(urlopen(request_url).read())
        return response

    def view(self, params, _):
        if params.startswith('email='):
            action = 'user_view_email'
        elif params.startswith('username='):
            action = 'user_view_username'
        elif params.startswith('id='):
            action = 'user_view'
        request_url = '%s&api_action=%s&api_output=%s&%s' % (
            self.url, action, self.output, params)
        response = json.loads(urlopen(request_url).read())
        return response


if __name__ == '__main__':
    ac = ActiveCampaign(ACTIVECAMPAIGN_URL, ACTIVECAMPAIGN_API_KEY)

    ## add
##    user = {
##        'username': 'johnsmith',
##        'first_name': 'John',
##        'last_name': 'Smith',
##        'password': 'mypwd',
##        'password_r': 'mypwd',
##        'email': 'person@example.com',
##        'group[3]' : 3
##    }    
##    print ac.api('user/add', user)

## delete_list
##    print ac.api('user/delete_list?ids=3,4')

## delete
##    print ac.api('user/delete?id=5')

## edit
##    user = {
##        'username': 'johnsmith',
##        'first_name': 'John',
##        'last_name': 'Smyth',
##        'password': 'mynwqpwd',
##        'password_r': 'mynewpwd',
##        'email': 'person@example.com',
##        'group[3]' : 3,
##        'id' : 6
##    }    
##    print ac.api('user/edit', user)

## list
##    print ac.api('user/list?ids=1,6')

## me
##    print ac.api('user/me')

## view email
##    print ac.api('user/view?email=person@example.com')

## view username
##    print ac.api('user/view?username=johnsmith')

## view id
##    print ac.api('user/view?id=1')
