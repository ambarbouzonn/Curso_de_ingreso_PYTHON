import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
TP: For_UTN_Factory
---
Enunciado:
UTN Software Factory está en la búsqueda de programadores para incorporar a su equipo de 
trabajo. En las próximas semanas se realizará un exhaustivo proceso de selección. Para ello se 
ingresarán los siguientes datos de los 10 postulantes para luego establecer distintas métricas 
necesarias para tomar decisiones a la hora de la selección:

Nombre
Edad (mayor de edad)
Género (F-M-NB)
Tecnología (PYTHON - JS - ASP.NET)
Puesto (Jr - Ssr - Sr)

Informar por pantalla:
a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
b. Nombre del postulante Jr con menor edad.
c. Promedio de edades por género.
d. Tecnologia con mas postulantes (solo hay una).
e. Porcentaje de postulantes de cada genero.

Todos los datos se ingresan por prompt y los resultados se muestran por consola (print)

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        titulo = "Datos!"
        menor_edad_jr = None
        nombre_menor_edad_jr = None
        acumulador_nb_asp_js_ssr = 0
        acumulador_nb = 0
        acumulador_f = 0
        acumulador_m = 0
        acumulador_edades_nb = 0
        acumulador_edades_f = 0
        acumulador_edades_m = 0
        acumulador_tecnologia_python = 0
        acumulador_tecnologia_js = 0
        acumulador_tecnologia_asp = 0
        tecnologia_mas_postulantes = ""
        


        for contador in range(1, 11):
            nombre = prompt(titulo, "Por favor, ingrese su nombre")
            edad = int(prompt(titulo, "Por favor, ingrese su edad"))
            genero = prompt(titulo, "Por favor, ingrese solo la primera letra de su genero")
            tecnologia = prompt(titulo, "Ingrese la teclogia que utiliza (PYTHON - JS - ASP.NET)")
            puesto = prompt(titulo, "Por favor, ingrese su puesto (Jr - Ssr - Sr)")

            # a
            if genero == "NB" and (tecnologia == "ASP.NET" or tecnologia == "JS") and 25 < edad < 40 and puesto == "Ssr":
                acumulador_nb_asp_js_ssr += 1

            # b
            if puesto == "Jr" and (menor_edad_jr is None or edad < menor_edad_jr):
                menor_edad_jr = edad
                nombre_menor_edad_jr = nombre

            # c
            if genero == "F":
                acumulador_f += 1
                acumulador_edades_f += edad
            
            if genero == "M":
                acumulador_m += 1
                acumulador_edades_m += edad

            if genero == "NB":
                acumulador_nb += 1
                acumulador_edades_nb += edad

            # d
            match tecnologia:
                case "PYTHON" | "python":
                    acumulador_tecnologia_python += 1
                case "JS" | "js":
                    acumulador_tecnologia_js += 1
                case "ASP.NET" |"asp.net":
                    acumulador_tecnologia_asp += 1
            
            if acumulador_tecnologia_python >= acumulador_tecnologia_js and acumulador_tecnologia_python >= acumulador_tecnologia_asp:
                tecnologia_mas_postulantes = "PYTHON"
            else: 
                if acumulador_tecnologia_js >= acumulador_tecnologia_python and acumulador_tecnologia_js >= acumulador_tecnologia_asp:
                    tecnologia_mas_postulantes = "JS"
                else:
                    if acumulador_tecnologia_asp >= acumulador_tecnologia_python and acumulador_tecnologia_asp >= acumulador_tecnologia_js:
                        tecnologia_mas_postulantes = "ASP.NET"

                
        # Promedio de edades por genero
        promedio_edades_f = acumulador_edades_f / acumulador_f if acumulador_f else 0
        promedio_edades_m = acumulador_edades_m / acumulador_m if acumulador_m else 0
        promedio_edades_nb = acumulador_edades_nb / acumulador_nb if acumulador_nb else 0


        # Porcetaje de postulantes por genero
        total_postulantes = acumulador_f + acumulador_m + acumulador_nb
        porcentaje_f = (acumulador_f / total_postulantes) * 100 if total_postulantes else 0
        porcentaje_m = (acumulador_m / total_postulantes) * 100 if total_postulantes else 0
        porcentaje_nb = (acumulador_nb / total_postulantes) * 100 if total_postulantes else 0


        print(f"La cantidad de postulantes NB: {acumulador_nb_asp_js_ssr}")

        print(f"La edad promedio F es: {promedio_edades_f}")
        print(f"La edad promedio M es: {promedio_edades_m}")
        print(f"La edad promedio NB es: {promedio_edades_nb}")

        if nombre_menor_edad_jr is None:
            print("No hay postulantes Jr.") 
        else:
            print(f"El postulante de menor edad en el puesto Jr es: {nombre_menor_edad_jr}")

        print(f"La tecnologia mas postulada es: {tecnologia_mas_postulantes}")

        print(f"El porcetaje de postulantes F es: %{porcentaje_f}")
        print(f"El porcetaje de postulantes M es: %{porcentaje_m}")
        print(f"El porcetaje de postulantes NB es: % {porcentaje_nb}")



if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
