import sys
import math

def busquedaInterpolacion(lista, elemento):
    izq = 0
    der = len(lista)-1
    while(True):
        try:
            if(der < izq):
                return -1

            up = (elemento - lista[izq]) * (der - izq) 
            bottom = lista[der] - lista[izq]
            pos = izq + math.ceil( up / bottom )
            if(lista[pos] == elemento):
                return pos
            else:
                izq+=1
                der-=1
        except ZeroDivisionError:
            izq+=1
            der-=1
        except IndexError:
            return -1
    return -1

def main():
    f = open(str(sys.argv[1]),'r')
    text = f.readlines()

    lista = [int(x) for x in text[0].split(",")]

    x = 1

    index = busquedaInterpolacion(lista, int(text[1]))


    if(index == -1):
        print("No está en la lista")
    else:
        print(text[0])
        print("")
        print(f"El elemento {int(text[1])} está en el indice {index}")


if __name__ == "__main__":
    main()
