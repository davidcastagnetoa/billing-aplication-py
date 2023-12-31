# This code is using a web browser for authentification
import webbrowser
from dotenv import load_dotenv
import os

def send_message_via_link(phone_number, message):
    base_url = "https://web.whatsapp.com/send"
    chat_url = f"{base_url}?phone={phone_number}&text={message}"
    webbrowser.open(chat_url)

if __name__ == "__main__":
    phone = input("Introduce el número de teléfono del destinatario: ")
    phoneFormated = "+34" + phone
    print(phoneFormated)
    msg = input("Introduce el mensaje a enviar: ")
    send_message_via_link(phoneFormated, msg)

# ·················································································

# Tus credenciales
load_dotenv()
ACCOUNT_SID=os.getenv("ACCOUNT_SID")
AUTH_TOKEN=os.getenv("AUTH_TOKEN")

# # Para pruebas locales en terminales con puertos y proxys libres
# from twilio.rest import Client

# def send_whatsapp_via_twilio(to, body):
#     account_sid = ACCOUNT_SID  # Proporcionado por Twilio en tu dashboard. . Datos a proteger
#     auth_token = AUTH_TOKEN    # Proporcionado por Twilio en tu dashboard. . Datos a proteger
#     client = Client(account_sid, auth_token)
    
#     message = client.messages.create(
#         body=body,
#         from_='whatsapp:+1234567890',  # El número de Twilio con prefijo 'whatsapp:'
#         to=f'whatsapp:{to}'
#     )
    
#     print(message.sid)

# if __name__ == "__main__":
#     phone = input("Introduce el número de teléfono (con código de país): ")
#     msg = input("Introduce el mensaje a enviar: ")
#     send_whatsapp_via_twilio(phone, msg)

# ·················································································

# # Para pruebas
# # Download the helper library from https://www.twilio.com/docs/python/install
# import os
# from twilio.rest import Client


# # Find your Account SID and Auth Token at twilio.com/console
# # and set the environment variables. See http://twil.io/secure
# account_sid = ACCOUNT_SID
# auth_token = AUTH_TOKEN
# client = Client(account_sid, auth_token)

# message = client.messages \
#     .create(
#          from_='+34680771328',
#          body='Ahoy! This message was sent from my Twilio phone number!',
#          to='+34680771328'
#      )

# print(message.body)