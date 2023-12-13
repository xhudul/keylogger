import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, to_email, from_email, password):
    # E-posta sunucusuna bağlanma
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    # E-posta hesabına giriş yapma
    server.login(from_email, password)

    # E-posta mesajını oluşturma
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # E-posta içeriğini ekleme
    msg.attach(MIMEText(body, 'plain'))

    # E-postayı gönderme
    server.sendmail(from_email, to_email, msg.as_string())

    # E-posta sunucusu ile bağlantıyı kapatma
    server.quit()

# Dosyadaki içeriği okuma
with open('message.txt', 'r') as file:
    message_content = file.read()

# E-posta gönderme işlemi
send_email(
    subject='Konu',
    body=message_content,
    to_email='alici@example.com',
    from_email='gonderici@gmail.com',
    password='gonderici_sifre'
)
