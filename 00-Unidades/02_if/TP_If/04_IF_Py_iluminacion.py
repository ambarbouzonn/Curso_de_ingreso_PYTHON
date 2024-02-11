import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
TP: IF_Iluminacion
---
Enunciado:
Todas las lámparas están  al mismo precio de $800 pesos final.
		A.	Si compra 6 o más  lamparitas bajo consumo tiene un descuento del 50%. 
		B.	Si compra 5  lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
		C.	Si compra 4  lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
		D.	Si compra 3  lamparitas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
		E.	Si el importe final con descuento suma más de $4000  se obtien un descuento adicional de 5%.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__() 

        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Marca")
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        
        self.combobox_marca = customtkinter.CTkComboBox(master=self, values=["ArgentinaLuz", "FelipeLamparas","JeLuz","HazIluminacion","Osram"])
        self.combobox_marca.grid(row=0, column=1, padx=10, pady=10)

        self.label2 = customtkinter.CTkLabel(master=self, text="Cantidad")
        self.label2.grid(row=1, column=0, padx=10, pady=10)

        self.combobox_cantidad = customtkinter.CTkComboBox(master=self, values= ["1", "2","3","4","5","6","7","8","9","10","11","12"])
        self.combobox_cantidad.grid(row=1, column=1, padx=10, pady=10)
                
        self.btn_calcular = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_calcular_on_click(self):
        titulo_alert = "Iluminacion"
        precio_lampara = 800
        marca = self.combobox_marca.get()
        cantidad = int(self.combobox_cantidad.get())

        # compra 6 o más  lamparitas bajo consumo 
        compra_mayor_a_6_multi = precio_lampara * cantidad
        compra_mayor_a_6_menos = compra_mayor_a_6_multi * 0.50
        compra_mayor_a_6_total = compra_mayor_a_6_multi - compra_mayor_a_6_menos
        mensaje_6 = "Usted realizo una compra de {0} lamparas bajo consumo por lo que su total de compra queda en: {1}".format(cantidad, compra_mayor_a_6_total)

        # compra 5  lamparitas bajo consumo marca "ArgentinaLuz"
        compra_mayor_a_5_multi_argentinaluz = precio_lampara * 5
        compra_mayor_a_5_menos_argentinaluz = compra_mayor_a_5_multi_argentinaluz * 0.40
        compra_mayor_a_5_total_argentinaluz = compra_mayor_a_5_multi_argentinaluz - compra_mayor_a_5_menos_argentinaluz
        mensaje_5_argentinaluz = "Usted realizo una compra de 5 lamparas bajo consumo con la marca ArgentinaLuz por lo que su total de compra queda en: {0}".format(compra_mayor_a_5_total_argentinaluz)

        # compra 5  lamparitas bajo consumo marca culaquiera
        compra_mayor_a_5_multi_multimarca = precio_lampara * 5
        compra_mayor_a_5_menos_multimarca = compra_mayor_a_5_multi_multimarca * 0.30
        compra_mayor_a_5_total_multimarca = compra_mayor_a_5_multi_multimarca - compra_mayor_a_5_menos_multimarca
        mensaje_5 = "Usted realizo una compra de 5 lamparas bajo consumo por lo que su total de compra queda en: {0}".format(compra_mayor_a_5_total_multimarca)

        # compra 4  lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas”
        compra_mayor_a_4_multi = precio_lampara * 4
        compra_mayor_a_4_menos = compra_mayor_a_4_multi * 0.25
        compra_mayor_a_4_total = compra_mayor_a_4_multi - compra_mayor_a_4_menos
        mensaje_4 = "Usted realizo una compra de 4 lamparas bajo consumo de {0} por lo que su total de compra queda en: {1}".format(marca,compra_mayor_a_4_total)

        # compra 4  lamparitas bajo consumo marca "JeLuz", "HazIluminacion" y "Osram"
        compra_mayor_4_multi_marca = precio_lampara * 4
        compra_mayor_a_4_menos_marca = compra_mayor_4_multi_marca * 0.20
        compra_mayor_a_4_total_marca = compra_mayor_4_multi_marca - compra_mayor_a_4_menos_marca
        mensaje_4_marca = "Usted realizo una compra de 4 lamparas bajo consumo de {0} por lo que su total de compra queda en: {1}".format(marca,compra_mayor_a_4_total_marca)
        

        if (marca == "ArgentinaLuz" or "FelipeLamparas" or "JeLuz" or "HazIluminacion" or "Osram" and cantidad == 6):
            alert(titulo_alert,mensaje_6)
        elif (marca == "ArgentinaLuz" and cantidad == 5):
            alert(titulo_alert, mensaje_5_argentinaluz)
        elif (marca == "FelipeLamparas" or "JeLuz" or"HazIluminacion" or "Osram" and cantidad == 5):
            alert(titulo_alert, mensaje_5)
        elif (marca == "ArgentinaLuz" or "FelipeLamparas" and cantidad == 4):
            alert(titulo_alert, mensaje_4)
        elif (marca == "JeLuz" or "HazIluminacion" or "Osram" and cantidad == 4):
            alert(titulo_alert, mensaje_4_marca)
        
        


        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()