#coding=utf8
import sys
import os
from lib.lib_config import *
from core import run


if __name__=="__main__":
    
    parser=getoptions()
    parser.add_option('-t','--task',dest='taskscript',help="assign task script")
    parser.add_option('-r','--repate',dest='repate',help="repate the task yes/no")
    parser.add_option('-i','--interval',dest='interval',help="interval for the repate")
    
    (options, args) = parser.parse_args()
    
    config=read_conf(sys.path[0]+'/conf/AutoSecOP.conf')
    confdict=config.get_conf_dict()
    
    if options.taskscript:
        confdict['system']['task']=options.taskscript
    if options.repate:
        confdict['system']['repate']=options.repate
    if options.interval:
        confdict['system']['interval']=options.interval
 
    if not confdict['system']['task']:
        print "Please input vaild task script from AutoSecOP.conf or runtime_paras"
        exit()
        
    run(confdict,int(confdict['system']['debug']))

    
