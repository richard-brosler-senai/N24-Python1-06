from click import clear

def montar_tela(titulo,colunas = 40):
    clear() # Limpando a tela
    # Se for impar o tamanho do texto, coloca 1 espaço
    if len(titulo) % 2 == 1: titulo += ' '
    espacos = (colunas - len(titulo)) // 2
    print('+' + '-' * colunas + '+')
    print('|' + ' ' * espacos + titulo + 
          ' ' * espacos + '|' )
    print('+' + '-' * colunas + '+')

def fatorial(numero):
    apoio = 1
    for vl in range(numero,1,-1):
        apoio *= vl # apoio = apoio * vl
    return apoio

def min_max(lista):
    minimo = lista[0]
    maximo = lista[0]
    for item in lista[1:]:
        if item>maximo: maximo = item
        if item<minimo: minimo = item
    return minimo, maximo # retornando 2 valores

if __name__ == '__main__':
    montar_tela('Richard')
    print(fatorial(5))
    vl1, vl2 = min_max([1,2,3,4,5,6,7,8])
    print(vl1, vl2)
    input("Digite algo para continuar!")