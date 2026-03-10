import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry("600x400")
ventana.title("Nueva ventana")
ventana.configure(background="#1d2d44")

def mostrar():
    print("boton1")
def mostrar2():
    print("boton2")
def mostrar3():
    print("boton3")

boton1 = ttk.Button(ventana, text="boton1", command=mostrar)
boton2 = ttk.Button(ventana, text="boton2", command=mostrar2)
boton3 = ttk.Button(ventana, text="boton3",command=mostrar3)

boton1.grid(row=0, column=0)
boton2.grid(row=0, column=1)
boton3.grid(row=0, column=2)

ventana.mainloop()