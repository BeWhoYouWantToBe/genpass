#!/usr/bin/env python
# coding=utf-8 
from utility.cmdline import cmd_parse 

def genpass(): 
    args = cmd_parse()  
    domain = args.domain
    username = args.username

    rules = open('./rules/rules.txt')
    name = domain[0] if domain else username[0]
    pwds = open('{}.txt'.format(name),'w')

    for rule in rules:
        if username:
            pwd = rule.replace('%name%',username[0])
            pwds.write(pwd) 
            pwds.write(pwd.capitalize())
        if domain:
            pwd = rule.replace('%name%',domain[0]) 
            pwds.write(pwd)
            pwds.write(pwd.capitalize()) 


    rules.close()
    pwds.close() 

if __name__=='__main__':
    genpass() 
