# Primeiro importamos o date do módulo datetime
import datetime
from datetime import date

# Depois é só utilizá-lo dentro de uma variável qualquer, da forma que precisamos 
data = date(2025, 4, 14)
print(data) # 2025-04-14

# DOCUMENTAÇÃO PYTHON - DATETIME
# https://docs.python.org/3.13/search.html?q=datetime

# Printando a data atual
print(date.today()) #2025-04-14


# Sobre o datetime

# Data, hora e segundos.
data_hora = datetime.datetime(2024, 3, 14, 13, 48) # ano, mês, dia, horas e minutos
print(data_hora)
# Obs: Se não estipularmos a hora, minutos e segundos, eles irão aparecer como zero no datetime.







