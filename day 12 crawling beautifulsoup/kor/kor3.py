# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

a = '한글'
print a.decode('utf-8')
print unicode(a)

b = u'한글'
print a.encode('utf-8')
print str(a)
