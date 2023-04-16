import configparser

#this is to read and access data from config file.
config = configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")

class ReadConfig:
    @staticmethod # act as normal function and avoid self method.
    def getApplicationURL():
        url = config.get("common info", "baseURL")
        return url

    @staticmethod
    def getUseremail():
        username = config.get("common info", "useremail")
        return username

    @staticmethod
    def getPassword():
        password = config.get("common info", "password")
        return password