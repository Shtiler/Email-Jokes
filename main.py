import smtplib
import os
import requests
import json
from email.message import EmailMessage
import random

email1 = os.environ.get('email1')
password1 = os.environ.get('password1')

api = r"https://official-joke-api.appspot.com/random_joke"
def jokes(api):
    
    data = requests.get(api)
    dict = json.loads(data.text)
    return dict

def generate_send_joke():
    joke = jokes(api)
    # Api's limit is 100 requests per 15 min
    if joke['type'] == "error":
        print("Error")
        return
    msg = EmailMessage()
    msg['Subject'] = joke['setup']
    msg['From'] = email1
    msg['To'] = target
    msg.set_content(joke['punchline'])
    smtp.send_message(msg)
def generate_send_spam(subj,body):
    msg = EmailMessage()
    rand = f"#{random.randrange(1,1000)}"
    msg['Subject'] = subj + rand
    msg['From'] = email1
    msg['To'] = target
    msg.set_content(body)
    smtp.send_message(msg)

choice = int(input("Enter 1 for Sending a jokes: \nEnter 2 For Email Spam: "))
target = input("Enter Target's Email: ")
num_emails = int(input("Enter The Amount of Jokes To Send: "))

if choice == 1:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email1, password1)
        for i in range(num_emails):
            generate_send_joke()
        print("Done!")
elif choice == 2:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email1, password1)
        subj = input("Enter The Email's subject: ")
        body = input("Enter The Email's body: ")
        for i in range(num_emails):
            generate_send_spam(subj,body)
        print("Done!")
else:
    print("Invalid Choice")


