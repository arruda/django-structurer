import os
from distutils.core import setup

structurer_dir = 'django_structurer'
data_folder= os.path.join(structurer_dir,'data')
data_files = []

def helper_package_data(pkg,folder):
    data = {pkg : []}
    size = pkg.__len__() + 1
    for dirpath, dirnames, filenames in os.walk(os.path.join(pkg,folder)):
        temp = os.path.join(dirpath,"*.*")
        data[pkg].append(temp[size:])

#    print data
    return data

for dirpath, dirnames, filenames in os.walk(data_folder):
    data_files.append([dirpath, [os.path.join(dirpath, f) for f in filenames]])


setup(
    name = "django_structurer",
    version = "0.3.0",
    author = "Felipe Arruda Pontes",
    author_email = "contato@arruda.blog.br",
    description = ("This app allow you to create your own custom django project structure, and then use it as you please."),
    license = "MIT",
    keywords = "django project structure",
    url = "https://github.com/arruda/django-structurer",
    packages=['django_structurer'],
    scripts = ['bin/djstruct.py'],
    package_data=helper_package_data('django_structurer','data'),
    long_description="""The purpose of this app is to enable some custom script for manage.py and for django-admin.py(maybe?) that creates a different folder structure for Django.
This structure what I thought of a good one for projects that I'm working, and that possibly you are working too.""",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=[
        'PyYAML==3.09'
    ],
)
