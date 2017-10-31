#!/usr/bin/env python
# coding=utf-8 
from utility.cmdline import cmd_parse 

def genpass(): 
    args = cmd_parse()  
    domain = args.domain
    username = args.username

    name = domain[0] if domain else username[0]
    rules = open('./rules/domain_rules.txt') if domain else open('./rules/username_rules.txt')
    pwds = open('{}.txt'.format(name),'w')

    for rule in rules:
        if username:
            pwd = rule.replace('%username%',username[0])
            pwds.write(pwd) 
            pwds.write(pwd.capitalize()) 
        if domain:
            pwd = rule.replace('%domain%',domain[0]) 
            pwds.write(pwd)
            pwds.write(pwd.capitalize()) 


    rules.close()
    pwds.close() 

if __name__=='__main__':
    genpass() 
