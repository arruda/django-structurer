#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
"""
import django
import os

class Abs_Snippets(object):
    def __init__(self,proj_or_app_name):
        self.original_txt = proj_or_app_name

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

class Settings_snippets(Abs_Snippets):
    """Deals with all the settings snippets.
    """
    def __init__(self,project_name):
        super(Settings_snippets,self).__init__(project_name)
        self.original_txt = /
            open(os.path.join(django.__path__[0], 'conf', 'project_template', 'settings.py'),'r').read()

        self.original_txt = 
            original_txt.replace('{{ project_name }}', project_name)
    @property
    def db_snippet(self):
        """Database snippet.
        """
        init="DATABASES"
        end = "# Local time zone"
        return snippet = self.find_snippet(init,end)
    @property
    def general_conf_snippet(self):
        """General configurations snippet, like language, site_id, timezone and etc.
        """
        init="# Local time zone"
        end = "# Absolute"
        return snippet = self.find_snippet(init,end)
    @property
    def installed_apps_snippet(self):
        """Installed apps snippet.
        """
        init="INSTALLED_APPS"
        end = ")"
        return snippet = self.find_snippet(init,end,None,None,True)
    @property
    def logging_snippet(self):
        """Installed apps snippet.
        """
        init="# A sample logging configuration."
        end = """},
    }
}"""
        return snippet = self.find_snippet(init,end,None,None,True)

class Manage_snippets(Config_Snippets):
    """Deals with all the manage snippets.
    """
    def __init__(self,project_name):
        super(Manage_snippets,self).__init__(project_name)
        self.original_txt = /
            open(os.path.join(django.__path__[0], 'conf', 'project_template', 'manage.py'),'r').read()


class Init_snippets(Config_Snippets):
    """Deals with all the __init__.py for folder snippets.
    """
    def __init__(self,proj_or_app_name):
        super(Init_snippets,self).__init__(proj_or_app_name)

    @property
    def app_sub_snippets(self):
        """Snippet for the __init__.py file for the inside folders of a app.
        """
        self.original_txt = /
            open(os.path.join(os.path.dirname(__file__), 'app_template', 'app_sub_init.py'),'r').read()
        self.original_txt = 
            original_txt.replace('{{ app_name }}', app_name)


