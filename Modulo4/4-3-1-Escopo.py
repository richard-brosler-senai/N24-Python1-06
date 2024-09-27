from click import clear
def funcao():
    global idade, nome # Habilitando modificação na global
    print("funcao antes idade=",idade, id(idade))
    valor = 10
    print("valor",valor)
    # contexto função
    idade = 50
    print("funcao depois idade=",idade, id(idade))
    nome = "Richard"

clear()
# Contexto Global
idade = 47
funcao()
print("principal idade=",idade,id(idade),nome)
# Vai dar erro a linha de baixo
# A variavel valor só existe na funcao
# print(valor)