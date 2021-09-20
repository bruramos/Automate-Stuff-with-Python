import smtplib

conn = smtplib.SMTP('smtp.gmail.com', 587)
conn.ehlo()
conn.starttls()
conn.login('xxx@gmail.com', 'xxxxxx')

conn.sendmail('brunarsousa@gmail.com', 'brunarsousa@gmail.com', 'Subject: So long... \n\nDear Bruna, \nSo long, and thanks for all the fish. \n\n-Bruna')

conn.quit()
