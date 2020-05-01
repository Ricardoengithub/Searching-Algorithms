import sys

def busquedaSecuencial(lista, elemento):
    for i in range(0,len(lista)): 
        if(lista[i] == elemento):
            return i
    return -1    

def main():
    f = open(str(sys.argv[1]),'r')
    text = f.readlines()

    lista = [int(x) for x in text[0].split(",")]

    index = busquedaSecuencial(lista, int(text[1]))

    if(index == -1):
        print("No está en la lista")
    else:
        print(text[0])
        print("")
        print(f"El elemento {int(text[1])} está en el indice {index}")
    

if __name__ == "__main__":
    main()
