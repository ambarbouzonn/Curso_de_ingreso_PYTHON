import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Ambar Morena 
apellido: Bouzon
---
Ejercicio: while_08
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario quiera, 
hasta que presione el botón Cancelar (en el prompt) o el usuario ingrese cero. 
Calcular la suma acumulada de los positivos y multiplicar los negativos. 
Luego informar los resultados en las cajas de texto txt_suma_acumulada y txt_producto

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.txt_suma_acumulada = customtkinter.CTkEntry(master=self, placeholder_text="Suma acumulada")
        self.txt_suma_acumulada.grid(row=0, padx=20, pady=20)

        self.txt_producto = customtkinter.CTkEntry(master=self, placeholder_text="Producto")
        self.txt_producto.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        contador = 0
        acumulador_suma = 0
        producto = 1

        while True:
            ingrese_numeros = prompt("Numeros", "Por favor, ingrese los numeros que desee:")

            if ingrese_numeros is None or ingrese_numeros == 0:
                break

            ingrese_numeros = int(ingrese_numeros)
            if ingrese_numeros > 0:
                contador += 1

                acumulador_suma += ingrese_numeros
            else: 
                if ingrese_numeros < 0:
                    contador += 1
                    
                    producto *= ingrese_numeros
                
            
            
        self.txt_producto.delete(0, tkinter.END)
        self.txt_producto.insert(0, producto)
        self.txt_suma_acumulada.insert(0, acumulador_suma)



    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
