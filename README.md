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

   a. edit the applications __init__.py file

   b. insert something like :

        from django_block_manager.lib.manager import BlockManager

        blockmanager = BlockManager()
        blockmanager.add_block('YourBlockName', {
            'title' : 'SectionName',
            'content' : rendered_content_func,
        })

   c. notes :
      i. rendered_content_func : is a function which returns data to be inserted
           into template output, so if you need it to be html, then it's up to you
           to ensure it's safe.

      i. SectionName : By default this will be rendered inside a H2 tag,
           provide a template to override this.

      i. YourBlockName : This is how you call a block, which contains many bits of
           content. Requesting specific parts of a block is my next step to implement.

   d. In your template :

        {% blockmanager YourBlockName [SectionName] %}

   e. Provide the block override template

      i. in you template directory create :

            ...
            blockmanager +
                         +- block.html
            ...
      i. Fill block.html with

            <h1>{{ Title }}</h1>
            <p>{{ Content }}</p>


## Legal

### django_block_manager/*

+ Copyright (c) 2011 Zenobius Jiricek
+ Licensed under the MIT license: http://www.opensource.org/licenses/mit-license.php

### Trademarks

Django and the Django logo are registered trademarks of Django Software Foundation.
http://www.djangoproject.com/contact/foundation/

