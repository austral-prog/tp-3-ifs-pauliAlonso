def calculator():
   
    num1 = float(input())
    num2 = float(input())
    operacion = input()
 
    if operacion == "+":
        print(f"Resultado: {num1 + num2}")
    elif operacion == "-":
        print(f"Resultado: {num1 - num2}") 
    elif operacion == "*":
        print(f"Resultado: {num1 * num2}") 
    elif operacion == "/":
        if num2 == 0: 
            print("Error: division por cero") 
        else:
            print(f"Resultado: {num1 / num2}") 
    else:
        print("Operacion invalida") 


