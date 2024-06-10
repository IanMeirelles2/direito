import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#lendo o arquivo csv
df = pd.read_csv('/workspaces/direito/database/db_updated.csv', sep=',', encoding='utf-8')

#agrupar por por nome e contar o número de casos em cada um
cases_by_name = df.groupby('Nome do Advogado Principal').size().reset_index(name='Número de Casos')

#criar uma lista com os nomes dos advogados que possuem mais de 10 casos
cases_choices = []
for name in cases_by_name['Nome do Advogado Principal']:    
    cases_separate = cases_by_name[cases_by_name['Nome do Advogado Principal'] == name]
    if cases_separate['Número de Casos'].values[0] > 10:
        cases_choices.append(cases_separate['Nome do Advogado Principal'].values[0])

#para cada advogado com mais de 10 casos, contar o número de casos por ação e por CNPJ
for nm in cases_choices:
    cases = df.loc[df['Nome do Advogado Principal'] == nm]
    actions = cases['Ação'].value_counts().reset_index(name='Número de Casos')
    cnpj = cases['CNPJ do Réu'].value_counts().reset_index(name='Número de Casos')
    print(f"\n{nm.upper()} \n\nAções: \n{actions}\n\nCNPJ: \n{cnpj}")

