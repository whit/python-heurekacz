import re
import logging
import urllib2
from urllib import urlencode

email_re = re.compile(
    r"(^[-!#$%&'*+/=?^_`{}|~0-9A-Z]+(\.[-!#$%&'*+/=?^_`{}|~0-9A-Z]+)*"  # dot-atom
    r'|^"([\001-\010\013\014\016-\037!#-\[\]-\177]|\\[\001-011\013\014\016-\177])*"' # quoted-string
    r')@(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?$', re.IGNORECASE)  # domain

log = logging.getLogger('heurekacz')
if not log.handlers:
    logging.basicConfig()

class Overeno(object):
    """
    Overeno zakazniky

    Usage::

        ov = Overeno('xbG32nDsa...')
        ov.set_email('customer@example.com')
        ov.add_product('Some product')
        ...
        ov.add_product('Another product')
        ov.send()
    """

    BASE_URL = 'http://www.heureka.cz/direct/dotaznik/objednavka.php'
    RESPONSE_OK = 'ok'

    def __init__(self, api_key):
        super(Overeno, self).__init__()

        if not len(api_key) == 32:
            log.error('Lenght of api_key must be 32 characters, not %d.' % len(api_key))
        else:
            self.api_key = api_key
            self.products = []

    def set_email(self, email):
        if not email_re.match(email):
            log.error('E-mail address is not valid: %s' % email)
            return
        self.email = urlencode({'email': email})

    def add_product(self, product):
        self.products.append(urlencode({'produkt[]': product}))

    def send(self, timeout=2):
        url = "%(base_url)s?id=%(api_key)s&%(email)s&" % {
            'base_url': self.BASE_URL,
            'api_key': self.api_key,
            'email': self.email
        }
        url += "&".join(self.products)

        try:
            try:
                resp = urllib2.urlopen(url, timeout=timeout)
            except TypeError, e:
                log.warning('Cannot set timeout in urlopen: %s' % e)
                resp = urllib2.urlopen(url)
            cnt = resp.read()
            if cnt == self.RESPONSE_OK:
                return True
            else:
                log.error('Heureka.cz response fails: %s' % cnt)
                return False

        except Exception, e:
            log.error('Error in send request to Heureka.cz: %s' % e)
            return False
