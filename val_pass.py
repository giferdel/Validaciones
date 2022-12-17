import time

def val_pass():
    pas = input('Ingrese contraseña: ')
    long =len(pas)
    while long < 10:
        print('La contraseña debe tener al menos 10 caracteres')
        pas = input('Ingrese contraseña: ')
        long =len(pas)
    verifico = pas.isalnum() #verifico si todos los carateres son alfanumericos --> Tue o False
    while verifico is True:
        print('La contraseña debe tener al menos 1 caracter no alfanumérico')
        pas = input('Ingrese contraseña: ')
        verifico = pas.isalnum()
    # for p in pas:
    #     if p is 
    print('Verificando ontraseña')
    time.sleep(1)
    print('Contraseña aceptada')
val_pass()