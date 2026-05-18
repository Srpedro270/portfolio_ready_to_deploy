import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_email_gmail(assunto, nome, email_cliente, mensagem):
    user = os.getenv('GMAIL_USER')
    password = os.getenv('GMAIL_PASS')
    
    if not user or not password:
        print(">>> ERRO: GMAIL_USER ou GMAIL_PASS não configurado no Render")
        return False
    
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
        print("[DEBUG] Conectando via SSL 465...")
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, timeout=60) as server:
            print("[DEBUG] Login...")
            server.login(user, password)
            print("[DEBUG] Login OK! Enviando...")
            server.sendmail(user, user, msg.as_string())
        print(">>> SUCESSO: Gmail aceitou o email <<<")
        return True
    except smtplib.SMTPAuthenticationError as e:
        print(f">>> ERRO AUTH: Senha errada ou não é App Password. {e}")
        return False
    except Exception as e:
        print(f">>> ERRO GERAL: {type(e).__name__}: {e}")
        return False