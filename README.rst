===================================
Django Arpon Struct
===================================

About:
-----------------------------------

The purpose of this app is to enable some custom script for manage.py and for django-admin.py(maybe?) that creates a different folder structure for Django.
This structure what I thought of a good one for projects that I'm working, and that possibly you are working too.



Usage:
-----------------------------------
For now you can use the command that lets you create a new project using the default structure
or your own custom structure.
You can run the command::

    djstruct.py proj projectName custom_structure
And this will create the basic project layout.

You can make your own custom project structure using the default structure file as a base.
Since its a simple yaml file, it will be very easy for you to do it.

Env Vars:
-----------------------------------
To get the maximum usage from this app, you should set this vars in your system:
export DJSTRUCT_HOME=/some/where/my_djstruct
export DJSTRUCT_DEFAULT=/some/where/my_djstruct/most_used_struct.yaml

If the DJSTRUCT_HOME is set you can have custom settings like new snippets and custom structures.
And if you use the same custom structure over and over, you can just set the DJSTRUCT_DEFAULT
to this file so it will use it as the default.


TODO:
-----------------------------------
You can also use the new manage.py command::

    ./manage.py arpon_app appName
To create a new app using the sugested layout.

Install:
-----------------------------------
pip install -e git+https://github.com/arruda/django-structurer.git#egg=django_structurer


License:
-----------------------------------
This software is distributed using MIT license, see LICENSE file for more details.
