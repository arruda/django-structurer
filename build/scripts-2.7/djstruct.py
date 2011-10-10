#!/home/arruda/.virtualenvs/django_structurer/bin/python
#-*- coding:utf-8 -*-
import sys
import os
import django_structurer
from django_structurer.structurer import project_starter
from django_structurer.snippets_readers import CUSTOM_SNIPPETS

DEFAULT_PROJECT = os.path.join(django_structurer.__path__[0], 'default_structure.yaml')

def check_file(file_name, path):
    try:        
        file_path = os.path.join(path,file_name)
        yaml_file = file(file_path, 'r')
        return yaml_file
    except:
        return None

def tries_different_paths_for_file(file_name):    
    yaml_file = check_file(file_name, "./")
    if yaml_file == None:            
        yaml_file = check_file(file_name, CUSTOM_SNIPPETS)
        if yaml_file == None:
            yaml_file = file(DEFAULT_PROJECT,'r')

    return yaml_file

if __name__ == "__main__":
    project_name = sys.argv[1]
    yaml_project = DEFAULT_PROJECT
    try:        
        yaml_project = sys.argv[2]
    except IndexError:
        pass    

    yaml_file = tries_different_paths_for_file(yaml_project)
    project_starter(project_name, yaml_file)

