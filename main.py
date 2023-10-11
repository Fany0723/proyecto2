from  readchar import readkey, key

print('Escribir un programa que corra un bucle infinito leyendo e imprimiento las teclas y sólo terminará cuando se presione la tecla ↑ indicada como UP')


while True: 
    print('\n\n Presione cualquier tecla:')
    k = readkey()    
    if( k == key.UP):
        break
    print('la tecla fue: ', k)
    