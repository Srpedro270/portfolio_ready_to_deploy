import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_email_gmail(assunto, nome, email_cliente, mensagem):
    user = os.getenv('GMAIL_USER')
    password = os.getenv('GMAIL_PASS')
    
    print(f"[DEBUG] Vai usar: {user}")
    
    corpo = f"""
Novo contato pelo site:

Nome: {nome}
Email: {email_cliente}
Mensagem:
{mensagem}
    """
    
    msg = MIMEMultipart()
    msg['From'] = user
    msg['To'] = user
    msg['Reply-To'] = email_cliente
    msg['Subject'] = assunto
    msg.attach(MIMEText(corpo, 'plain'))

    try:
        print("[DEBUG] Conectando...")
        server = smtplib.SMTP('smtp.gmail.com', 587, timeout=60)
        print("[DEBUG] EHLO...")
        server.ehlo()
        print("[DEBUG] STARTTLS...")
        server.starttls()
        print("[DEBUG] Login...")
        server.login(user, password)
        print("[DEBUG] Login OK! Enviando...")
        server.sendmail(user, user, msg.as_string())
        server.quit()
        print(">>> SUCESSO: Gmail aceitou o email <<<")
        return True
    except smtplib.SMTPAuthenticationError as e:
        print(f">>> ERRO AUTH: Senha errada ou não é App Password. {e}")
        return False
    except Exception as e:
        print(f">>> ERRO GERAL: {type(e).__name__}: {e}")
        return False