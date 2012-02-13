#!/usr/bin/env python
#-*- coding:utf-8 -*-
import sys
import os
import django_structurer
from django_structurer.structurer import project_starter
from django_structurer.snippets_readers import DJSTRUCT_HOME, DATA_FOLDER, Snippets

DEFAULT_PROJECT = os.environ.get('DJSTRUCT_DEFAULT', os.path.join(DATA_FOLDER, 'default_structure.yaml'))

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
        yaml_file = check_file(file_name, DJSTRUCT_HOME)
        if yaml_file == None:
            yaml_file = file(DEFAULT_PROJECT,'r')

    return yaml_file

if __name__ == "__main__":
    command = sys.argv[1]
    if command == "proj":
        project_name = sys.argv[2]
        yaml_project = DEFAULT_PROJECT
        try:        
            yaml_project = sys.argv[3]
        except IndexError:
            pass    

        yaml_file = tries_different_paths_for_file(yaml_project)
        project_starter(project_name, yaml_file)
        print "Project %s FTW!" % project_name
    elif command == "dumpsnippets":
        snpt = Snippets()
        snpt.dump_snippets()

