"""Utilities to send texts"""
import smtplib

def text(receiver, content):
    """Define the function to send a text message"""
    mail = smtplib.SMTP('smtp-mail.outlook.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.ehlo()

    #REDACTED
    mail.login('example@outlook.com', 'example_password')
    mail.sendmail('example@outlook.com', receiver, content)
    mail.close()

def send_text(name:str):
    """Send a text message"""
    content = name + "has entered the apartment."
    print(content)

    #REDACTED
    #Fill in number email address (from cell provider) here:
    address = '12345678@cellprovider.com'
    text(address, content)
