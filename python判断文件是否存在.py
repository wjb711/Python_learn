import os
import logging
from datetime import datetime, timedelta
if os.path.exists('./list.ini'):
    pass
else:
    logging.warning('no list.ini file')

date=datetime.now().strftime('%Y-%m-%d_%H%M%S')
yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y%m%d')
#yesterday
print (yesterday)
#############################logging part###############################
#print (date)
#date=%Y%m%d_%H:%M:%S
logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                #datefmt='%a, %d %b %Y %H:%M:%S',
                datefmt='%Y%m%d_%H:%M:%S',
                filename=date+'.log',
                filemode='w')

#################################################################################################
F = open('list.ini','r')
lines = F.read().splitlines()
for line in lines:
    if line.startswith('#'):
        pass
        
     #   logging.info('This is #'+line)
    elif os.system('ping -n 1 -w 1 '+line)==1:
        #return=os.system('ping -n 1 -w 1 '+line)
        #print (line,'1')
        logging.warning(line+' This is not pingable')
    elif os.path.exists('//'+line+'/c$/')==False:
        
        print (line+'can not open folder')
        print(os.path.exists('//'+line+'/c$/'))
        logging.info(line+'can not open folder')
    elif os.path.exists('//'+line+'/c$/GD/logs/'+yesterday+line+'.exe')==False:
        print (line+' no exe file')
    else:
        logging.info(line+' success')
        #logging.info(os.listdir())
#print (lines[3])
#logging.debug('This is debug message')
#logging.info('This is info message')
#logging.warning('This is warning message')
