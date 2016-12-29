import datetime
import time

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

import simplejson as json


class Campaign(ActiveCampaign):
    def __init__(self, url, api_key):
        self.url = url
        self.api_key = api_key
        ActiveCampaign.__init__(self, url, api_key)

    def create(self, params, post_data):
        request_url = '%s&api_action=campaign_create&api_output=%s' % (
            self.url, self.output)
        post_data = urlencode(post_data)
        req = Request(request_url, post_data)
        response = json.loads(urlopen(req).read())
        return response

    def delete(self, params, _):
        request_url = '%s&api_action=campaign_delete&api_output=%s&%s' % (
            self.url, self.output, params)
        response = json.loads(urlopen(request_url).read())
        return response

    def delete_list(self, params, _):
        request_url = '%s&api_action=campaign_delete_list&api_output=%s&%s' % (
            self.url, self.output, params)
        response = json.loads(urlopen(request_url).read())
        return response

    def list_(self, params, _):
        request_url = '%s&api_action=campaign_list&api_output=%s&%s' % (
            self.url, self.output, params)
        print(request_url)
        response = json.loads(urlopen(request_url).read())
        return response

    def paginator(self, params, _):
        request_url = '%s&api_action=campaign_paginator&api_output=%s&%s' % (
            self.url, self.output, params)
        response = json.loads(urlopen(request_url).read())
        return response

    def report_bounce_list(self, params, _):
        request_url = '%s&api_action=campaign_report_bounce_list&api_output=%s&%s' % (
            self.url, self.output, params)
        response = json.loads(urlopen(request_url).read())
        return response

    def report_bounce_totals(self, params, _):
        request_url = '%s&api_action=campaign_report_bounce_totals&api_output=%s&%s' % (
            self.url, self.output, params)
        response = json.loads(urlopen(request_url).read())
        return response

    def report_forward_list(self, params, _):
        request_url = '%s&api_action=campaign_report_forward_list&api_output=%s&%s' % (
            self.url, self.output, params)
        response = json.loads(urlopen(request_url).read())
        return response

    def report_forward_totals(self, params, _):
        request_url = '%s&api_action=campaign_report_forward_totals&api_output=%s&%s' % (
            self.url, self.output, params)
        response = json.loads(urlopen(request_url).read())
        return response

    def report_link_list(self, params, _):
        request_url = '%s&api_action=campaign_report_link_list&api_output=%s&%s' % (
            self.url, self.output, params)
        response = json.loads(urlopen(request_url).read())
        return response

    def report_link_totals(self, params, _):
        request_url = '%s&api_action=campaign_report_link_totals&api_output=%s&%s' % (
            self.url, self.output, params)
        response = json.loads(urlopen(request_url).read())
        return response

    def report_open_list(self, params, _):
        request_url = '%s&api_action=campaign_report_open_list&api_output=%s&%s' % (
            self.url, self.output, params)
        response = json.loads(urlopen(request_url).read())
        return response

    def report_open_totals(self, params, _):
        request_url = '%s&api_action=campaign_report_open_totals&api_output=%s&%s' % (
            self.url, self.output, params)
        response = json.loads(urlopen(request_url).read())
        return response

    def report_totals(self, params, _):
        request_url = '%s&api_action=campaign_report_totals&api_output=%s&%s' % (
            self.url, self.output, params)
        response = json.loads(urlopen(request_url).read())
        return response

    def report_unopen_list(self, params, _):
        request_url = '%s&api_action=campaign_report_unopen_list&api_output=%s&%s' % (
            self.url, self.output, params)
        response = json.loads(urlopen(request_url).read())
        return response

    def report_unsubscription_list(self, params, _):
        request_url = '%s&api_action=campaign_report_unsubscription_list&api_output=%s&%s' % (
            self.url, self.output, params)
        response = json.loads(urlopen(request_url).read())
        return response

    def report_unsubscription_totals(self, params, _):
        request_url = '%s&api_action=campaign_report_unsubscription_totals&api_output=%s&%s' % (
            self.url, self.output, params)
        response = json.loads(urlopen(request_url).read())
        return response

    def send(self, params, _):
        request_url = '%s&api_action=campaign_send&api_output=%s&%s' % (
            self.url, self.output, params)
        response = json.loads(urlopen(request_url).read())
        return response

    def status(self, params, _):
        request_url = '%s&api_action=campaign_status&api_output=%s&%s' % (
            self.url, self.output, params)
        response = json.loads(urlopen(request_url).read())
        return response


if __name__ == '__main__':
    ac = ActiveCampaign(ACTIVECAMPAIGN_URL, ACTIVECAMPAIGN_API_KEY)

    ## create
    sdate = datetime.datetime.now() + datetime.timedelta(hours=0, minutes=2)
    campaign = {
        'type': 'single',
        'name': 'testActiveCampaign: %s' % datetime.datetime.now(),
        'sdate': time.strftime('%Y-%m-%d %H:%M:%S', sdate.timetuple()),
        'status': 0,
        'public': 0,
        'tracklinks': 'all',
        'trackreads': 1,
        'htmlunsub': 1,
        'p[1]': 1,
        'm[1]': 100
    }
    from time import time

    time2 = time()
    print(ac.api('campaign/create', post_data=campaign))
    print('diff2 = %.5f seconds' % (time() - time2))

    # list
    print ac.api('campaign/list', ids=1)

'''
    # delete
    print ac.api('campaign/delete', id=12)

    # delete_list
    print ac.api('campaign/delete_list', ids='1,2')

    # paginator
    print ac.api('campaign/paginator?sort=&offset=0&limit=20&filter=0&public=0')

    # report_bounce_list
    print ac.api('campaign/report_bounce_list?campaignid=3')

    # report_bounce_totals
    print ac.api('campaign/report_bounce_totals?campaignid=13&messageid=2')

    # report_forward_list
    print ac.api('campaign/report_forward_list?campaignid=13&messageid=2')

    # report_forward_totals
    print ac.api('campaign/report_forward_totals?campaignid=13&messageid=2')

    # report_link_list
    print ac.api('campaign/report_link_list?campaignid=13&messageid=2')

    # report_link_totals
    print ac.api('campaign/report_link_totals?campaignid=13&messageid=2')

    # report_open_list
    print ac.api('campaign/report_open_list?campaignid=13&messageid=2')

    # report_open_totals
    print ac.api('campaign/report_open_totals?campaignid=13&messageid=2')

    # report_totals
    print ac.api('campaign/report_totals?campaignid=13&messageid=2')

    # report_unopen_list
    print ac.api('campaign/report_unopen_list?campaignid=13&messageid=2')

    # report_unsubscription_list
    print ac.api('campaign/report_unsubscription_list?campaignid=13')

    # report_unsubscription_totals
    print ac.api('campaign/report_unsubscription_totals?campaignid=13&messageid=2')

    # report_send
    print ac.api('campaign/send?campaignid=13&messageid=2&type=mime&action=send&email=person@example.com')

    # report_status
    print ac.api('campaign/status?id=13&status=5')
'''
