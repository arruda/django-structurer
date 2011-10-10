#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os


DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'snippets','default')

DJSTRUCT_HOME = os.environ.get('DJSTRUCT_HOME', None)

class Snippets(object):
    def __init__(self):
        self.snippets = {}
        
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
                key = str(file_path).replace('/','.')
                print key
                snippet = open(file_path,'r')
                self.snippets[key] = snippet.read()
                snippet.close()
                

    def load_snippets(self):
        """Loads all snippets into snippets.
        """
        self._load_snippets(DEFAULT_PATH)
        if DJSTRUCTURER_HOME not None:
            self._load_snippets(DJSTRUCTURER_HOME)


    def dump_snoppets(self):
        """Dump the snippets from the folder to where the user is using the command.
           It actualy copies the default folder(from snippets) into where the user whants.
        """
        pass


