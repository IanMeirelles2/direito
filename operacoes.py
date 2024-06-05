import pandas as pd
df_excel = pd.read_excel('/workspaces/direito/database/dfdireito.xlsx', engine='openpyxl')

# Filtrar todos os casos em que o "UF" é "SP"
cases_sp = df_excel[df_excel['UF'] == 'SP']
print(cases_sp)

# Agrupar por "Comarca" e contar o número de casos em cada uma
cases_by_comarca = df_excel.groupby('Comarca').size().reset_index(name='Número de Casos')
print(cases_by_comarca)

# Calcular quantos casos de cada tipo de "Ação" existem
cases_by_action = df_excel['Ação'].value_counts().reset_index(name='Número de Casos')
cases_by_action.columns = ['Ação', 'Número de Casos']
print(cases_by_action)