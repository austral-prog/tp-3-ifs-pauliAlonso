def discount():
  
    precio_producto = float(input())
    cant_unidades = int(input())
    subtotal = precio_producto * cant_unidades 

    if cant_unidades >= 10:
        porcentaje = 0.20
    elif 5 <= cant_unidades <= 9:
        porcentaje = 0.10
    else:
        porcentaje = 0.0

    monto_descuento = subtotal * porcentaje
    total_final = subtotal - monto_descuento

    print(f"Subtotal: {subtotal}")
    print(f"Descuento aplicado: {int(porcentaje * 100)}%")
    print(f"Monto de descuento: {monto_descuento}")
    print(f"Total final: {total_final}")
