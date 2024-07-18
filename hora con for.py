import time
import datetime
from datetime import datetime

hora = datetime.now()
current_time = hora.strftime('%H:%M:%S')
hora1 = int(hora.strftime('%H'))
minuto = int(hora.strftime('%M'))
segundo = int(hora.strftime('%S'))

for h in range(hora1,24,1):
    for m in range(minuto,60,1):
        for s in range(segundo,60,1):
            print(h, m, s)
            time.sleep(1)