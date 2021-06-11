def separarNumero(k,n):
    lista_unidade = []
    for i in range (0, n):
        lista_unidade.append(list(k))
    converterParaInteiro(lista_unidade)

def converterParaInteiro(listaUnidade):
    lista_int = []
    for j in range(0,len(listaUnidade)):
        for t in range(0,len(listaUnidade[j])):
            lista_int.append(int(listaUnidade[j][t]))
    somarNumeros(lista_int)

def somarNumeros(lista):
    verificarDigito(sum(lista))

def verificarDigito(numero):
    numeroEmString = str(numero)
    if len(numeroEmString)==1:
        print("O digito único é: ", numero)
    else:
        separarNumero(numeroEmString,1)


k = input()
n = int(input())

separarNumero(k,n)




# numero = sum(lista_int)
# print(numero)
# lista_unidade = lista_num.split("")

