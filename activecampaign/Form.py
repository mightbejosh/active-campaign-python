import json

from .ActiveCampaign import ActiveCampaign
from .Config import ACTIVECAMPAIGN_URL, ACTIVECAMPAIGN_API_KEY

try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen


class Form(ActiveCampaign):
    def __init__(self, url, api_key):
        self.url = url
        self.api_key = api_key
        ActiveCampaign.__init__(self, url, api_key)

    def getforms(self, params, _):
        del params
        request_url = '%s&api_action=form_getforms&api_output=%s' % (
            self.url, self.output)
        response = json.loads(urlopen(request_url).read())
        return response

    def html(self, params, _):
        request_url = '%s&api_action=form_html&api_output=%s&%s' % (
            self.url, self.output, params)
        # print urllib2.urlopen(request_url).read()
        response = json.loads(urlopen(request_url).read())
        return response


if __name__ == '__main__':
    ac = ActiveCampaign(ACTIVECAMPAIGN_URL, ACTIVECAMPAIGN_API_KEY)

    # getforms
    # print ac.api('form/getforms')

    # html
    # print ac.api('form/html?id=1142')
