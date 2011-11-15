===================================
Django Structurer
===================================

About:
-----------------------------------

The purpose of this app is to enable some custom script for manage.py and for django-admin.py(maybe?) that creates a different folder structure for Django.
This structure what I thought of a good one for projects that I'm working, and that possibly you are working too.



Usage:
-----------------------------------
For now you can use the command that lets you create a new project using the default structure
or your own custom structure.
You can run the command to create a new project::

    djstruct.py proj projectName custom_structure
And this will create the basic project layout.


You can also run the file created with the last command to make a new
app with the custom structure::
    python app_starter.py myNewApp

And this will create the basic app layout.

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



Install:
-----------------------------------
pip install django_structurer


License:
-----------------------------------
This software is distributed using MIT license, see LICENSE file for more details.
