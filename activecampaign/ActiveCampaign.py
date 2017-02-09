
from .Config import ACTIVECAMPAIGN_URL, ACTIVECAMPAIGN_API_KEY
from .Connector import Connector

try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

class ActiveCampaign(Connector):

    def __init__(self, url, api_key, api_user = '', api_pass = ''):
        self.url = url
        self.api_key = api_key
        Connector.__init__(self, url, api_key, api_user, api_pass)

    def api(self, path, post_data=None, **kwargs):
        if not post_data:
            post_data = kwargs.pop('data', {})

        for k, v in post_data.items():
            post_data[k] = unicode(v).encode('utf-8')

        # IE: "subscriber/view"
        components = path.split('/')
        component = components[0]

        if '?' in components[1]:
            # query params appended to method
            # IE: subscriber/edit?overwrite=0
            method_arr = components[1].split('?')
            method = method_arr[0]
            params = method_arr[1]
        else:
            if components[1]:
                method = components[1]
                for k, v in kwargs.items():
                    kwargs[k] = unicode(v).encode('utf-8')
                params = urlencode(kwargs)
            else:
                return 'Invalid method.'

        # adjustments
        if component == 'branding':
            # reserved word
            component = 'design'
        elif component == 'sync':
            component = 'contact'
            method = 'sync'
        elif component == 'singlesignon':
            component = 'auth'

        class1 = '%s' % component.capitalize() # IE: "contact" becomes "Contact"
        source_module = __import__(class1, globals(), locals(), [], -1) # import Contact
        class1 = getattr(source_module, class1) # get Contact
        class1 = class1(ACTIVECAMPAIGN_URL, ACTIVECAMPAIGN_API_KEY) # Contact()
        # contact.view()

        if method == 'list':
            # reserved word
            method = 'list_'

        if method in dir(class1):
            return getattr(class1, method)(params, post_data)
        return None
