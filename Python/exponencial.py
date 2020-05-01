import sys

def busquedaExponencial(lista, limiteSuperior, elemento):
    pivot = int(limiteSuperior / 2)
    index = pivot 
    while(True):
        mitad = int(limiteSuperior / 4)
        try:
            if(lista[pivot + mitad] == elemento):  
                return pivot + mitad
            else:
                if(limiteSuperior/2 == 1):
                    break
                else:
                    if(lista[pivot + mitad] > elemento):
                        limiteSuperior/=2
                    else:       
                        pivot+=mitad
        except Exception as e:          
            limiteSuperior/=2
    return -1

def main():
    f = open(str(sys.argv[1]),'r')
    text = f.readlines()

    lista = [int(x) for x in text[0].split(",")]

    x = 1

    while(True):
        try:
            if(lista[x] > int(text[1])):
                index = busquedaExponencial(lista,x, int(text[1]))
                break
            else:
                x = x*2
        except:
            index = busquedaExponencial(lista,x, int(text[1]))
            break

    if(index == -1):
        print("No está en la lista")
    else:
        print(text[0])
        print("")
        print(f"El elemento {int(text[1])} está en el indice {index}")


if __name__ == "__main__":
    main()
