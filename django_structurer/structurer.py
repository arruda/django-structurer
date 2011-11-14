#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os
import yaml
from snippets_readers import Snippets

import sys

snpt = Snippets()
manage_file_folder=None
app_folder=None

def make_structure(archive,root, name, is_project=True):
    if archive['name'] == "$project_name" or archive['name'] == "$app_name":
        archive['name'] = name

    archive_path = os.path.join(root,archive['name'])

    if archive['var'] is '$source':
        manage_file_folder=archive_path

    if archive['var'] == "$create_with_app":
        app_folder=archive_path
        if is_project:
            change_proj_name(archive,name)
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
     
def change_proj_name(archive,project_name):
    "Change any $project_name for the project name"
    if archive.get('name',None) is None:
        return
    if archive['name'] == "$project_name":
        archive['name'] = project_name
    change_proj_name(archive['archives'],project_name)

def create_app_struct_file(archive):
    """Creates a yaml file that contains the info for a given project
    that knows how an app should be.
    """
    if manage_file_folder != None and app_folder != None:
        app_strucure = os.path.join(manage_file_folder,'app_structure.yaml')
        app_strucure = open(app_strucure, "w")
        yaml.dump(archive,app_strucure)
        app_strucure.close()


#def find_app_folder(archive,root):
#    """Returns the dict that represents the app_folder
#    passing the original archive and root dir
#    """    
#    if archive['name'] == "$project_name" or archive['name'] == "$app_name":
#        archive['name'] = name

#    archive_path = os.path.join(root,archive['name'])
#    if archive.get('var', None) == '$create_with_app':
#        return archive, archive_path

#    for sub_ar in archive.get('archives',None):
#        dct,path = find_app_folder(sub_ar,archive_path)
#        if dct and path !=None
#            return dct,path

#    return None

def app_starter(app_name,yaml_app):
    """
    Creates a new app struture in the folder that the user is in,
    using the yaml file that discribes how it should do it.
    """
    snpt.load_snippets()
    archives = yaml.load(yaml_app)
    find_app_folder(archives,"./")
    make_project_structure(archives,"./",app_name,False)

def project_starter(project_name,yaml_project):
    """
    Creates a new Django project struture in the folder that the user is in,
    using the yaml file that discribes how it should do it.
    """
    snpt.load_snippets()
    archives = yaml.load(yaml_project)
    make_structure(archives,"./",project_name,True)

#    
#if __name__ == "__main__":
#    project_name = sys.argv[1]
#    yaml_project = file(sys.argv[2], 'r')
#    
#    project_starter(project_name, yaml_project)


