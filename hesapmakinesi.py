import tkinter as tk
from tkinter import END,RIGHT


def tiklananbuton(sayi):
    girdi.insert(END,sayi)

def toplama():
    global sayi1
    global islem
    islem = "+"
    sayi1 = float(girdi.get())
    girdi.delete(0,END)
def cikarma():
    global sayi1
    global islem
    islem = "-"
    sayi1 = float(girdi.get())
    girdi.delete(0,END)
def carpma():
    global sayi1
    global islem
    islem = "*"
    sayi1 = float(girdi.get())
    girdi.delete(0,END)
def bolme():
    global sayi1
    global islem
    islem = "/"
    sayi1 = float(girdi.get())
    girdi.delete(0,END)
def karesi():
    global sayi1
    global islem
    islem = "**"
    sayi1 = float(girdi.get())
    girdi.delete(0,END)
    if islem == "**":
        girdi.insert(0, sayi1 ** 2)
def yuzde():
    global sayi1
    global islem
    islem = "%"
    sayi1 = float(girdi.get())
    girdi.delete(0,END)
    if islem == "%":
        girdi.insert(0, sayi1 / 100)
def esittir():
    sayi2 = float(girdi.get())
    girdi.delete(0,END)

    if islem == "+":
        girdi.insert(0, sayi1 + sayi2)
    elif islem == "-":
        girdi.insert(0, sayi1 - sayi2)
    elif islem == "*":
        girdi.insert(0, sayi1 * sayi2)
    elif islem == "/":
        girdi.insert(0, sayi1 / sayi2)
def silme():
    girdi.delete(0,END)

pencere = tk.Tk()
pencere.geometry("230x210")
pencere.title("Hesap Makinesi")
girdi = tk.Entry(pencere,width=225,justify=RIGHT)
girdi.pack(pady=10)

buton1 = tk.Button(text="1",command=lambda:tiklananbuton(1))
buton1.place(x=10,y=140,width=45, height=30)
buton2 = tk.Button(text="2",command=lambda:tiklananbuton(2))
buton2.place(x=65,y=140,width=45, height=30)
buton3 = tk.Button(text="3",command=lambda:tiklananbuton(3))
buton3.place(x=120,y=140,width=45, height=30)
buton4 = tk.Button(text="4",command=lambda:tiklananbuton(4))
buton4.place(x=10,y=110,width=45, height=30)
buton5 = tk.Button(text="5",command=lambda:tiklananbuton(5))
buton5.place(x=65,y=110,width=45, height=30)
buton6 = tk.Button(text="6",command=lambda:tiklananbuton(6))
buton6.place(x=120,y=110,width=45, height=30)
buton7 = tk.Button(text="7",command=lambda:tiklananbuton(7))
buton7.place(x=10,y=80,width=45, height=30)
buton8 = tk.Button(text="8",command=lambda:tiklananbuton(8))
buton8.place(x=65,y=80,width=45, height=30)
buton9 = tk.Button(text="9",command=lambda:tiklananbuton(9))
buton9.place(x=120,y=80,width=45, height=30)
buton0 = tk.Button(text="0",command=lambda:tiklananbuton(0))
buton0.place(x=10,y=170,width=100, height=30)

butonartı = tk.Button(text="+",command=toplama)
butonartı.place(x=175,y=140,width=45, height=30)
butoneksi = tk.Button(text="-",command=cikarma)
butoneksi.place(x=175,y=110,width=45, height=30)
butonçarpım = tk.Button(text="x",command=carpma)
butonçarpım.place(x=175,y=80,width=45, height=30)
butonbölme = tk.Button(text="/",command=bolme)
butonbölme.place(x=175,y=50,width=45, height=30)
butonyuzde = tk.Button(text="%",command=yuzde)
butonyuzde.place(x=65,y=50,width=45, height=30)
butonnokta = tk.Button(text=".",command=lambda:tiklananbuton("."))
butonnokta.place(x=120,y=170,width=45, height=30)
butonC = tk.Button(text="C",command=silme)
butonC.place(x=10,y=50,width=45, height=30)
butonesittir = tk.Button(text="=",bg="grey",command=esittir)
butonesittir.place(x=175,y=170,width=45, height=30)
butonkaresi = tk.Button(text="x²",command=karesi)
butonkaresi.place(x=120,y=50,width=45, height=30)

pencere.mainloop()