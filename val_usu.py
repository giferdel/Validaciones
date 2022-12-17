def val_usu():
    usu = input('Ingrese usuario: ')
    long =len(usu)
    while long < 5 or long >15:
        if long<5:
            print('El usuario no puede tener menos de 5 caracteres')
            usu = input('Ingrese su Usuario: ')
            long =len(usu)
        elif long>15:
            print('El usuario no puede tener más de 15 caracteres')
            usu = input('Ingrese su Usuario: ')
            long =len(usu)
    print('Usuario correcto')

val_usu()