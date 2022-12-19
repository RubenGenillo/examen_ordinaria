print(ord("c"))
#funcion que mire si tiene letra y la posicion de esta, y si no tiene letra que devuelva -1 para que luego no lo ponga en la nueva lista
def posicion_letra(cadena):
    for i in range(len(cadena)):
        if cadena[i].isalpha():
            return ord(cadena[i])
    return -1

#si ya hay uno con la misma posicon que le sume +1 al key

#funcion que quita letras
def quita_letras(cadena):
    for i in range(len(cadena)):
        if cadena[i].isalpha():
            cadena = cadena.replace(cadena[i], " ")
    cadena = "".join(cadena.split())
    return cadena


#funcion que ordene y retorne el diccionario como lista ordenada
def crea_lista(diccionario):
    lista = []
    for key in sorted(diccionario):
        lista.append(diccionario[key])
    return lista

#funcion que devuelve los numeros ordenados
def orden_num(cadena):
    diccionario = {}
    cadenaSeparada = cadena.split()
    for i in range(len(cadenaSeparada)):
        if posicion_letra(cadenaSeparada[i]) != -1:
            if posicion_letra(cadenaSeparada[i]) in diccionario:
                posicion = posicion_letra(cadenaSeparada[i])
                while posicion in diccionario:
                    posicion += 1
                diccionario[posicion] = quita_letras(cadenaSeparada[i])
            else:
                diccionario[posicion_letra(cadenaSeparada[i])] = quita_letras(cadenaSeparada[i])
    return crea_lista(diccionario)

#funcion que hace la operacion en si
def do_math(cadena):
    pass

def main():
    print(orden_num("24z6 1x23 y369 89a 900b"))
    print(orden_num("24z6 1z23 y369 89z 900b"))
    print(orden_num("10a 90x 14b 78u 45a 7b 34y"))
if __name__ == '__main__':
    main()