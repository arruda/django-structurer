#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
"""
import django
import os

class Config_Snippets(object):
    def __init__(original_txt, project_name):
        self.original_txt = 
            original_txt.replace('{{ project_name }}', project_name)

    def find_snippet(init_text,final_text, start=None,end=None,put_final=False):
        """Returns a snippet from the original_txt that start with the
            init_text and ends with right beforze final_text.
            this search is done from the start(default to 0)
            to the end(deafult to the end of the file)

            returns None if the string wasn't found.
        """
        i = self.original_txt.find(init_text,start,end)
        if i == -1:
            return None
        j = self.original_txt.find(final_text,i,end)
        if put_final and j != -1:
            j+= final_text.__len__()

        return self.original_txt[i:j] if (j and i is not -1) else None

class settings_snippets(Config_Snippets):
    """Deals with all the settings snippets.
    """
    def db_snippet(self):
        """Database snippet.
        """
        init="DATABASES"
        end = "# Local time zone"
        return snippet = self.find_snippet(init,end)

    def installed_apps_snippet(self):
        """Installed apps snippet.
        """
        init="INSTALLED_APPS"
        end = ")"
        return snippet = self.find_snippet(init,end,None,None,True)

