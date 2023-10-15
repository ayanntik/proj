import tkinter
from tkinter import *
import socket
host = '192.168.80.133'
port = 5050
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))
screen = Tk()
screen.title("Train Data")
screen.geometry("840x510")
screen.resizable(False, False)

#heading
Label(screen, text="TRAIN 1", font=("sanskrit text", 20, "bold"), bg="blue", fg="white").place(x=0,
y=0)
Label(screen, text="TRAIN 2", font=("sanskrit text", 20, "bold"), bg="red",
fg="white").place(x=420, y=0)

#labels
Label(screen, text="Line1:", font=("roman",20)).place(x=40, y=60)
Label(screen, text="Direction1:", font=("roman",20)).place(x=40, y=110)
Label(screen, text="Speed1:", font=("roman",20)).place(x=40, y=170)
Label(screen, text="Line2:", font=("roman",20)).place(x=460, y=60)
Label(screen, text="Direction2:", font=("roman",20)).place(x=460, y=110)
Label(screen, text="Speed2:", font=("roman",20)).place(x=460, y=170)

#radio
ln1=StringVar()
ln1.set(None)
Radiobutton(screen, text='up', font=('small fonts', 20), variable=ln1, value='up').place(x=180,
y=60)
Radiobutton(screen, text='down', font=('small fonts', 20), variable=ln1,
value='down').place(x=280, y=60)
dir1=StringVar()
dir1.set(None)
Radiobutton(screen, text='left', font=('small fonts', 20), variable=dir1, value='left').place(x=180,
y=110)
Radiobutton(screen, text='right', font=('small fonts', 20), variable=dir1,
value='right').place(x=280, y=110)
ln2=StringVar()
ln2.set(None)
Radiobutton(screen, text='up', font=('small fonts', 20), variable=ln2, value='up').place(x=600,
y=60)
Radiobutton(screen, text='down', font=('small fonts', 20), variable=ln2,
value='down').place(x=700, y=60)
dir2=StringVar()
dir2.set(None)
Radiobutton(screen, text='left', font=('small fonts', 20), variable=dir2, value='left').place(x=600,
y=110)
Radiobutton(screen, text='right', font=('small fonts', 20), variable=dir2,
value='right').place(x=700, y=110)

#text entry
spd1=Entry(screen, font=('small fonts', 14), bd=4)
spd1.place(x=180, y=170)
spd2=Entry(screen, font=('small fonts', 14), bd=4)
spd2.place(x=600, y=170)
data = ''
def process():
    line1=ln1.get()
    direction1=dir1.get()
    line2=ln2.get()
    direction2=dir2.get()
    speed1=spd1.get()
    speed2=spd2.get()
    data = f'{line1},{direction1},{line2},{direction2},{speed1},{speed2}'
    client_socket.send(data.encode())
    response = client_socket.recv(1024).decode()
    if(response):
        result, color = response.split(',')
        signal = tkinter.Canvas(screen, height=100, width=100)
        signal.place(x=370, y=310)
        signal.create_oval((10,10,90,90),fill=color)
        Label(screen, text=result, font=("impact", 40, "bold"), bg="black", fg="white").pack(side='bottom', fill='both')

#button
Button(screen, text='SUBMIT', font=("small fonts",16), command=process).place(x=371, y=240)
screen.mainloop()
client_socket.close()