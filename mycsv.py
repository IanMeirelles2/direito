import pandas as pd
import random

# Função para gerar nomes aleatórios
def random_name():
    first_names = ["João", "Maria", "Carlos", "Ana", "José", "Paula", "Pedro", "Clara", "Rafael", "Juliana"]
    last_names = ["Silva", "Santos", "Oliveira", "Pereira", "Costa", "Rodrigues", "Martins", "Almeida", "Barbosa", "Melo"]
    return f"{random.choice(first_names)} {random.choice(last_names)}"

# Função para gerar números OAB aleatórios
def random_oab():
    return f"{random.randint(10000, 99999)}/{random.choice(['SP', 'RJ', 'MG', 'RS', 'PR', 'SC', 'BA', 'PE'])}"

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
    "Nome do Advogado Principal": [random_name() for _ in range(40)],
    "Inscrição OAB": [random_oab() for _ in range(40)],
    "CPF do autor": [random_cpf() for _ in range(40)],
    "CNPJ do Réu": [random_cnpj() for _ in range(40)],
    "Ação": [random_case() for _ in range(40)],
    "Classe": [random_classe() for _ in range(40)],
    "Comarca": [random_comarca() for _ in range(40)],
    "UF": [random_uf() for _ in range(40)],
    "Juizado Especial": ["Juizado especial cívil" for _ in range(40)]
}

df_updated = pd.DataFrame(data_updated)

# Caminho completo do arquivo para salvar
csv_path_updated = "E:\ibmec _ian\projeto-direito"

# Salvando o dataframe como um arquivo CSV
df_updated.to_csv(csv_path_updated, index=False)

print(f"Arquivo CSV salvo em {csv_path_updated}")