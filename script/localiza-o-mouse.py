import pyautogui
import time

# Espera 5 segundos antes de capturar a posição
time.sleep(5)

# Pega a posição atual do mouse
x, y = pyautogui.position()
print(f"Posição do mouse: ({x}, {y})")

