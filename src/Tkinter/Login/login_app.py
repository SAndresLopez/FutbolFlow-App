import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry("600x400")
ventana.title("Login")
ventana.configure(background="#1d2d44")

ventana.columnconfigure(0, weight=1)
ventana.rowconfigure(0, weight=1)
#Creación del frame
frame = ttk.Frame(ventana)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=3)
#Titulo del frame
etiqueta = ttk.Label(frame, text="Login", font=("Arial", 20))
etiqueta.grid(row=0, column=0, columnspan=2)
#Contenido
usuario_etiqueta = ttk.Label(frame, text="Usuario:")
usuario_etiqueta.grid(row=1, column=0,sticky=tk.W, padx=5, pady=5)

usuario_caja_texto =ttk.Entry(frame)
usuario_caja_texto.grid(row=1, column=1, sticky=tk.E , padx=5, pady=5)

password_etiqueta = ttk.Label(frame, text="Password:")
password_etiqueta.grid(row=2, column=0,sticky=tk.W, padx=5, pady=5)

password_caja_texto =ttk.Entry(frame, show="*")
password_caja_texto.grid(row=2, column=1, sticky=tk.E , padx=5, pady=5)
#Agregar boton
login_botton = ttk.Button(frame, text="Enviar")
login_botton.grid(row=3, column=0,columnspan=2, padx=5, pady=5)

frame.grid(row=0, column=0)

ventana.mainloop()