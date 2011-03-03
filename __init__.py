import urllib2
import urllib
from django.conf import settings

class SmartPass:
    def __init__(self, username, password):
        self.username = username
        self.password = password

        passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
        # this creates a password manager
        passman.add_password(None, settings.SMARTPASS_URL, self.username, self.password)
        # because we have put None at the start it will always
        # use this username/password combination for  urls
        # for which `theurl` is a super-url

        authhandler = urllib2.HTTPBasicAuthHandler(passman)
        # create the AuthHandler

        opener = urllib2.build_opener(authhandler)

        urllib2.install_opener(opener)
        # All calls to urllib2.urlopen will now use our handler
        # Make sure not to include the protocol in with the URL, or
        # HTTPPasswordMgrWithDefaultRealm will be very confused.
        # You must (of course) use it when fetching the page though.

    def call(self, url, get = None, post = None):
        """
        Generic caller. Handles authentication and weither to use and/or post
        """

        url = settings.SMARTPASS_URL + url

        if post:
            post_data = urllib.urlencode(post)

        if get:
            get_data = urllib.urlencode(get)

        if post:
            response = urllib2.urlopen("%s?%s" %(url, get_data), post_data)
        else:
            response = urllib2.urlopen("%s?%s" %(url, get_data))

        return response.read()


    def add_guest(self, username, user_type = '24-Hours Duration', password = None, person_name = None, email_address = None, other_values = None):
        """
        Adds a new guest wifi user in smartpass

        username required
        """

        url = 'webservice/provision/v1/users'
        get_data = {'op':'add',
                    'username':username,
                    'user-type': user_type }

        if password:
            get_data['password'] = password

        if person_name:
            get_data['person_name'] = person_name

        if email_address:
            get_data['email_address'] = email_address

        if other_values:
            get_data.update(other_values)

        self.call(url, get = get_data)


        
