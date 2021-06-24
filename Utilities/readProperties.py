import configparser

config = configparser.RawConfigParser()

config.read(".\\Configurations\\config.ini")


class Readconfig():

    @staticmethod
    def ApplicationURL():
        url = config.get('common info', 'URL')
        return url

    @staticmethod
    def ApplicationURL_Pnt():
        urlPnt = config.get('common info', 'URL_Pnt')
        return urlPnt

    @staticmethod
    def getUseremail():
        username = config.get('common info', 'user_email')
        return username

    @staticmethod                        ### we can add as much data as we need update config.ini ile as well
    def getPassword():
        password = config.get('common info', 'user_password')
        return password