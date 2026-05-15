import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()

def send_hire_email(name, email, project):
    remetente = os.getenv('EMAIL_USER')  # teu outlook
    senha = os.getenv('EMAIL_PASS')      # senha de app do outlook
    destinatario = 'gustavo.pedro.dev27@outlook.com' # tu mesmo

    # Monta o email
    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = f'Novo contato via Portfolio - {name}'

    corpo = f"""
    Novo projeto pelo site:

    Nome: {name}
    Email: {email}
    Projeto: {project}
    """
    msg.attach(MIMEText(corpo, 'plain'))

    try:
        # Conecta no Outlook
        server = smtplib.SMTP('smtp-mail.outlook.com', 587)
        server.starttls()
        server.login(remetente, senha)
        server.sendmail(remetente, destinatario, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        print(f"Erro ao enviar email: {e}")
        return False