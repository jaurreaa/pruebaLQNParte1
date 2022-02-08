"""
    Algoritmo que imprima los números del 0 al 100. Adicionalmente debe
    imprimirse en la misma línea la palabra buzz en caso de que el número sea par. Sí el
    número es múltiplo de 5 debe imprimirse en la misma línea la palabra bazz.

"""
for x in range (101):
    if (x!= 0 and x % 2 == 0 and x % 5 == 0):
        print(f'{x} buzz bazz')
    elif (x!= 0 and x % 2 == 0):
        print(f'{x} buzz')
    elif (x!= 0 and x % 5 == 0):
        print(f'{x} bazz')
    else:
        print(x)

