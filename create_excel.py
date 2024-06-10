import pandas as pd
import random

# Dicionário para armazenar os números OAB por nome de advogado
oab_by_name = {}

# Função para gerar nomes aleatórios
def random_name():
    first_names = ["João", "Maria", "Carlos", "Ana", "José", "Paula", "Pedro"]
    last_names = ["Silva", "Santos", "Oliveira", "Pereira", "Almeida"]
    return f"{random.choice(first_names)} {random.choice(last_names)}"

# Função para gerar números OAB aleatórios
def random_oab(name):
    if name in oab_by_name:
        return oab_by_name[name]
    else:
        oab = f"{random.randint(10000, 99999)}/{random.choice(['SP', 'RJ', 'MG', 'RS', 'PR', 'SC', 'BA', 'PE'])}"
        oab_by_name[name] = oab
        return oab

# Função para gerar CPF aleatório
def random_cpf():
    return f"{random.randint(100, 999)}.{random.randint(100, 999)}.{random.randint(100, 999)}-{random.randint(10, 99)}"

# Função para gerar CNPJ aleatório
def random_cnpj():
    return f"{random.randint(10, 99)}.{random.randint(100, 999)}.{random.randint(100, 999)}/{random.randint(1000, 9999)}-{random.randint(10, 99)}"

# Função para gerar tipos de ação aleatórios
def random_case():
    classes = ["Ação de Cobrança", "Ação de Indenização", "Ação de Obrigação de Fazer", "Ação de Execução", "Ação Revisional"]
    return random.choice(classes)

# Função para gerar classes aleatórias
def random_classe():
    classes = ["Embargos de Declaração Cível", "Apelação Cível"]
    return random.choice(classes)

# Função para gerar comarcas aleatórias
def random_comarca():
    comarcas = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Porto Alegre", "Curitiba", "Florianópolis", "Salvador", "Recife"]
    return random.choice(comarcas)

# Função para gerar UFs aleatórios
def random_uf():
    ufs = ["SP", "RJ", "MG", "RS", "PR", "SC", "BA", "PE"]
    return random.choice(ufs)

# Criar dataframe com colunas adicionais
data_updated = {
    "Nome do Advogado Principal": [],
    "Inscrição OAB": [],
    "CPF do autor": [],
    "CNPJ do Réu": [],
    "Ação": [],
    "Classe": [],
    "Comarca": [],
    "UF": [],
    "Juizado Especial": []
}

for _ in range(70):
    name = random_name()
    data_updated["Nome do Advogado Principal"].append(name)
    data_updated["Inscrição OAB"].append(random_oab(name))
    data_updated["CPF do autor"].append(random_cpf())
    data_updated["CNPJ do Réu"].append(random_cnpj())
    data_updated["Ação"].append(random_case())
    data_updated["Classe"].append(random_classe())
    data_updated["Comarca"].append(random_comarca())
    data_updated["UF"].append(random_uf())
    data_updated["Juizado Especial"].append("Juizado especial cívil")

df_updated = pd.DataFrame(data_updated)

# Caminho completo do arquivo para salvar
csv_path_updated = "E:\ibmec _ian\projeto-direito"

# Salvando o dataframe como um arquivo CSV
df_updated.to_csv(csv_path_updated, index=False)

print(f"Arquivo CSV salvo em {csv_path_updated}")
