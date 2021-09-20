import pyautogui

width, height = pyautogui.size() #Tamanho da tela

pyautogui.position() #Posição do mouse

pyautogui.moveTo(10, 10, duration=1.5) #Mover mouse para a posição

pyautogui.moreRel(10, 10)#Mover mouse de forma relativa a posição atual

pyautogui.click() #Clicar onde o mouse está
pyautogui.click(288,32) #Clicar em determinada posição na tela
pyautogui.doubleClick(288,32) #Clique duplo com o mouse
pyautogui.rightClick(288,32) #Clique com o botão direito do mouse
