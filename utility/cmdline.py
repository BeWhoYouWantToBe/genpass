#!/usr/bin/env python
# coding=utf-8
import argparse  
import pdb

def cmd_parse():
    parser = argparse.ArgumentParser(description='User information') 

    parser.add_argument('-u','--username',dest='username',action='store',
                       help='username of target,English only',nargs='*',default=[])
    parser.add_argument('-d','--domain',dest='domain',action='store',
                       help='domain of target',nargs='*',default=[]) 

    args = parser.parse_args() 
    if not any(args.__dict__.values()):
        parser.print_help() 
        raise SystemExit 

    return args 


if __name__=='__main__':
    pdb.set_trace() 
    args = cmd_parse() 
    print(args)
