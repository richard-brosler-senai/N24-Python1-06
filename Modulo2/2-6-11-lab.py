# Importando a função clear da biblioteca click
from click import clear
clear() # Limpa a tela
hour = int(input("Hora de início (horas): "))
mins = int(input("Hora de início (minutos): "))
dura = int(input("Duração do evento (minutos): "))
# Escreva seu código aqui.
apoio = hour * 60 + mins + dura # Total do tempo em minutos
hour = apoio // 60 % 24 # Divisão inteira por 60
mins = apoio % 60 # Resto da divisão
print(f"{hour:02d}",f"{mins:02d}",sep=":") # Formata 00:00
# min = 10
print(min(10,2,3))
