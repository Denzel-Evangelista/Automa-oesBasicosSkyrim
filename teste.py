import pyautogui
import keyboard
import time

# Aguarda 5 segundos para você posicionar o jogo na tela
time.sleep(5)

while True:
    # Simula o clique do botão direito e esquerdo do mouse
    pyautogui.mouseDown(button='right')
    pyautogui.mouseDown(button='left')
    time.sleep(1)  # Tempo mais curto para o clique
    pyautogui.mouseUp(button='right')
    pyautogui.mouseUp(button='left')
    time.sleep(1)  # Tempo mais curto para transição
    
    # Simula o pressionamento da tecla 't' que é usada para ativar o tempo de espera no jogo
    keyboard.press_and_release('t')
    time.sleep(1)  # Aguarda um pouco para garantir que 't' foi registrado

    # Simula o pressionamento da tecla 'ENTER'
    keyboard.press_and_release('enter')
    time.sleep(3)  # Tempo maior após 'ENTER' para garantir que a ação é registrada
