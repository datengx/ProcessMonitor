import configparser
from configparser import ConfigParser


# Modified version of configuration file parser based on the Python library
# class.
class MyConfigParser(ConfigParser):

    def __init__(self):
        super(MyConfigParser, self).__init__()

    def get_name(self):
        first_name = ''
        last_name = ''

        try:
            first_name = self.get('Setup', 'firstname')
            last_name = self.get('Setup', 'lastname')
        except configparser.NoOptionError:
            print('Error: parsing Name in the config file.')

        return {'first_name':  first_name, 'last_name': last_name}

    def get_email(self):
        email = ""

        # Raise exception when the parsing failed and return
        # empty string
        try:
            email = self.get('Setup', 'email')
        except configparser.NoOptionError:
            print('Error: parsing E-mail in the config file.')

        return email

    def get_phone_number(self):
        phone = ""

        try:
            phone = self.get('Setup', 'phone#')
        except configparser.NoOptionError:
            print('Error: parsing E-mail in the config file.')

        return phone
