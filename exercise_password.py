def password():

    contraseña = input()
    caracteres = len(contraseña)
    tiene_numero = ("0" in contraseña or "1" in contraseña or "2" in contraseña
 or "3" in contraseña or "4" in contraseña or "5" in contraseña or "6" in contraseña or "7" in contraseña or "8" in contraseña or "9" in contraseña)

    if caracteres >= 8 and tiene_numero:
        print("Contraseña valida") 
    else:
        if caracteres < 8:
            print("Contraseña muy corta")
        if not tiene_numero:
            print("Debe contener un numero")
