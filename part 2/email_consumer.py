import time
from db_models import Contact
from rabbit_conect import channel
import Mongo_connect

channel.queue_declare(queue='email_queue')


def send_email(contact_id):
    contact = Contact.objects.get(id=contact_id)
    time.sleep(1)
    contact.send_email = True
    contact.save()


def callback(ch, method, properties, body):
    contact_id = body.decode('utf-8')
    send_email(contact_id)


channel.basic_consume(queue='email_queue', on_message_callback=callback, auto_ack=True)

print('Waiting for email messages. To exit press CTRL+C')
channel.start_consuming()
