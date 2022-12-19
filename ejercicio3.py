#Hago una funcion que me de el nombre de cualquier numero
def obtener_nombre(n):
    numero = str(n)
    listanum = [*numero]
    listaletras = []
    dict = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
    }

    for elemento in listanum:
        listaletras.append(dict.get(int(elemento)))

    return("".join(listaletras))

#Hago una funcion que me de una lista con el nombre de los numeros hasta que el numero tenga 4 letras
def numbersOfLetters(n):
    listanombres = []
    nombre = obtener_nombre(n)
    listanombres.append(nombre)
    while len(listanombres[-1]) != 4:
        numero_actual = len(listanombres[-1])
        nombre = obtener_nombre(numero_actual)
        listanombres.append(nombre)
    listanombres.append("four")
    return listanombres

def main():
    numero = 60
    print(numbersOfLetters(numero))
    numero2 = 1
    print(numbersOfLetters(numero2))

if __name__ == "__main__":
    main()