# Si tiene cantiadad con un for (ej: for contador in range(cantiadad pedida))
# Si no se sabe cuantos datos se van a ingresar (while True:)


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


            # Validar un string
            clave_ingresada = prompt("", "Ingrese la clave:")
            if clave_ingresada == clave:
                alert("Clave!", "La clave ingresada es correcta.")
                break
            else:
                alert("Incorrecto", "La contraseña ingresada es incorrecta. Por favor, inténtelo nuevamente.")
                continue


            # Validar letras
            letra_ingresada = prompt("Letras", "Por favor, ingrese una letra")
            letra_ingresada_mayuscula = letra_ingresada.upper()
            if letra_ingresada_mayuscula == "U" or letra_ingresada_mayuscula == "T" or letra_ingresada_mayuscula == "N":
                alert(titulo_alert, mensaje_1)
                break
            else:
                alert(titulo_alert, mensaje_2)
                continue

