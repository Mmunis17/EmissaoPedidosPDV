import pyautogui
import time

# Pausa inicial para permitir que você abra e foque na janela correta
time.sleep(3)

# Mova o mouse para a posição do botão e clique (substitua (x, y) com as coordenadas reais)
pyautogui.click(x=453, y=142)  # Substitua com as coordenadas do botão real


# Pequena pausa para garantir que o clique foi registrado e o campo de texto esteja ativo
time.sleep(1)

# Lista de linhas para inserir no campo de texto
linhas = [
    "Primeira linha de texto",
    "Segunda linha de texto",
    "Terceira linha de texto",
    "Quarta linha de texto"
]

# Loop para inserir cada linha e pular para a próxima linha
for linha in linhas:
    pyautogui.write(linha)  # Digita a linha atual
    pyautogui.press('enter')  # Pressiona Enter para pular para a próxima linha
    time.sleep(0.5)  # Pequena pausa para garantir que o sistema tenha tempo de processar
