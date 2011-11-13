#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os
import yaml
from snippets_readers import Snippets

import sys

snpt = Snippets()
manage_file_folder=''

def make_structure(archive,root, name, is_project=True):
    if archive['name'] == "$project_name" or archive['name'] == "$app_name":
        archive['name'] = name

    archive_path = os.path.join(root,archive['name'])

    if archive['var'] is '$source':
        manage_file_folder=archive_path

    if archive['var'] == "$create_with_app" and is_project:
        create_app_struct_file(archive)
        return


    arc_archives = archive.get('archives',None)
    #check if is a folder or a file
    if arc_archives != None:
        os.mkdir(archive_path)   
        for sub_ar in arc_archives: 
            make_project_structure(sub_ar,archive_path, project_name)

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
                archive_file.write(snippet_txt)
    
        archive_file.close()       

def find_app_folder(archive,root):
    """Returns the dict that represents the app_folder
    passing the original archive and root dir
    """    
    if archive['name'] == "$project_name" or archive['name'] == "$app_name":
        archive['name'] = name

    archive_path = os.path.join(root,archive['name'])
    if archive.get('var', None) == '$create_with_app':
        return archive, archive_path

    for sub_ar in archive.get('archives',None):
        dct,path = find_app_folder(sub_ar,archive_path)
        if dct and path !=None
            return dct,path

    return None

def app_starter(app_name,yaml_app):
    """
    Creates a new app struture in the folder that the user is in,
    using the yaml file that discribes how it should do it.
    """
    snpt.load_snippets()
    archives = yaml.load(yaml_project)
    find_app_folder(archives,)
    make_project_structure(archives,"./",project_name)

def project_starter(project_name,yaml_project):
    """
    Creates a new Django project struture in the folder that the user is in,
    using the yaml file that discribes how it should do it.
    """
    snpt.load_snippets()
    archives = yaml.load(yaml_project)
    make_project_structure(archives,"./",project_name)

#    
#if __name__ == "__main__":
#    project_name = sys.argv[1]
#    yaml_project = file(sys.argv[2], 'r')
#    
#    project_starter(project_name, yaml_project)


