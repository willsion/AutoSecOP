import os
import sys
import time


def run(conf_dict,debug=False):
    if debug:print conf_dict
    flag=int(conf_dict['system']['repate'])
    interval=int(conf_dict['system']['interval'])
    imax=int(conf_dict['system']['max'])
    exec 'from task.%s import task' %conf_dict['system']['task']
    if flag:
        i=0
        while True:
            print "=========%s=============" %time.asctime()
            task()
            time.sleep(interval)
            i+=1
            if imax>0 and i>=imax:
                break
    else:
        task()
    
    
    