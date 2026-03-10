import tkinter as tk

ventana = tk.Tk()
ventana.geometry("600x400")
ventana.title("Nueva ventana")
ventana.configure(background="#1d2d44")

etiqueta = tk.Label(ventana, text="Saludos")

etiqueta.configure(text="Nos vemos...")
etiqueta.pack(pady=20)


ventana.mainloop()
