try:
    from django.conf import settings
except ImportError:
    settings = None

if settings:
    ACTIVECAMPAIGN_URL = getattr(settings, 'ACTIVECAMPAIGN_URL')
    ACTIVECAMPAIGN_API_KEY = getattr(settings, 'ACTIVECAMPAIGN_API_KEY')
else:
    ACTIVECAMPAIGN_URL = 'YOUR_AC_URL_HERE'
    ACTIVECAMPAIGN_API_KEY = 'YOUR_AC_API_KEY_HERE'
