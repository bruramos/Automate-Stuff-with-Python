from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://automatetheboringstuff.com')

elem = browser.find_element_by_css_selector('body > div.main > main > div > ul:nth-child(19) > li:nth-child(1) > a')
elem.text #Pegar o texto do elemento
elem.click()

searchElem = browser.find_element_by_css_selector('.search-field')
searchElem.send_keys('Bruna')
searchElem.submit() #Clicar ok ou dar enter automaticamente

browser.back() #Voltar página
browser.forward() #Ir para frente
browser.refresh() #Atualizar página
browser.quit() #Fechar página

elem = browser.find_element_by_css_selector('html')
elem.text #Pega o texto da página inteira
