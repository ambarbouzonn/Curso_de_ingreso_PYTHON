import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Ambar Morena 
apellido: Bouzon
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        titulo = "Numeros"
        contador_pos = 0 #Cantidad positivos
        contador_neg = 0 #Cantidad negativos
        contador_de_0 = 0 #Cantidad de 0
        resultado_pos = 0 #Suma de positivos
        resultado_neg = 0 #Suma de negativos
        

        while True:
            numero_ingresado = prompt(titulo, "Ingrese los numeros que desee:")

            if numero_ingresado is None:
                break

            numero_ingresado = int(numero_ingresado)

            if numero_ingresado > 0: #Positivo
                contador_pos += 1
                resultado_pos += numero_ingresado
            else:
                if numero_ingresado < 0: #Negativo
                    contador_neg += 1
                    resultado_neg += numero_ingresado
                else:
                    contador_de_0 += 1
                    
        diferencia = resultado_pos + resultado_neg
                    

        alert(titulo, 
              f"Resultados:\n\n"
              f"Suma de positivos: {resultado_pos}\n"
              f"Suma de negativos: {resultado_neg}\n"
              f"Cantidad de números positivos ingresados: {contador_pos}\n"
              f"Cantidad de números negativos ingresados: {contador_neg}\n"
              f"Cantidad de ceros ingresados: {contador_de_0}\n"
              f"Diferencia entre la cantidad de números positivos y negativos: {diferencia}\n")
      




    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
