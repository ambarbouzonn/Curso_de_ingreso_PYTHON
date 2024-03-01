import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Ambar Morena
apellido: Bouzon
---
Enunciado:
De 5 mascotas que ingresan a una veterinaria se deben tomar y validar los siguientes datos.
Nombre
Tipo (gato ,perro o exotico)
Peso ( entre 10 y 80)
Sexo( F o M )
Edad(mayor a 0)

Pedir datos por prompt y mostrar por print, se debe informar:
Informe A- Cuál fue el sexo menos ingresado (F o M)
Informe B- El porcentaje de mascotas hay por tipo (gato ,perro o exotico)
Informe C- El nombre y tipo de la mascota menos pesada
Informe D- El nombre del perro más joven
Informe E- El promedio de peso de todas las mascotas

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        titulo = "Validacion de Datos"
        contador_sexo__mascota_f = 0
        contador_sexo__mascota_m = 0
        contador_perros = 0
        contador_gatos = 0
        contador_exoticos = 0
        acumulador_peso_mascotas = 0
        peso_mascota_menor = 80
        nombre_mascota_menor = ""
        tipo_mascota_menor = ""
        bandera_perro_joven = True



        for contador in range(1, 6):
            nombre_mascota = prompt(titulo, "Por favor, ingrese su nombre")

            tipo_mascota = prompt(titulo, "Por favor, ingrese si su mascota es un Perro, Gato o Exotico").capitalize()
            while tipo_mascota != "Perro" and tipo_mascota != "Gato" and tipo_mascota != "Exotico":
                tipo_mascota = prompt(titulo, "Por favor, ingrese si su mascota es un Perro, Gato o Exotico").capitalize()
                
            peso_mascota = prompt(titulo, "Por favor, ingrese el peso de la mascota")
            peso_mascota = int(peso_mascota)
            while peso_mascota < 10 or peso_mascota > 80:
                peso_mascota = prompt(titulo, "Por favor, ingrese el peso de la mascota")
                peso_mascota = int(peso_mascota)

            sexo_mascota = prompt(titulo, "Por favor, ingrese el sexo de la mascota").capitalize()
            while sexo_mascota != "F" and sexo_mascota != "M":
                sexo_mascota = prompt(titulo, "Por favor, ingrese el sexo de la mascota")
                
            edad_mascota = prompt(titulo, "Por favor, ingrese la edad de la mascota")
            edad_mascota = float(edad_mascota)
            while edad_mascota < 0:
                edad_mascota = prompt(titulo, "Por favor, ingrese la edad de la mascota")
                edad_mascota = float(edad_mascota)
                

            # Contador de sexos
            if sexo_mascota == "F":
                contador_sexo__mascota_f += 1
            else:
                contador_sexo__mascota_m += 1


            # Contador de tipos de mascotas
            match tipo_mascota:
                case "Perro":
                    contador_perros += 1
                case "Gato":
                    contador_gatos += 1
                case "Exotico":
                    contador_exoticos += 1


            # Mascota de menor peso
            if peso_mascota < peso_mascota_menor:
                peso_mascota_menor = peso_mascota
                nombre_mascota_menor = nombre_mascota
                tipo_mascota_menor = tipo_mascota

            # Perro mas joven
            if tipo_mascota == "Perro" and bandera_perro_joven == True:
                edad_perro_joven = edad_mascota
                nombre_perro_joven = nombre_mascota
            else:
                if edad_mascota < edad_perro_joven:
                    nombre_perro_joven = nombre_mascota


            # Peso total y promedio de mascotas
            acumulador_peso_mascotas += peso_mascota
            promedio_peso_mascotas = acumulador_peso_mascotas / 5


            # Porcetaje de cantidad de maascotas por tipo
            total_mascotas = contador_gatos + contador_perros + contador_exoticos
            if contador_gatos != 0:
                porcentaje_gato = (contador_gatos / total_mascotas) * 100
            else:
                porcentaje_gato = 0
            
            if contador_perros != 0:
                porcentaje_perro = (contador_perros / total_mascotas) * 100
            else:
                porcentaje_perro = 0
            
            if contador_exoticos != 0:
                porcentaje_exotico = (contador_exoticos / total_mascotas) * 100
            else:
                porcentaje_exotico = 0


        # Informe A
        print("Sexo menos ingresado:", 'F' if contador_sexo__mascota_f < contador_sexo__mascota_m else 'M')
        # Informe B
        print("Porcentaje de mascotas por tipo:\n"
              f"Gato: {porcentaje_gato}%\n"
              f"Perro: {porcentaje_perro}%\n"
              f"Exotico: {porcentaje_exotico}%\n")
        # Informe C
        print(f"La mascota menos pesada es: Nombre: {nombre_mascota_menor} - Tipo: {tipo_mascota_menor}")
        # Informe D
        print(f"El nombre del perro mas joven es: {nombre_perro_joven}")
        # Informe E
        print(f"El promedio de peso de todas las masscotas ingresadas da: {promedio_peso_mascotas}")

        
           




if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
