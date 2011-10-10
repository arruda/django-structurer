#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os

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
        """
        snpt_path_fix = os.path.join(SNIPPETS_FOLDER, "")
        init = full_path.find(snpt_path_fix)+snpt_path_fix.__len__()        
        alter_path = os.path.join(full_path,file_path).replace(full_path[:init],"")
        key = alter_path.replace("/",".")
        return key

    def _load_snippets(self,folder=DEFAULT_PATH):
        """Load snippets from the default snippets folder.
        """
        for d, subdirs, files in os.walk(folder):             
            for f in files:
                if not f.endswith('.snippets'):
                    # Ignore .pyc, .pyo, .py.class etc, as they cause various
                    # breakages.
                    continue
                                
                file_path = os.path.join(d, f)   
                key = Snippets.mount_key(d,f)             
                print key
                snippet = open(file_path,'r')
                self.snippets[key] = snippet.read()
                snippet.close()
                

    def load_snippets(self):
        """Loads all snippets into snippets.
        """
        self._load_snippets(DEFAULT_PATH)
        if DJSTRUCT_HOME != None:
            self._load_snippets(DJSTRUCT_HOME)


    def dump_snoppets(self):
        """Dump the snippets from the folder to where the user is using the command.
           It actualy copies the default folder(from snippets) into where the user whants.
        """
        pass


