from flask import Flask, render_template, request, redirect, url_for
import json
import os
from email_utils import send_email_gmail
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route("/")
def home():
    with open('data/CV.json', 'r', encoding='utf-8') as f:
        dados_cv = json.load(f)
    return render_template('index.html', cv=dados_cv)

# Rota do seu form "Hire Me" 
@app.route("/send_request", methods=["POST"])
def send_request():
    nome = request.form['name']
    email = request.form['email'] 
    message = request.form['message']
    
    print(f"Nova solicitação de: {nome} - {email}")
    
    # Envia email via Gmail
    enviou = send_email_gmail(
        assunto=f'[SITE] Novo projeto - {nome}',
        nome=nome,
        email_cliente=email,
        mensagem=message
    )
    
    if not enviou:
        print("Falha ao enviar email. Verificar logs.")
    
    return redirect(url_for('home'))

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=5000, debug=False)
