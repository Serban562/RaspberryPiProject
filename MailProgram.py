import base64
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from requests import HTTPError

def SendEmail(distance, email) :
    SCOPES = [
            "https://www.googleapis.com/auth/gmail.send"
        ]
    flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
    creds = flow.run_local_server(port=0)

    service = build('gmail', 'v1', credentials=creds)
    message = MIMEMultipart()
    message['From']  = "proiectelectronica@gmail.com"
    message['to'] = email
    message['subject'] = 'Email Subject'
    body="Mugshot!"
    html_part = MIMEText(body)
    with open('test.jpg', 'rb') as f:
        image_part = MIMEImage(f.read())
    message.attach(html_part)
    message.attach(image_part)
    create_message = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

    try:
        message = (service.users().messages().send(userId="me", body=create_message).execute())
        print(F'sent message to {message} Message Id: {message["id"]}')
    except HTTPError as error:
        print(F'An error occurred: {error}')
        message = None
