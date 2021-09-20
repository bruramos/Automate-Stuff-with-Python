import pyautogui

pyautogui.click(100,100)
pyautogui.typewrite('Hello World!', interval=0.2)
pyautogui.typewrite(['enter']) #pyautogui.press('enter')
pyautogui.typewrite('Bye World!', interval=0.2)

pyautogui.KEYBOARD_KEYS #Lista de teclas especiais

pyautogui.hotkey(['ctrl', 'o']) #Apertar comandos ou teclas juntas
