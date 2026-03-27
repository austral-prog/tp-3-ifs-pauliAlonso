def triangle():

    num1 = int(input())
    num2 = int(input())
    num3 = int(input())

    if num1 + num2 > num3 and num1 + num3 > num2 and num2 + num3 > num1:
        print("Los lados forman un triangulo valido") 
    else:
        print("Los lados no forman un triangulo valido")

