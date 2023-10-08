from random import choice
import pika
from faker import Faker
from db_models import Contact
import Mongo_connect
from rabbit_conect import channel, connection

fake = Faker("uk-UA")
notification_options = ['email', 'sms']

channel.queue_declare(queue='email_queue')
channel.queue_declare(queue='sms_queue')

contacts = []
for _ in range(20):
    contacts.append({
        'fullname': fake.name(),
        'email': fake.email(),
        'phone_number': fake.msisdn(),
        'choice_for_message': choice(notification_options),
        'send_email': False,
        'send_sms': False
    })

for data in contacts:
    contact = Contact(**data)
    contact.save()

    if contact.choice_for_message == 'email' and not contact.send_email:
        channel.basic_publish(exchange='', routing_key='email_queue', body=str(contact.id).encode())

    if contact.choice_for_message == 'sms' and not contact.send_sms:
        channel.basic_publish(exchange='', routing_key='sms_queue', body=str(contact.id).encode())

connection.close()
