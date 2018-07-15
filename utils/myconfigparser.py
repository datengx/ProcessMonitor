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

    def get_from_email(self):
        source_email = ""

        # Raise exception when the parsing failed and return
        # empty string
        try:
            source_email = self.get('Setup', 'from_email')
        except configparser.NoOptionError:
            print('Error: parsing source E-mail in the config file.')

        return source_email

    def get_to_email(self):
        destination_email = ""

        # Raise exception when the parsing failed and return
        # empty string
        try:
            destination_email = self.get('Setup', 'to_email')
        except configparser.NoOptionError:
            print('Error: parsing destination E-mail in the config file.')

        return destination_email

    def get_phone_number(self):
        phone = ""

        try:
            phone = self.get('Setup', 'phone#')
        except configparser.NoOptionError:
            print('Error: parsing phone # in the config file.')

        return phone

    def get_password(self):
        password = ""

        try:
            password = self.get("Setup", "password")
        except configparser.NoOptionError:
            print("Error: parsing password in the config file.")

        return password
