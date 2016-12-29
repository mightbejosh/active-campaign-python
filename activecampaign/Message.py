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


class Message(ActiveCampaign):
    def __init__(self, url, api_key):
        self.url = url
        self.api_key = api_key
        ActiveCampaign.__init__(self, url, api_key)

    def add(self, params, post_data):
        request_url = '%s&api_action=message_add&api_output=%s' % (
            self.url, self.output)
        post_data = urlencode(post_data)
        req = Request(request_url, post_data)
        response = json.loads(urlopen(req).read())
        return response

    def delete_list(self, params, _):
        request_url = '%s&api_action=message_delete_list&api_output=%s&%s' % (
            self.url, self.output, params)
        response = json.loads(urlopen(request_url).read())
        return response

    def delete(self, params, _):
        request_url = '%s&api_action=message_delete&api_output=%s&%s' % (
            self.url, self.output, params)
        response = json.loads(urlopen(request_url).read())
        return response

    def edit(self, params, post_data):
        request_url = '%s&api_action=message_edit&api_output=%s' % (
            self.url, self.output)
        post_data = urlencode(post_data)
        req = Request(request_url, post_data)
        response = json.loads(urlopen(req).read())
        return response

    def list_(self, params, _):
        request_url = '%s&api_action=message_list&api_output=%s&%s' % (
            self.url, self.output, params)
        response = json.loads(urlopen(request_url).read())
        return response

    def template_add(self, params, post_data):
        request_url = '%s&api_action=message_template_add&api_output=%s' % (
            self.url, self.output)
        post_data = urlencode(post_data)
        req = Request(request_url, post_data)
        response = json.loads(urlopen(req).read())
        return response

    def template_delete_list(self, params, _):
        request_url = '%s&api_action=message_template_delete_list&api_output=%s&%s' % (
            self.url, self.output, params)
        response = json.loads(urlopen(request_url).read())
        return response

    def template_delete(self, params, _):
        request_url = '%s&api_action=message_template_delete&api_output=%s&%s' % (
            self.url, self.output, params)
        response = json.loads(urlopen(request_url).read())
        return response

    def template_edit(self, params, post_data):
        request_url = '%s&api_action=message_template_edit&api_output=%s' % (
            self.url, self.output)
        post_data = urlencode(post_data)
        req = Request(request_url, post_data)
        response = json.loads(urlopen(req).read())
        return response

    def template_export(self, params, _):
        request_url = '%s&api_action=message_template_export&api_output=%s&%s' % (
            self.url, self.output, params)
        response = json.loads(urlopen(request_url).read())
        return response

    def template_import(self, params, post_data):
        request_url = '%s&api_action=message_template_import&api_output=%s' % (
            self.url, self.output)
        post_data = urlencode(post_data)
        req = Request(request_url, post_data)
        response = json.loads(urlopen(req).read())
        return response

    def template_list(self, params, _):
        request_url = '%s&api_action=message_template_list&api_output=%s&%s' % (
            self.url, self.output, params)
        response = json.loads(urlopen(request_url).read())
        return response

    def template_view(self, params, _):
        request_url = '%s&api_action=message_template_view&api_output=%s&%s' % (
            self.url, self.output, params)
        response = json.loads(urlopen(request_url).read())
        return response

    def view(self, params, _):
        request_url = '%s&api_action=message_view&api_output=%s&%s' % (
            self.url, self.output, params)
        response = json.loads(urlopen(request_url).read())
        return response


if __name__ == '__main__':
    ac = ActiveCampaign(ACTIVECAMPAIGN_URL, ACTIVECAMPAIGN_API_KEY)

    ## add
##    message = {
##        'format': 'mime',
##        'subject': 'Fetch at send: %s' % datetime.datetime.now(),
##        'fromemail': 'person@example.com',
##        'fromname': 'John Smith',
##        'reply2': 'reply2@example.com',
##        'priority': 3,
##        'charset': 'utf-8',
##        'encoding': 'quoted-printable',
##        'htmlconstructor': 'external',
##        'htmlfetch': 'http://example.com',
##        'htmlfetchwhen': 'send',
##        'textconstructor': 'external',
##        'textgetch': 'http://example.com',
##        'textfetchwhen': 'send',
##        'p[1]': 1
##    }
##    print ac.api('message/add', message)

## delete
##    print ac.api('message/delete?id=32')

## delete_list
##    print ac.api('message/delete_list?ids=30,31')

## edit
##    message = {
##        'id': 1,
##        'subject': 'Fetch at send: %s' % datetime.datetime.now(),
##        'fromemail': 'person@example.com',
##        'p[1]': 1
##    }
##    print ac.api('message/edit', message)

## list
##    print ac.api('message/list?ids=1,2')

## template_add
##    template = {
##        'name': 'My New Template',
##        'subject': 'New Subject',
##        'html': '<html><head><title>New Template</title></head><body><h1>This template was added via the API<h1></body></html></html>',
##        'template_scope': 'all',
##        'tags[]': 'Holiday',
##        'p[1]': 1
##    }
##    print ac.api('message/template_add', template)

## template_delete
##    print ac.api('message/template_delete?id=35')

## template_delete_list
##    print ac.api('message/template_delete_list?ids=35,36,37')

## template_edit
##    template = {
##        'id': 54,
##        'name': 'My New Template',
##        'html': '<html><head><title>New Template</title></head><body><h1>This template was added via the API<h1></body></html></html>',
##        'p[1]': 1
##    }
##    print ac.api('message/template_edit', template)

## template_export
##    print ac.api('message/template_export?ids[54]=54&type=xml')

## template_import
##    template = {
##        'names[0]': 'My Template Imported Test',
##        'template_scope2': 'all',
##        'urls[0]': 'http://example.com/template.xml'
##    }
##    print ac.api('message/template_import', template)

## template_import
##    template = {
##         'names[0]': 'My Template Imported Test',
##         'template_scope2': 'all',
##         'urls[0]': 'http://example.com/template.xml'
##     }
##    print ac.api('message/template_import', template)

## template_view
##    print ac.api('message/template_view?id=54')

## view
##    print ac.api('message/view?id=1')

## template_list
##    print ac.api('message/template_list?ids=76')
