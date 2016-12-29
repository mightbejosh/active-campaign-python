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


class Design(ActiveCampaign):
    def __init__(self, url, api_key):
        self.url = url
        self.api_key = api_key
        ActiveCampaign.__init__(self, url, api_key)

    def edit(self, _, post_data):
        request_url = '%s&api_action=branding_edit&api_output=%s' % (
            self.url, self.output)
        post_data = urlencode(post_data)
        req = Request(request_url, post_data)
        response = json.loads(urlopen(req).read())
        return response

    def view(self, params, _):
        request_url = '%s&api_action=branding_view&api_output=%s' % (
            self.url, self.output)
        response = json.loads(urlopen(request_url).read())
        return response


if __name__ == '__main__':
    ac = ActiveCampaign(ACTIVECAMPAIGN_URL, ACTIVECAMPAIGN_API_KEY)

    # edit
    branding = {
        'id': 1,
        'branding_url': 'http://www.example.com/logo.png',
        'copyright': 'off',
        'demo': 'on',
        'footer_html': 'html',
        'footer_html_valueEditor': '',
        'groupid': 3,
        'header_html': 'html',
        'header_html_valueEditor': '',
        'site_name': 'Adulmec.ro',
        'logo_source': 'url'

    }
    # print ac.api('branding/edit', branding)

    # view
    print(ac.api('branding/view'))
