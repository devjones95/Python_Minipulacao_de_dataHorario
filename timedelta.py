# DOCUMENTAÇÃO PYTHON - Timedelta
# https://docs.python.org/3.13/library/datetime.html#timedelta-objects

'''
Para Ffazermos operações com tempo, acrescentar e diminuir horas, meses, dias e segundos, precisamos do timedelta.
É ele que nos permite fazer essas operações entre datas e horas
'''
# Supondo que temos um Lava-Rápido

from datetime import timedelta, datetime



tipo_carro = str(input('Insira o tamanho do veículo a ser lavado: P, M ou G ')).upper()

tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now() # a função .now trás a data atual em tempo real

if tipo_carro == 'P':
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f'O carro chegou ás: {data_atual} e ficará pronto ás {data_estimada}.')

elif tipo_carro == 'M':
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f'O carro chegou ás: {data_atual} e ficará pronto ás {data_estimada}.')

else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f'O carro chegou ás: {data_atual} e ficará pronto ás {data_estimada}.')
    