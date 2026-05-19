import os
import resend

def send_email_gmail(assunto, nome, email_cliente, mensagem):
    resend.api_key = os.getenv('RESEND_API_KEY')
    user = os.getenv('GMAIL_USER') # seu gmail pra receber

    if not resend.api_key or not user:
        print(">>> ERRO: RESEND_API_KEY ou GMAIL_USER não configurado <<<")
        return False

    corpo = f"""
Novo contato pelo site:

Nome: {nome}
Email: {email_cliente}
Mensagem:
{mensagem}
    """

    try:
        params = {
            "from": "Portfolio <onboarding@resend.dev>",
            "to": [user],
            "reply_to": email_cliente,
            "subject": assunto,
            "text": corpo,
        }
        email = resend.Emails.send(params)
        print(f">>> SUCESSO: Resend ID {email['id']} <<<")
        return True
    except Exception as e:
        print(f">>> ERRO RESEND: {e}")
        return False