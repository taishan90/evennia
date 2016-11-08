# -*- coding:utf-8 -*-  

import sys
import inspect
from datetime import *
#from evennia.utils import logger
from twisted.python import log

def zkprint (text):
    print (str(datetime.now()))
    call_func=sys._getframe().f_back
    
    print (call_func.f_code.co_filename)

    print( call_func.f_code.co_name)
    print( call_func.f_lineno)
    print(text)
    #zklog.get_cur_info(target)
