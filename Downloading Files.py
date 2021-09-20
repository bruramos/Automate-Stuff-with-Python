import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

res.status_code

len(res.text)
print(res.text[:10])

res.raise_for_status() #Verificar status e retornar erro

playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)


playFile.close()

