from mongoengine import connect
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

mongo_user = config.get('DB', 'user')
mongo_pass = config.get('DB', 'pass')
db_name = config.get('DB', 'db_name')

connect(host=f"mongodb+srv://{mongo_user}:{mongo_pass}@cluster0.p1klsgt.mongodb.net/{db_name}")
