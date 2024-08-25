import pandas as pd
import os

# Definir o caminho do arquivo original
caminho_arquivo = "C:\\Webscraping\\outros\\tudo\\produtos_pt_todos.xlsx"  # Substitua pelo caminho do seu arquivo

# Ler o arquivo Excel
df = pd.read_excel(caminho_arquivo)

# Definir o diretório onde os novos arquivos serão salvos
diretorio_destino = "C:\\Webscraping\\outros\\loja-paulista\\"  # Substitua pelo caminho desejado
os.makedirs(diretorio_destino, exist_ok=True)

# Dividir o DataFrame em pedaços de 50 linhas
pedacos = [df[i:i + 50] for i in range(0, len(df), 50)]

# Salvar cada pedaço em um novo arquivo Excel
for idx, pedaco in enumerate(pedacos, start=1):
    nome_arquivo = f"produtos_pt_{str(idx).zfill(2)}.xlsx"  # Nomear o arquivo com número sequencial
    caminho_para_salvar = os.path.join(diretorio_destino, nome_arquivo)
    pedaco.to_excel(caminho_para_salvar, index=False, header=["produtos"])  # Incluir o cabeçalho "produtos"
    
    # Printar uma mensagem após salvar cada planilha
    print(f"Planilha '{nome_arquivo}' foi gerada com sucesso e salva em '{caminho_para_salvar}'.")

print("Processo de divisão concluído.")

