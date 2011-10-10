#!/usr/bin/python
#-*- coding:utf-8 -*-
import sys
import os
import django_structurer
from django_structurer.structurer import project_starter

if __name__ == "__main__":
    project_name = sys.argv[1]
    try:
        yaml_project = file(sys.argv[2], 'r')
    except:
        default_proj = os.path.join(django_structurer.__path__[0], 'default_structure.yaml')
        yaml_project = file(default_proj,'r')

    project_starter(project_name, yaml_project)
