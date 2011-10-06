#!/usr/bin/env python
#-*- coding:utf-8 -*-
#import django
import os

class Abs_Snippets(object):
    def __init__(self,proj_or_app_name):
        self.original_txt = proj_or_app_name

    def find_snippet(self,init_text,final_text, start=None,end=None,put_final=False):
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
        f_path = os.path.join(os.path.dirname(__file__), 'project_template', 'settings.py')
        self.original_txt = open(f_path,'r').read()
        self.original_txt = self.original_txt.replace('{{ project_name }}', project_name)

    @property
    def db(self):
        """Database snippet.
        """
        init="DATABASES"
        end = "# Local time zone"
        return self.find_snippet(init,end)

    @property
    def general_conf(self):
        """General configurations snippet, like language, site_id, timezone and etc.
        """
        init="# Local time zone"
        end = "# Absolute"
        return  self.find_snippet(init,end)

    @property
    def installed_apps(self):
        """Installed apps snippet.
        """
        init="INSTALLED_APPS"
        end = ")"
        return self.find_snippet(init,end,None,None,True)

    @property
    def logging(self):
        """Installed apps snippet.
        """
        init="# A sample logging configuration."
        end = """},
    }
}"""
        return self.find_snippet(init,end,None,None,True)

class Manage_snippets(Abs_Snippets):
    """Deals with all the manage snippets.
    """
    def __init__(self,project_name):
        super(Manage_snippets,self).__init__(project_name)
        f_path = os.path.join(os.path.dirname(__file__), 'project_template', 'manage.py')
        self.original_txt = open(f_path,'r').read()


class App_snippets(Abs_Snippets):
    """Deals with all the apps snippets.
    """
    def __init__(self,proj_or_app_name):
        super(App_snippets,self).__init__(proj_or_app_name)

    @property
    def sub_init(self):
        """Snippet for the __init__.py file for the inside folders of a app.
        """
        f_path = os.path.join(os.path.dirname(__file__), 'app_template', 'app_sub_init.py')
        snippet = open(f_path,'r').read()
        snippet = snippet.replace('{{ app_name }}', app_name)
        return snippet

class Urls_snippets(Abs_Snippets):
    """Deals with all the Urls snippets.
    """
    def __init__(self,proj_or_app_name):
        super(Urls_snippets,self).__init__(proj_or_app_name)
        f_path = os.path.join(os.path.dirname(__file__),  'project_template', 'urls.py')
        self.original_txt = open(f_path,'r').read()
        self.original_txt = self.original_txt.replace('{{ project_name }}', proj_or_app_name)




