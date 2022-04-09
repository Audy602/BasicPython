#GUI-calculator.py

from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import messagebox

GUI = Tk() 
GUI.title('โปรแกรมคำนวณราคา')
GUI.geometry('700x600')

bg = PhotoImage(file=r'G:\OneDrive\Program\Python\Pyton for Beginner\Van.png')

BG = Label(GUI, image=bg)   
BG.pack()

L = Label(GUI,text='กรุณากรอกจำนวน (kg)',font=(None,20))
L.pack()

v_quantity = StringVar() 
E1 = ttk.Entry(GUI, textvariable=v_quantity, font=(None,20))
E1.pack()

def Cal():
    try:
        quan = float(v_quantity.get())
        calc = quan *39
        messagebox.showinfo('ราคาทั้งหมด', 'ราคาปลาทั้งหมด {} บาท'.format(calc) )
        v_quantity.set('1')
    except:
        messagebox.showwarning('กรอกเฉพาะตัวเลขเท่านั้น')
        v_quantity.set('1')


B = ttk.Button(GUI, text='คำนวณ',command=Cal)
B.pack(ipadx=30, ipady=20)

GUI.mainloop() #เพื่อให้โปรแกรมรันตลอดเวลา