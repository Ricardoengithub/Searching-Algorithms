import sys

def busquedaBinaria(lista, elemento):
    index = 0
    while(True):
        mitad = int(len(lista) / 2)
        if(lista[mitad] == elemento):  
            index += mitad          
            return index
        else:
            if(len(lista) == 1):
                break
            else:
                if(lista[mitad] > elemento):
                    lista = lista[0:mitad]
                else:
                    lista = lista[mitad:]
                    index += mitad
    return -1
            


def main():
    f = open(str(sys.argv[1]),'r')
    text = f.readlines()

    lista = [int(x) for x in text[0].split(",")]
    index = busquedaBinaria(lista, int(text[1]))    

    if(index == -1):
        print("No está en la lista")
    else:
        print(text[0])
        print("")
        print(f"El elemento {int(text[1])} está en el indice {index}")


if __name__ == "__main__":
    main()
