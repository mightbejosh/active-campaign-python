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


class Contact(ActiveCampaign):
    def __init__(self, url, api_key):
        self.url = url
        self.api_key = api_key
        ActiveCampaign.__init__(self, url, api_key)

    def add(self, params, post_data):
        request_url = '%s&api_action=contact_add&api_output=%s' % (
            self.url, self.output)
        if params:
            request_url = '%s&%s' % (request_url, params)
        post_data = urlencode(post_data)
        req = Request(request_url, post_data)
        response = json.loads(urlopen(req).read())
        return response

    def delete(self, params, _):
        request_url = '%s&api_action=contact_delete&api_output=%s&%s' % (
            self.url, self.output, params)
        response = json.loads(urlopen(request_url).read())
        return response

    def delete_list(self, params, _):
        request_url = '%s&api_action=contact_delete_list&api_output=%s&%s' % (
            self.url, self.output, params)
        response = json.loads(urlopen(request_url).read())
        return response

    def edit(self, params, post_data):
        request_url = '%s&api_action=contact_edit&api_output=%s&%s' % (
            self.url, self.output, params)
        post_data = urlencode(post_data)
        req = Request(request_url, post_data)
        response = json.loads(urlopen(req).read())
        return response

    def list_(self, params, _):
        request_url = '%s&api_action=contact_list&api_output=%s&%s' % (
            self.url, self.output, params)
        response = json.loads(urlopen(request_url).read())
        return response

    def paginator(self, params, _):
        request_url = '%s&api_action=contact_paginator&api_output=%s&%s' % (
            self.url, self.output, params)
        response = json.loads(urlopen(request_url).read())
        return response

    def sync(self, params, post_data):
        request_url = '%s&api_action=contact_sync&api_output=%s' % (
            self.url, self.output)
        if params:
            request_url = '%s&%s' % (request_url, params)
        post_data = urlencode(post_data)
        req = Request(request_url, post_data)
        response = json.loads(urlopen(req).read())
        return response

    def view(self, params, _):
        if params.startswith('email='):
            action = 'contact_view_email'
        elif params.startswith('hash='):
            action = 'contact_view_hash'
        elif params.startswith('id='):
            action = 'contact_view'
        else:
            action = 'contact_view'
        request_url = '%s&api_action=%s&api_output=%s&%s' % (
            self.url, action, self.output, params)
        response = json.loads(urlopen(request_url).read())
        return response


if __name__ == '__main__':
    ac = ActiveCampaign(ACTIVECAMPAIGN_URL, ACTIVECAMPAIGN_API_KEY)

'''
    add
   contact = {
       'email': 'person@example.com',
       'first_name': 'John',
       'last_name': 'Smith',
       'p[1]': 1,
       'status[1]': 1,
   }
   print ac.api('contact/add', contact)

delete
   print ac.api('contact/delete?id=10')

delete_list
   print ac.api('contact/delete_list?ids=9,11')

edit
   contact = {
       'id': 12,
       'email': 'person@example.com',
       'first_name': 'Johnny',
       'last_name': 'Smith',
       'p[1]': 1,
       'status[1]': 1
   }
   print ac.api('contact/edit', contact)

list
   print ac.api('contact/list?ids=1,12')

paginator
   print ac.api('contact/paginator?sort=&offset=0&limit=20&filter=0')

sync
   contact = {
       'email': 'person@example.com',
       'first_name': 'John',
       'last_name': 'Smith',
       'p[1]': 1,
       'status[1]': 1,
   }
   print ac.api('contact/sync', contact)

view id
   print ac.api('contact/view?id=12')

view email
   print ac.api('contact/view?email=person@example.com')

view hash
   print ac.api('contact/view?hash=3eeda4735e93f5407fced5ed45ddae82')
'''