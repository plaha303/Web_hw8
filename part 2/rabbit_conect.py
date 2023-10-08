import pika
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

rabbit_host = config.get('RABBIT', 'host')

host = rabbit_host
params = pika.URLParameters(host)
connection = pika.BlockingConnection(params)
channel = connection.channel()
