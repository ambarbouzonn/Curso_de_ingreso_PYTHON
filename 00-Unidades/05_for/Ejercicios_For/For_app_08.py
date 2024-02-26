import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: for_08
---
Enunciado:
Al presionar el botón 'Mostrar' pedir un número. Mostrar cada número primo entre 1 y el número ingresado, 
e informar la cantidad de números primos encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        numero = prompt("", "Ingrese un numero")
        numero = int(numero)
        contador_primos = 0

        for numero in range(1, numero + 1):
            bandera_primo = True
            for divisor in range(2, int(numero ** 0.5) + 1):
                if numero % divisor == 0:
                    bandera_primo = False
                    break
            if bandera_primo and numero > 1: 
                contador_primos += 1
                print(numero)
                
        if contador_primos > 0:
            print(f"Cantidad de numeros primos encontrados: {contador_primos}")
        else:
            print("No se encontraron numeros primos.")

                     
                
            
            
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()