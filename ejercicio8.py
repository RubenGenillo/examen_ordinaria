import lorem

def detectar_Nessi(texto):
    if (" tree fiddy " in texto or " 3.50 " in texto)or " three fifty " in texto:
        return True
    elif (texto == "tree fiddy" or texto == "3.50")or texto == "three fifty":
        return True
    elif ((texto == "tree fiddy " and texto[0:11] == "tree fiddy ") or (texto == "3.50 " and texto[0:5] == "3.50 "))or (texto == "three fifty " and texto[0:12] == "three fifty "):
        return True
    elif ((texto == " tree fiddy" and texto[::-1][0:11] == " yddif eert ") or (texto == " 3.50" and texto[::-1][0:5] == "05.3 "))or (texto == " three fifty" and texto[::-1][0:12] == "ytfif eerht "):
        return True
    else:
        return False

def main():
    print(detectar_Nessi(lorem.text()))

if __name__ == '__main__':
    main()