def enviar_email(mensagem):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    destinatario = "destinatario1@gmail.com, Cco:destinatario2@gmail.com"
    assunto = "Mensagem Usando google Calendar"
    
    print(mensagem)
      
    # 1 - Configurar informações do remetente e do servidor de e-mail
    remetente = "remetente@gmail.com"
    senha = "SenhaDeApp"
    servidor_sxmtp = "smtp.gmail.com"
    porta_smtp = 587

    # 2 - Criar objeto de mensagem multipart
    msg = MIMEMultipart()

    # 3 - Configurar os campos do cabeçalho do e-mail
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = assunto
        

    # 4 - Adicionar corpo do e-mail
    msg.attach(MIMEText(mensagem, 'plain'))
    

    # 6 - Conectar ao servidor e enviar o e-mail
    with smtplib.SMTP(servidor_sxmtp, porta_smtp) as smtp:
        smtp.starttls()
        smtp.login(remetente, senha)
        smtp.send_message(msg)
           
        smtp.quit()