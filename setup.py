import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

structurer_dir = 'django_structurer'
data_folder= os.path.join(structurer_dir,'snippets')
data_files = []

for dirpath, dirnames, filenames in os.walk(data_folder):
    data_files.append([dirpath, [os.path.join(dirpath, f) for f in filenames]])


setup(
    name = "django_structurer",
    version = "0.1.3",
    author = "Felipe Arruda Pontes",
    author_email = "contato@arruda.blog.br",
    description = ("This app allow you to create your own custom django project structure, and then use it as you please."),
    license = "MIT",
    keywords = "django project structure",
    url = "https://github.com/arruda/django-structurer",
    packages=['django_structurer'],
    scripts = ['django_structurer/bin/djstruct.py'],
    data_files = data_files,
    install_requires=[
        'PyYAML==3.09'
    ],
    long_description="""The purpose of this app is to enable some custom script for manage.py and for django-admin.py(maybe?) that creates a different folder structure for Django.
This structure what I thought of a good one for projects that I'm working, and that possibly you are working too.""",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)
