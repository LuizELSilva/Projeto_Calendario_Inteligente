import Envia_Email
import os.path
import datetime as dt
from google.auth.transport.requests import Request 
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
'''
pip install python-google-calendar-api
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

'''

Data_hoje = str(dt.date.today())
diaAtual = Data_hoje[8:10]
mesAtual = Data_hoje[5:7]
lista_EventHoje = []
lista_DiaAtual = []
lista_MesAtual = []
lista_Hora = []
lista_Data = []
lista_Evento = []

SCOPES = ["https://www.googleapis.com/auth/calendar"]

def atualiza_Listas(semEventos,events):
    Cont_Eventos_hoje = 0
    if not events: # Retorna verdadeiro, caso os não exista eventos
            semEventos = True
    else:
        for event in events: # Adiciona a duas listas, evento(lista_Evento) data(lista_Data)
            
            start = event['start'].get('dateTime',event['start'].get('date'))
            summary = event['summary']
            lista_Evento.append(summary)
            lista_Data.append(start)
                
        for lista in range (0,len(lista_Data)): # Pega das duas listas (Evento) e (Data) e atribui nas listas DiaAtual/MesAtual/hora.
            if (diaAtual == lista_Data[lista][8:10] and mesAtual == lista_Data[lista][5:7]):
                lista_EventHoje.append(lista_Evento[lista])
                lista_DiaAtual.append(lista_Data[lista][8:10])
                lista_MesAtual.append(lista_Data[lista][5:7])
                lista_Hora.append(lista_Data[lista][11:16])
                Cont_Eventos_hoje += 1
                
    return Cont_Eventos_hoje, semEventos

def atualiza_Mensagem(semEventos,Cont_Eventos_hoje):
    if semEventos == True or Cont_Eventos_hoje == 0: # Caso não tenha eventos esse trecho é executado.
        mensagem = "Olá, Não temos eventos hoje."
        Envia_Email.enviar_email(mensagem)
    else: # Caso tenha eventos no dia o trecho de código é executado. Esse trecho pega as informações das listas e substitui o Texto na variável mensagem.
        mensagem = 'Olá segue eventos de hoje:\n'
        mensagemAux = 'eventoAlt - Data do evento: dia/mes hora: inicio\n'
        for _ in range (0,len(lista_EventHoje)):
            mensagem += mensagemAux
            mensagem = mensagem.replace('eventoAlt',lista_Evento[_])
            mensagem = mensagem.replace('dia',lista_DiaAtual[_])
            mensagem = mensagem.replace('mes',lista_MesAtual[_])
            mensagem = mensagem.replace('inicio',lista_Hora[_])
    Envia_Email.enviar_email(mensagem)
    
def main ():
    
    semEventos = False
    creds = None
    if os.path.exists("token.json"): # Verifica caminho do token (se existe)
        creds = Credentials.from_authorized_user_file("token.json")
    
    if not creds or not creds.valid: # Cria token usando credenciais caso não exista.
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port = 0)
    
        with open("token.json","w") as token:
            token.write(creds.to_json())

    try: # Pega todas as informações do calendário
        service = build("calendar","v3", credentials=creds)
        now = dt.datetime.now().isoformat() + "Z"
        event_result = service.events().list(calendarId="primary", timeMin=now, maxResults=30, singleEvents = True, orderBy= "startTime").execute() # vai trazer todos os eventos apartir do momento atual (Quant: 30 itens)
        events = event_result.get("items",[])
        
        Cont_Eventos_hoje, semEventos = atualiza_Listas(semEventos,events)
        
    except HttpError as error:
        print("Um erro ocorreu: ", error)
        
    atualiza_Mensagem(semEventos, Cont_Eventos_hoje)
    
if __name__ == "__main__":
    main()
