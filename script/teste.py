import pandas as pd
import pyautogui
import time
import os


pyautogui.click(x=664, y=406)  # Clicar no campo Natureza da Operação
time.sleep(1)  # Aguardar 1 segundo para garantir que o menu se abra

# Pressionar a seta para baixo 5 vezes para selecionar a opção desejada
for _ in range(3):
    pyautogui.moveRel(1, 0)  # Simula um pequeno movimento do mouse
    pyautogui.press('down')
    time.sleep(1)  # Pequena pausa para garantir que cada movimento seja processado