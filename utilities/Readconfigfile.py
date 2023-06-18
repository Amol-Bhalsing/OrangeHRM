import configparser
config=configparser.RawConfigParser()
config.read(r'D:\SoftwareTesting\Automation Testing\Framework_Projects\OrangeHRM\Configuration\config.ini')

class Readvalue:
    @staticmethod
    def getUsername():
        username=config.get('login info','username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('login info', 'password')
        return password

    @staticmethod
    def getUrl():
        url = config.get('login info', 'url')
        return url