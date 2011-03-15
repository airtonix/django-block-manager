Django Block Manager
=========================

This application allows me to have any other application describe what views
it wants to expose to the block manager, which in turn allows me to use those
in any template as a callable template tag.

It might not be pretty, or fast, but it achieved what I wanted.

## Installation

1. You need to have python-setuptools installed
`sudo apt-get install python-setuptools`

1. `python ./setup.py install`

1. Include it in your INSTALLED_APPS tuple

1. For each application that you want to create "blocks" for :

 a. edit the __init__.py

 b. insert something like :

    from django_block_manager.lib.manager import BlockManager

    content_func = view_function

    blockmanager = BlockManager()
    blockmanager.add_block('virtualhost-link-list', {
        'title' : 'Virtualhosts',
        'content' : content_func,
    })


 c.

## Legal

### django_block_manager/*

+ Copyright (c) 2011 Zenobius Jiricek
+ Licensed under the MIT license: http://www.opensource.org/licenses/mit-license.php

### Trademarks

Django and the Django logo are registered trademarks of Django Software Foundation.
http://www.djangoproject.com/contact/foundation/

