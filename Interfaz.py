import tkinter as tk
from tkinter import ttk,messagebox

windows = tk.Tk()
windows.geometry("300x130")
windows.title("Login")
windows.iconbitmap("LOGO-INMOBILIARIA.ico")
windows.resizable(None,None)

windows.columnconfigure(0,weight=1)
windows.columnconfigure(1,weight=3)

#Usuario
usuario_etiqueta = ttk.Label(windows,text="Usuario: ")
usuario_etiqueta.grid(row=0,column=0, sticky=tk.E, padx=5,pady=5)
usuario_entrada = ttk.Entry(windows)
usuario_entrada.grid(row=0,column=1,sticky=tk.W, padx=5,pady=5)

#password
password_etiqueta = ttk.Label(windows,text="Password: ")
password_etiqueta.grid(row=1, column=0,sticky=tk.E,padx=5,pady=5)
password_entrada = ttk.Entry(windows,show="*")
password_entrada.grid(row=1,column=1,sticky=tk.W,padx=5,pady=5)

#boton Login
def Login():
    messagebox.showinfo("Datos Login", f"usuario: {usuario_entrada.get()} password: {password_entrada.get()}")
btn = ttk.Button(windows,text="Login",command=Login)
btn.grid(row=3,column=0,columnspan=2)



windows.mainloop()