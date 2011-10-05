#!/usr/bin/python
#-*- coding:utf-8 -*-
from django_structurer.structurer import project_starter

if __name__ == "__main__":
    project_name = sys.argv[1]
    yaml_project = file(sys.argv[2], 'r')
    
    project_starter(project_name, yaml_project)
