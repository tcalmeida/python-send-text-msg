import os
import GUI
from dotenv import load_dotenv
from tkinter import END, messagebox
from twilio.rest import Client

load_dotenv()

sid = os.getenv('SID')
token = os.getenv('AUTH_TOKEN')
your_number = os.getenv('YOUR_NUMBER')


def send_message():
    phone_number = GUI.phone_number.get()
    text = GUI.text_area.get('1.0', END)

    if not phone_number or len(text) == 1:
        return messagebox.showerror(title='Error', message='Enter a valid phone number or text')

    try:
        client = Client(sid, token)
        message = client.messages.create(
            body=text,
            from_=your_number,
            to=phone_number
        )
        GUI.text_area.delete('1.0', END)
        print(f'Message has been sent: {message.sid}')
    except Exception as error:
        return messagebox.showerror(title='Error', message=f'{error}')
