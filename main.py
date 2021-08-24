import smtplib
import os
import requests
import json
from email.message import EmailMessage

email1 = os.environ.get('email1')
password1 = os.environ.get('password1')

api = r"https://official-joke-api.appspot.com/random_joke"
def jokes(api):
    
    data = requests.get(api)
    dict = json.loads(data.text)
    return dict

def generate_send_msg():
    joke = jokes(api)
    msg = EmailMessage()
    msg['Subject'] = joke['setup']
    msg['From'] = email1
    msg['To'] = target
    msg.set_content(joke['punchline'])
    smtp.send_message(msg)

target = input("Enter Target's Email: ")
num_emails = int(input("Enter The Amount of Jokes To Send: "))

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email1, password1)
    for i in range(num_emails):
        generate_send_msg()


