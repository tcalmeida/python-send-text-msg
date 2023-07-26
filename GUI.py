from tkinter import *
from tkinter import Text
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

sid = os.getenv('SID')
token = os.getenv('AUTH_TOKEN')
your_number = os.getenv('YOUR_NUMBER')
target_number = os.getenv('TARGET_NUMBER')


def send_message():
    message = text_area.get('1.0', END)

    client = Client(sid, token)
    client.messages.create(
        body=message,
        from_=your_number,
        to=target_number
    )
    print(f'Message has been sent!')


window = Tk()

text_area: Text = Text(window,
                       font=('Arial', 25),
                       height=8,
                       width=20,
                       padx=20,
                       pady=20,
                       fg='red')
text_area.pack()

button = Button(window, text='Send', command=send_message)
button.pack()

window.mainloop()
