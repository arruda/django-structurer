#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os
import yaml
from snippets_readers import Snippets

import sys

snpt = Snippets()

def make_project_structure(archive,root, project_name):
    if archive['name'] == "$project_name":
        archive['name'] = project_name

    archive_path = os.path.join(root,archive['name'])

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


