import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry("600x400")
ventana.title("Nueva ventana")
ventana.configure(background="#1d2d44")

def saludar():
    print("Saludos desde el boton")

boton1 = ttk.Button(ventana, text="Enviar", command=saludar)
boton1.pack(pady=20)


ventana.mainloop()