import pandas as pd
import pyautogui
import time
import os


pyautogui.FAILSAFE = False  # Desativa o fail-safe

# Salvar a posição inicial do cursor
posicao_inicial = pyautogui.position()

# Caminho da pasta que contém as planilhas
caminho_pasta = 'C:\\Robo\\arquivos-pedidos\\'

# Obter a lista de arquivos Excel na pasta
arquivos_excel = [f for f in os.listdir(caminho_pasta) if f.endswith('.xlsx')]

for arquivo in arquivos_excel:
    print(f"Iniciando o processamento da planilha: {arquivo}")  # Informar a planilha que está sendo processada
    caminho_arquivo = os.path.join(caminho_pasta, arquivo)
    df = pd.read_excel(caminho_arquivo, usecols=[0])  # Lê apenas a primeira coluna

    # Converte a coluna em uma lista de strings (removendo valores nulos)
    linhas = df.iloc[:, 0].dropna().tolist()

# Passo 1: Selecionar a opção da tecla F2
    pyautogui.click(x=20, y=187) 
    time.sleep(5)  # Pequena pausa para garantir o processamento

# Passo 2: Informar cliente e filial
    pyautogui.click(x=114, y=167)  # Substitua (x, y) com as coordenadas reais do campo Cliente/Filial
    pyautogui.write('007 0')  # Informar cliente e filial
    time.sleep(2)

# Passo 3: Selecionar a natureza da operação
    pyautogui.click(x=296, y=465)  # Clicar no campo Natureza da Operação
    time.sleep(1)

    # Simular pequenos movimentos do mouse
    pyautogui.moveRel(0, 1)  # Mover um pixel para baixo
    pyautogui.moveRel(0, -1) # Mover um pixel para cima
    time.sleep(1)

    # operação
    pyautogui.click(x=150, y=250)  # Substitua (x, y) com as coordenadas reais do campo Natureza da Operação
    time.sleep(0.05)
    
    # Digitar o '5927-03' com intervalo mais rápido entre as teclas
    pyautogui.click(x=229, y=459)
 
    pyautogui.write('5927-02', interval=0.05)  # Aumente ou diminua o valor de interval para ajustar a velocidade
    time.sleep(0.3)

    time.sleep(5)

    # Pressionar 'Enter' para confirmar a seleção
    pyautogui.press('enter')

# Passo 4: Clicar em avançar
    pyautogui.click(x=768, y=70)  # Substitua (x, y) com as coordenadas reais do botão Avançar
    time.sleep(1)

# Passo 5: Inserir produtos item a item na planilha
    for linha in linhas:
        pyautogui.click(x=491, y=57)  # Substitua (x, y) com as coordenadas reais do campo de inserção do produto
        pyautogui.write(str(linha))  # Digita o produto atual
        pyautogui.press('enter')  # Confirma o produto e passa para o próximo
        time.sleep(0.5)  # Pequena pausa para garantir que o sistema tenha tempo de processar

# Passo 6: Finalizar F12 - processo de emissão
    pyautogui.press('F12')
    time.sleep(2)

    pyautogui.click(x=299, y=143) #possicionar e dar esc
    pyautogui.press('Esc')
    time.sleep(2)
    
    pyautogui.click(x=448, y=346)  # Substitua (x, y) com as coordenadas reais do campo Cliente/Filial
    pyautogui.write('361713')  # Preencher senha
    time.sleep(2)
    
    pyautogui.click(x=635, y=374)
    time.sleep(30)

# Fim do processo do robo em tela

    # Imprimir mensagem após finalizar cada planilha
    print(f'Finalizado o processamento da planilha: {arquivo}')

    # Voltar o cursor para a posição inicial
    pyautogui.moveTo(posicao_inicial)

# Imprimir mensagem após finalizar todas as planilhas
print('Processo completo para todas as planilhas.')

# Voltar o cursor para a posição inicial ao final
pyautogui.moveTo(posicao_inicial)

### -- Script Criado em 22/08/2024 -- ### -->MaYaRa<--
### -- Script Atualizando em 28/08/2024 -- ### -->MaYaRa<--
