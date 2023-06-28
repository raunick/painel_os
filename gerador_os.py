import pandas as pd
import random
from datetime import date, timedelta

data = {
    "Número OS": [],
    "Status": [],
    "Prioridade": [],
    "Setor": [],
    "Data": [],
    "Executante": [],
    "Solicitante": []
}

# Exemplo de valores para os executantes e solicitantes
executantes = ["RVVG", "SD", "GC", "FP", "RA"]
solicitantes = ["João", "Maria", "Pedro", "Ana", "Carlos"]

# Obter o mês atual
data_atual = date.today()
mes_atual = data_atual.month

# Gerar dados para 30 dias aleatórios do mesmo mês
for i in range(100):
    dia = random.randint(1, 28)  # Selecionar um dia aleatório dentro do mês
    data_os = date(data_atual.year, mes_atual, dia)
    data["Número OS"].append(f"OS{i+1}")
    if i % 8 == 0:
        data["Status"].append("Aberto")
    elif i % 3 == 0:
        data["Status"].append("Em Processo")
    else:
        data["Status"].append("Encerrada")
    if i % 2 == 0:
        data["Prioridade"].append("Alta")
    elif i % 3 == 1:
        data["Prioridade"].append("Média")
    else:
        data["Prioridade"].append("Baixa")
    if i % 6 == 0:
        data["Setor"].append("CC")
    elif i % 3 == 1:
        data["Setor"].append("FAT")
    elif i % 4 == 2:
        data["Setor"].append("CTI")
    else:
        data["Setor"].append("PA")
    data["Data"].append(data_os)

    # Adicionar executante e solicitante
    executante = random.choice(executantes)
    solicitante = random.choice(solicitantes)
    data["Executante"].append(executante)
    data["Solicitante"].append(solicitante)

df = pd.DataFrame(data)

# Salvar DataFrame em um arquivo CSV
df.to_csv("ordens_de_servico.csv", index=False)
