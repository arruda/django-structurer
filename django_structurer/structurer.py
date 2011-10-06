#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os
import sys
import yaml
from snippets_readers import Settings_snippets, Manage_snippets, App_snippets, Urls_snippets

default_dict = {
'name':"$project_name", 'archives':[
            {'name':"$project_name", 'archives':[
                {'name':"apps", 'archives':[],'folder':True},
                {'name':"media", 'archives':[],'folder':True},
                {'name':"static", 'archives':[
                    {'name':"js", 'archives':[],'folder':True},
                    {'name':"css", 'archives':[],'folder':True},
                    {'name':"images", 'archives':[],'folder':True},
                    ],'folder':True},

                {'name':"settings", 'archives':[
                    {'name':"apps.py", 'archives':[],'folder':False},
                    {'name':"config.py", 'archives':[],'folder':False},
                    {'name':"env_dev.py", 'archives':[],'folder':False},
                    {'name':"env_prod.py", 'archives':[],'folder':False},
                    ],'folder':True},

                {'name':"templates", 'archives':[],'folder':True},
                {'name':"scripts", 'archives':[],'folder':True},
                {'name':"libs", 'archives':[],'folder':True},

                ],'folder':True},
            {'name':"docs", 'archives':[],'folder':True},
            {'name':"etc", 'archives':[
                {'name':"requirements.txt", 'archives':[],'folder':False},
                ],'folder':True},
          ],'folder':True }

def make_project_structure(archive,root, project_name):
    if archive['name'] == "$project_name":
        archive['name'] = project_name

    archive_path = os.path.join(root,archive['name'])
    if archive['folder'] is True:        
        os.mkdir(archive_path)   
        arc_archives = archive.get('archives',[])
        for sub_ar in arc_archives: 
            make_project_structure(sub_ar,archive_path, project_name)

    #is a file:
    else:
        archive_file = open(archive_path,'w')
        #inclui os snippets
        arc_snippets = archive.get('snippets',[])
        for snippet in arc_snippets:
            #get the snippet type and name: like settings.att     
            #write this snippet in the file(lookout for ordering in arc_snippets)  
            prefix = snippet.split('.')[0]
            posfix = snippet.split('.')[1]
            #get the class for the snippet
            snippet_class = eval(prefix+'_snippets')

            proj_or_app_name = ""
            if prefix == "Settings":
                proj_or_app_name = project_name

            if prefix == "App":
                proj_or_app_name = project_name
 
            snippet_txt = getattr(snippet_class(proj_or_app_name),posfix)
            archive_file.write(snippet_txt+"\n")          
     
        archive_file.close()       
    
def project_starter(project_name,yaml_project):
    """
    Creates a new Django project struture in the folder that the user is in,
    using the yaml file that discribes how it should do it.
    """
    archives = yaml.load(yaml_project)
    make_project_structure(archives,"./",project_name)

#if __name__ == "__main__":
#    project_name = sys.argv[1]
#    yaml_project = file(sys.argv[2], 'r')
#    
#    project_starter(project_name, yaml_project)


