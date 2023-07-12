Projeto feito em python que utiliza google Api Calendar para envio de E-mails.

O projeto consiste em uma automação do Google Agenda, o programa pega todos os eventos marcados na agenda e manda por E-mail (Os e-mails dos destinatários devem ser digitados dentro do código). O código está dividido em dois arquivos py, o primeiro (Main) pega e filtra as informações e o segundo (Envia_Email), formata e envia para os destinatários.

Utilizei como base o guia de início para python: https://developers.google.com/calendar/api/quickstart/python?hl=pt-br
Para fazer o código funcionar é preciso inicialmente instalar calendar_api e google-api-python.

pip install python-google-calendar-api

pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib


Além disso, é preciso ter o arquivo json, responsável pela criação do token. Além dessas duas etapas, é preciso ter a senha de app Ativada e referenciada.
