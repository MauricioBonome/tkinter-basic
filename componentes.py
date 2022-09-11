import tkinter as tk
from tkinter import ttk,messagebox

ventana  = tk.Tk()
ventana.geometry("600x400")
ventana.title("Componentes")
ventana.iconbitmap("LOGO-INMOBILIARIA.ico")

def crear_tabs():
    # Creamos un tab contro, para ello usamos la clase Notebook

    control_tabulador= ttk.Notebook(ventana)
    #Agregamos un marco (frame) para agregar dentro del tab del tabulador y organizar

    tabulador1 = ttk.Frame(control_tabulador)
    #Agregamos el tabular  al control de tabuladores
    control_tabulador.add(tabulador1, text="Tabulador 1 ")
    #Mostramos el tabulador
    control_tabulador.pack(fill="both")


crear_tabs()

ventana.mainloop()