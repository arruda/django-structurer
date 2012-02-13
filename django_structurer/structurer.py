#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os, stat
import yaml
from snippets_readers import Snippets

import sys

snpt = Snippets()
MANAGE_FILE_FOLDER=None
APP_FOLDER=None

def make_exec(path):
    "make a file executable"
    mode = os.stat(path).st_mode
    mode_add = stat.S_IXOTH | stat.S_IEXEC | stat.S_IXGRP
    mode = mode + mode_add
    os.chmod(path, mode)

def make_structure(archive,root, name, is_project=True):
    archive['name'] = archive['name'].replace("$project_name",name)

    if is_project == False:
        archive['name'] = archive['name'].replace("$app_name",name)

    archive_path = os.path.join(root,archive['name'])
#    print archive_path

    if archive.get('var', None) == "$create_with_app":
        if is_project:
            change_proj_name(archive,name)
            create_app_struct_file(archive)
            return


    arc_archives = archive.get('archives',None)
    #check if is a folder or a file
    if arc_archives != None:
        os.mkdir(archive_path)   
        for sub_ar in arc_archives: 
            make_structure(sub_ar,archive_path, name, is_project)

    #is a file:
    else:
        archive_file = open(archive_path,'w')
        #inclui os snippets
        arc_snippets = archive.get('snippets',[])        
        for snippet in arc_snippets:
            snippet_dict = snpt.snippets.get(snippet,None)
            if snippet_dict == None:
                continue
            snippet_txt = snippet_dict['txt']
            if snippet_txt != None:
                snippet_txt=snippet_txt.replace('$app_folder',APP_FOLDER)
                archive_file.write(snippet_txt)
    
        archive_file.close()  
        if archive.get('var',None) == '$executable':
            make_exec(archive_path)

def change_proj_name(archive,project_name):
    "Change any $project_name for the project name"
    if archive.get('name',None) is None:
        return
    if archive['name'] == "$project_name":
        archive['name'] = project_name
    
    archives_k = archive.get('archives',None)
    if archives_k != None:
        for k in archives_k:
            change_proj_name(k,project_name)

def create_app_struct_file(archive):
    """Creates a yaml file that contains the info for a given project
    that knows how an app should be.
    """
    #print "app = %s" %APP_FOLDER
    if MANAGE_FILE_FOLDER != None and APP_FOLDER != None:
        app_strucure = os.path.join(MANAGE_FILE_FOLDER,'app_structure.yaml')
        app_strucure = open(app_strucure, "w")
        yaml.dump(archive,app_strucure)
        app_strucure.close()

def get_infos_path(archive,root):
    "get the infos for the global vars of paths"
    archive_path = os.path.join(root,archive['name'])
    if archive.get('var',None) == "$source":
        global MANAGE_FILE_FOLDER
        MANAGE_FILE_FOLDER = archive_path

    if archive.get('var',None) == "$app_folder":
        global APP_FOLDER
        APP_FOLDER = archive_path.replace(MANAGE_FILE_FOLDER,'.')

    arc_archives = archive.get('archives',None)
    #check if is a folder or a file
    if arc_archives != None:
        for sub_ar in arc_archives: 
            get_infos_path(sub_ar,archive_path)
    

def app_starter(app_name,app_folder,yaml_app):
    """
    Creates a new app struture in the folder that the user is in,
    using the yaml file that discribes how it should do it.
    """
    snpt.load_snippets()
    archives = yaml.load(yaml_app)
    global APP_FOLDER
    APP_FOLDER = app_folder
    make_structure(archives,app_folder,app_name,False)

def project_starter(project_name,yaml_project):
    """
    Creates a new Django project struture in the folder that the user is in,
    using the yaml file that discribes how it should do it.
    """
    snpt.load_snippets()
    archives = yaml.load(yaml_project)
    change_proj_name(archives,project_name)
    get_infos_path(archives,"./")
    make_structure(archives,"./",project_name,True)

#    
#if __name__ == "__main__":
#    project_name = sys.argv[1]
#    yaml_project = file(sys.argv[2], 'r')
#    
#    project_starter(project_name, yaml_project)


