import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Un gimnasio quiere medir el progreso de sus clientes, para ello se debe ingresar:

Nombre

Edad (debe ser mayor a 12)

Altura (no debe ser negativa)

Días que asiste a la semana (1, 3, 5)

Kilos que levanta en peso muerto (no debe ser cero, ni negativo)

 

No sabemos cuántos clientes serán consultados.

Se debe informar al usuario:

El promedio de kilos que levantan las personas que asisten solo 3 días a la semana.

El porcentaje de clientes que asiste solo 1 día a la semana.

Nombre y edad del cliente con más altura.

Determinar si los clientes eligen más ir 1, 3 o 5 días

Nombre y cantidad de kilos levantados en peso muerto, de la persona más joven que solo asista 5 días a la semana.

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        seguir = True
        contador_dias_1_semana = 0
        contador_dias_3_semana = 0
        contador_dias_5_semana = 0
        acumulador_kilos_dias_3 = 0
        bandera_altura = True
        max_joven_5_dias = 150  
        nombre_max_joven_5_dias = ""
        kilos_max_joven_5_dias = 0

        while seguir:

            # Pedir nombre
            nombre = prompt("Datos", "Ingrese su nombre")


            # Pedir edad y validarla
            edad = prompt("Datos", "Ingrese su edad")
            edad = int(edad)
            while edad < 11:
                alert("", "Por favor ingrese una edad valida.")
                edad = prompt("Datos", "Ingrese su edad")
                edad = int(edad)


            # Pedir altura y validarla
            altura = prompt("datos", "Ingrese su altura en cm")
            altura = float(altura)
            while altura < 0:
                alert("Error", "Ingrese un altura valida")
                altura = prompt("datos", "Ingrese su altura en cm")
                altura = float(altura)

                
            # Pedir dias que asiste y validarlos - Validar numeros
            dias_asiste = prompt("Datos", "Ingrese si asiste al gimnasio 1, 3 o 5 dias")
            dias_asiste = int(dias_asiste)
            while dias_asiste != 1 and dias_asiste != 3 and dias_asiste != 5:
                alert("Error", "Ingrese 1 dia, 3 dias o 5 dias.")
                dias_asiste = prompt("Datos", "Ingrese si asiste al gimnasio 1, 3 o 5 dias")
                dias_asiste = int(dias_asiste)


            # Validar kilos en peso muerto
            kilos_peso_muerto = prompt("Datos", "Ingrese su peso en el peso muerto")
            kilos_peso_muerto = int(kilos_peso_muerto)
            while kilos_peso_muerto <= 0:
                alert("Error", "Ingrese una cantidad valida")
                kilos_peso_muerto = prompt("Datos", "Ingrese su peso en el peso muerto")
                kilos_peso_muerto = int(kilos_peso_muerto)


            # Preguntar si desea continuar, si pone No (False) rompe, si pone Si (True) continua
            seguir = question("Datos", "Desea seguir ingresando datos?")

            
        # El minimo edad
        if dias_asiste == 5 and edad < max_joven_5_dias:
            max_joven_5_dias = edad
            nombre_max_joven_5_dias = nombre
            kilos_max_joven_5_dias = kilos_peso_muerto


        # Sacar el maximo 
        if bandera_altura == True:
            max_altura = altura
            nombre_max_altura = nombre
            edad_max_altura = edad
        else:
            if altura > max_altura:
                max_altura = altura
                nombre_max_altura = nombre
                edad_max_altura = edad


        # Contadores de los dias
        if dias_asiste == 1:
            contador_dias_1_semana += 1
        else:
            if dias_asiste == 3:
                contador_dias_3_semana += 1
                acumulador_kilos_dias_3 += kilos_peso_muerto
            else:
                if dias_asiste == 5:
                    contador_dias_5_semana += 1

                    
        # Hace el promedio, pero si ningun usario ingreso dia 3, da 0
        if contador_dias_3_semana > 0:
            promedio_kilos_3_dias = acumulador_kilos_dias_3 / contador_dias_3_semana
        else:
            promedio_kilos_3_dias = 0

        # Da el porcentaje de los usarios que asisten solo 1 dia, sino no se ingreso nunca 1 dia, da 0
        total_clientes = contador_dias_1_semana + contador_dias_3_semana + contador_dias_5_semana
        if contador_dias_1_semana != 0:
            porcentaje_dia_1 = (contador_dias_1_semana * 100) / total_clientes
        else:
            porcentaje_dia_1 = 0
             

        alert("Resultados", f"Promedio de kilos para personas que asisten solo 3 días a la semana: {promedio_kilos_3_dias}")
        alert("Resultados", f"Porcentaje de clientes que asisten solo 1 día a la semana: %{porcentaje_dia_1}")
        alert("Resultados", f"Cliente con más altura: Nombre: {nombre_max_altura}, Edad: {edad_max_altura}, Altura: {max_altura} cm")
        alert("Resultados", f"Número de clientes que asisten a la semana: 1 día: {contador_dias_1_semana}, 3 días: {contador_dias_3_semana}, 5 días: {contador_dias_5_semana}")
        alert("Resultados", f"Persona más joven que asiste 5 días a la semana: Nombre: {nombre_max_joven_5_dias}, Kilos levantados en peso muerto: {kilos_max_joven_5_dias}")


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()