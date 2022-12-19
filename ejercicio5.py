#Creo una fución llamada hollow_triangle que con una altura cree un triangulo con # y _
def hollow_triangle(altura):
    numero = altura*2 -1
    lista = []
    centro = altura
    cadena = "_"*numero
    for i in range(centro-1):
        print(lista)
        cadena2 = [*cadena]
        cadena2[centro-i-1] = "#"
        cadena2[centro+i-1] = "#"
        cadena2 = "".join(cadena2)
        lista.append(cadena2)
    lista.append("#"*numero)
    return lista

def main():
    print(hollow_triangle(6))
    print(hollow_triangle(9))

if __name__ == "__main__":
    main()