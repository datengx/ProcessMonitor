import configparser
from configparser import ConfigParser




# Modified version of configuration file parser based on the Python library
# class.
class MyConfigParser(ConfigParser):

    def __init__(self):
        super(MyConfigParser, self).__init__()

    def getname(self):
        firstname = ''
        lastname = ''

        try:
            firstname = self.get('Setup', 'firstname')
            lastname = self.get('Setup', 'lastname')
        except configparser.NoOptionError:
            print('Error: parsing Name in the config file.')

        return {'firstname':  firstname, 'lastname': lastname}


    def getemail(self):
        email = ""

        # Raise exception when the parsing failed and return
        # empty string
        try:
            email = self.get('Setup', 'email')
        except configparser.NoOptionError:
            print('Error: parsing E-mail in the config file.')

        return email

    def getphonenumber(self):
        phone = ""


        try:
            phone = self.get('Setup', 'phone#')
        except configparser.NoOptionError:
            print('Error: parsing E-mail in the config file.')

        return phone