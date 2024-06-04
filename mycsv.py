import pandas as pd
import random

# Function to generate random names
def random_name():
    first_names = ["João", "Maria", "Carlos", "Ana", "José", "Paula", "Pedro", "Clara", "Rafael", "Juliana"]
    last_names = ["Silva", "Santos", "Oliveira", "Pereira", "Costa", "Rodrigues", "Martins", "Almeida", "Barbosa", "Melo"]
    return f"{random.choice(first_names)} {random.choice(last_names)}"

# Function to generate random OAB number
def random_oab():
    return f"{random.randint(10000, 99999)}/{random.choice(['SP', 'RJ', 'MG', 'RS', 'PR', 'SC', 'BA', 'PE'])}"

# Function to generate random CPF
def random_cpf():
    return f"{random.randint(100, 999)}.{random.randint(100, 999)}.{random.randint(100, 999)}-{random.randint(10, 99)}"

# Function to generate random CNPJ
def random_cnpj():
    return f"{random.randint(10, 99)}.{random.randint(100, 999)}.{random.randint(100, 999)}/{random.randint(1000, 9999)}-{random.randint(10, 99)}"

# Function to generate random case class/subject
def random_case():
    classes = ["Ação de Cobrança", "Ação de Indenização", "Ação de Obrigação de Fazer", "Ação de Execução", "Ação Revisional"]
    return random.choice(classes)

def random_classe():
    classe = ["Embargos de Declaração Cível", "Apelação Cível"]
    return random.choice(classe)

# Function to generate random county
def random_comarca():
    comarcas = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Porto Alegre", "Curitiba", "Florianópolis", "Salvador", "Recife"]
    return random.choice(comarcas)

# Function to generate random UF
def random_uf():
    ufs = ["SP", "RJ", "MG", "RS", "PR", "SC", "BA", "PE"]
    return random.choice(ufs)

# Create dataframe with additional column
data_updated = {
    "Nome do Advogado Principal": [random_name() for _ in range(40)],
    "Inscrição OAB": [random_oab() for _ in range(40)],
    "CPF do autor": [random_cpf() for _ in range(40)],
    "CNPJ do Réu": [random_cnpj() for _ in range(40)],
    "Ação": [random_case() for _ in range(40)],
    "Classe": [random_classe() for _ in range(40)],
    "Comarca": [random_comarca() for _ in range(40)],
    "UF": [random_uf() for _ in range(40)],
    "Juizado Especial": ["Juizado especial cívil"]
}

df_updated = pd.DataFrame(data_updated)
csv_path_updated = "C:/Users/202402630661/Desktop/direito/casos_civeis_com_juizado.csv"
df_updated.to_csv(csv_path_updated, index=False)