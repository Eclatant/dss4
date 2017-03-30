# -*- coding: utf-8 -*-

import threading
import time

def work():
    i = 0
    while i < 10:
        print 'I am working..'
        time.sleep(0.5)
        i += 1

t = threading.Thread(target=work)
# Daemon 설정
#t.setDaemon(True) 
t.daemon = True # 혹인 이렇게도 가능
t.start()

print 'main thread finished'
