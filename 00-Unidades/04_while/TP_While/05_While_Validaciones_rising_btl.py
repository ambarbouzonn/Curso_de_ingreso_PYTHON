import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Ambar Morena
apellido: Bouzon
---
TP: While_validaciones_rising_btl
---
Enunciado:
Rising BTL. Empresa dedicada a la toma de datos para realizar estadísticas 
y censos nos pide realizar una carga de datos validada e ingresada 
por ventanas emergentes solamente (para evitar hacking y cargas maliciosas) 
y luego asignarla a cuadros de textos. 

Los datos requeridos son los siguientes:
    Apellido
    Edad, entre 18 y 90 años inclusive.
    Estado civil, ["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"]
    Número de legajo, numérico de 4 cifras, sin ceros a la izquierda.
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        
        self.title("UTN Fra")

        self.label0 = customtkinter.CTkLabel(master=self, text="Apellido")
        self.label0.grid(row=0, column=0, padx=20, pady=10)
        self.txt_apellido = customtkinter.CTkEntry(master=self)
        self.txt_apellido.grid(row=0, column=1)

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=1, column=0, padx=20, pady=10)
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=1, column=1)

        self.label2 = customtkinter.CTkLabel(master=self, text="Estado")
        self.label2.grid(row=2, column=0, padx=20, pady=10)
        self.combobox_tipo = customtkinter.CTkComboBox(
            master=self, values=["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"])
        self.combobox_tipo.grid(row=2, column=1, padx=20, pady=10)

        self.label3 = customtkinter.CTkLabel(master=self, text="Legajo")
        self.label3.grid(row=3, column=0, padx=20, pady=10)
        self.txt_legajo = customtkinter.CTkEntry(master=self)
        self.txt_legajo.grid(row=3, column=1)

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        titulo_alert = "Validacion de datos"

        
        # Solicitar apellido
        while True:
            apellido = prompt(titulo_alert, "Por favor, ingrese su apellido")

            if apellido is None and apellido == "":
                break
            else:
                break

        # Solicitar edad
        while True:
            edad = prompt(titulo_alert, "Por favor, ingrese su edad")
            
            if edad is None or edad == "":
                break

            edad = int(edad)
            if edad < 17 or edad > 91:
                alert("Error", "Por favor, ingrese una edad valida")
                continue
            else:
                break


        # Solicitar numero de legajo
        while True:
            numero_legajo = prompt(titulo_alert, "Por favor, ingrese su numero de legajo de 4 cifras")

            if numero_legajo is None or "":
                break

            numero_legajo = int(numero_legajo)
            if numero_legajo > 9999 or numero_legajo < 1000:
                alert("Error", "Por favor, ingrese un numero de 4 cifras valido")
                continue
            else:
                break


        # Solicitar estado civil
        while True:
            estado_civil = prompt(titulo_alert, "Por favor, ingrese su estado civil\n"
                                  "Ingrese: Soltero/a, Casado/a, Divorciado/a, Viudo/a")
            
            if estado_civil is None or "":
                break

            if estado_civil not in ["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"]:
                alert("Error", "Por favor, ingrese un estado civil válido")
                continue
            else:
                break

        
        self.txt_edad.insert(0, edad)
        self.txt_apellido.insert(0, apellido.capitalize())
        self.txt_legajo.insert(0, numero_legajo)
        self.combobox_tipo.set(estado_civil)


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
