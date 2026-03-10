import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry("600x400")
ventana.title("Nueva ventana")
ventana.configure(background="#1d2d44")

def mostrar():
    texto = caja_texto.get()
    print(f"texto proporcionado:{texto}")

caja_texto = ttk.Entry(ventana, font=("Arial", 15))
caja_texto.pack(pady=20)

boton = ttk.Button(ventana, text="Enviar", command = mostrar)
boton.pack(pady=20)
ventana.mainloop()