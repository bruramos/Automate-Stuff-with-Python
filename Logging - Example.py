import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

#Para salvar os logs em uma pasta
#logging.basicConfig(filename='logs.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


#logging.disable(logging.CRITICAL) #para desabilitar logs

logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial (%s)' %(n))
    total = 1
    for i in range(1, n+1):
        total *= i
        logging.debug('i is %s, total is %s' %(i, total))

    logging.debug('Return value is %s' %(total))
    return total

print(factorial(5))

logging.debug('End of program')


#Tipos de Logs:
#logging.debug()
#logging.info()
#logging.warning()
#logging.error()
#logging.critical()
