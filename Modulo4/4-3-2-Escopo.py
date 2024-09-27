def calcular(a, b):
    ret = a + b
    a = 15
    return ret

def adicionar_na_lista(lst,valor):
    lst.append(valor)

def fatorial_rec(numero):
    if numero < 2: return 1
    return numero * fatorial_rec(numero-1)

x = 5
y = 10
print('calculo=',calcular(x,y))
print('x=',x)
lista = [1,2,3]
adicionar_na_lista(lista,9)
print(lista)
print(fatorial_rec(5))