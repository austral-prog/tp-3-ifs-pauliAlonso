def weekday():

    dia_semana = input()
    dia_semana = dia_semana.lower()

    if dia_semana == "lunes" or dia_semana == "martes" or dia_semana == "miercoles" or dia_semana == "jueves" or dia_semana == "viernes":
        print("Dia habil")
    else:
        print("Fin de semana")
