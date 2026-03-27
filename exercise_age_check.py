def age_check():
    
    edad = int(input())
    limite_edad = int(input())
    
    if edad <= 0 or limite_edad <= 0:
        print("Entrada invalida") 
    elif edad >= limite_edad: 
        print("Eres mayor de edad")
    else: 
        print("Eres menor de edad")

    