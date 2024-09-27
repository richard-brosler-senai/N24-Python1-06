from click import clear
clear() # limpar a tela
blocks = int(input("Insira o número de blocos:"))  
 # Escreva seu código aqui.
altura = 0
total = 0
while total+altura+1 <= blocks:
    altura += 1     # altura = altura + 1
    total += altura # total = total + altura

#
print("A altura da pirâmide:", altura)