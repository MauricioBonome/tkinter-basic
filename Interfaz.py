import tkinter as tk
from tkinter import ttk,messagebox


class Login(tk.Tk):
    def __init__(self):
        super().__init__()
        #ventana prinicpal
        self.geometry("300x130")
        self.title("Login")
        self.iconbitmap("LOGO-INMOBILIARIA.ico")
        self.resizable(None,None)

        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=3)

        self._crear_componentes()
        #definir el metodo
    def _crear_componentes(self):

        #Usuario
        usuario_etiqueta = ttk.Label(self,text="Usuario: ")
        usuario_etiqueta.grid(row=0,column=0, sticky=tk.E, padx=5,pady=5)
        self.usuario_entrada = ttk.Entry(self)
        self.usuario_entrada.grid(row=0,column=1,sticky=tk.W, padx=5,pady=5)

        #password
        password_etiqueta = ttk.Label(self,text="Password: ")
        password_etiqueta.grid(row=1, column=0,sticky=tk.E,padx=5,pady=5)
        self.password_entrada = ttk.Entry(self,show="*")
        self.password_entrada.grid(row=1,column=1,sticky=tk.W,padx=5,pady=5)

        #boton Login

        btn = ttk.Button(self,text="Login",command=self._Login)
        btn.grid(row=3,column=0,columnspan=2)




    def _Login(self):
        messagebox.showinfo("Datos Login", f"usuario: {self.usuario_entrada.get()} password: {self.password_entrada.get()}")


if __name__=="__main__":
    login_ventana=Login()
    login_ventana.mainloop()