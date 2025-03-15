from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = '2025-04-14 15:30'

print(data_hora_atual) #2025-03-14 15:30

# Note que a data da variável vem no formato US, ou seja, Y-M-D H-M
# Vamos converter essa data para o formato aqui do Brasil, D-M-Y H-M

formatoPT_BR = '%d/%m/%Y' # criamos uma 'máscara' que será exibida no lugar do formato americano

# em seguida, usamos o strtime() para trasnformar o formato US pelo formato BR
print(data_hora_atual.strftime(formatoPT_BR)) # 14/03/2025




# strptime

formatoEN_US = '%Y-%m-%d %H:%M'

data_convertida_EN_US = datetime.strptime(data_hora_str, formatoEN_US)

print(data_convertida_EN_US) # 2025-04-14 15:30:00