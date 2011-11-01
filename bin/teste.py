#!/home/arruda/.virtualenvs/django_structurer/bin/python
#-*- coding:utf-8 -*-

from django_structurer.snippets_readers import DATA_FOLDER, DEFAULT_PATH, CUSTOM_SNIPPETS
#import os
#DATA_FOLDER =""
#try:
#    import pkgutil
#    DATA_FOLDER = pkgutil.get_data("django_structurer", 'data','default_structure.yaml').__path__[0]
#    DATA_FOLDER = os.path.dirname(DATA_FOLDER)
#except ImportError:
#    import pkg_resources
#    DATA_FOLDER = pkg_resources.resource_string("django_structurer", 'default_structure.yaml').__path__[0]
#    DATA_FOLDER = os.path.dirname(DATA_FOLDER)

print DATA_FOLDER
print DEFAULT_PATH
print CUSTOM_SNIPPETS
