from closing_window import closing_window
from tkinter import *
from send_message import send_message

window = Tk()
window.title('Send a message!')

label_number = Label(window,
                     text='Enter a phone number:',
                     font=('Arial', 20),
                     fg='red')
label_number.pack()

phone_number = Entry(window,
                     font=('Arial', 20),
                     fg='#00FF00',
                     bg='black',
                     relief=SUNKEN,
                     width=20)
phone_number.config(insertbackground='white')
phone_number.pack()

label_text = Label(window,
                   text='Enter a text message:',
                   font=('Arial', 20),
                   fg='red')
label_text.pack()

text_area = Text(window,
                 font=('Arial', 20),
                 height=8,
                 width=20,
                 padx=20,
                 pady=20,
                 fg='#00FF00',
                 bg='black')
text_area.config(insertbackground='white')
text_area.pack()

button = Button(window, text='Send',
                font=('Arial', 12),
                command=send_message)
button.pack()

window.protocol("WM_DELETE_WINDOW", closing_window)
window.mainloop()
