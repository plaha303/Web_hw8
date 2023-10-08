import time
from db_models import Contact
from rabbit_conect import channel
import Mongo_connect

channel.queue_declare(queue='sms_queue')


def send_sms(contact_id):
    contact = Contact.objects.get(id=contact_id)
    time.sleep(1)
    contact.send_sms = True
    contact.save()


def callback(ch, method, properties, body):
    contact_id = body.decode('utf-8')
    send_sms(contact_id)


channel.basic_consume(queue='sms_queue', on_message_callback=callback, auto_ack=True)

channel.start_consuming()
