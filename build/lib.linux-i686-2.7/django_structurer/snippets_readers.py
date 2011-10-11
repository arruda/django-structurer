#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os

SNIPPETS_TERM = ".snippets"
SNIPPETS_FOLDER = "snippets"
DEFAULT_PATH = os.path.join(SNIPPETS_FOLDER,'default')
#DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'snippets','default')

DJSTRUCT_HOME = os.environ.get('DJSTRUCT_HOME', None)
CUSTOM_SNIPPETS = None
if DJSTRUCT_HOME != None:
    CUSTOM_SNIPPETS=os.path.join(DJSTRUCT_HOME,SNIPPETS_FOLDER)

class Snippets(object):
    def __init__(self):
        self.snippets = {}

    @classmethod
    def mount_key(cls,full_path,file_path):
        """Generates a key for a snippet by removing the first part of full_path that contains
        the string 'snippets.' from the path.
        EX:
        The file: snippets/default/others/headers.snippets you have a key:
        'default.others.headers'
        """
        snpt_path_fix = os.path.join(SNIPPETS_FOLDER, "")
        init = full_path.find(snpt_path_fix)+snpt_path_fix.__len__()      
        alter_file_path = file_path.replace(SNIPPETS_TERM,"")  
        alter_path = os.path.join(full_path,alter_file_path).replace(full_path[:init],"")
        key = alter_path.replace("/",".")
        return key

    def _load_snippets(self,folder=DEFAULT_PATH):
        """Load snippets from the default snippets folder.
        """
        full_path = os.path.join(os.path.dirname(__file__), folder)
        for d, subdirs, files in os.walk(full_path):             
            for f in files:
                if not f.endswith(SNIPPETS_TERM):
                    # Ignore .pyc, .pyo, .py.class etc, as they cause various
                    # breakages.
                    continue
                                
                file_path = os.path.join(d, f)   
                key = Snippets.mount_key(d,f)             
                print key
                snpt_dict = {'file':file_path, 'txt': None}
                snippet = open(file_path,'r')
                self.snippets[key]['txt'] = snippet.read()
                snippet.close()
                

    def load_snippets(self):
        """Loads all snippets into snippets.
        """
        self._load_snippets(DEFAULT_PATH)
        if DJSTRUCT_HOME != None:
            self._load_snippets(DJSTRUCT_HOME)


    def dump_snippets(self,destination="./"):
        """Dump the snippets from the user folder, and the default(if True) 
           to where the user is using the command.
           It actualy copies the default folder(from snippets) into where the user whants.
        """
        self.load_snippets()
        for key in self.snippets:
            old_path = self.snippets[key]['file']
            print old_path
