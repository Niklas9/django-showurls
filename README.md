# django-showurls

[![Build status](https://travis-ci.org/Niklas9/django-showurls.svg?branch=master)](https://travis-ci.org/Niklas9/django-showurls)
[![Latest version](https://img.shields.io/pypi/v/django-showurls.svg?style=flat)](https://pypi.python.org/pypi/django-showurls/)
[![Downloads](https://img.shields.io/pypi/dm/django-showurls.svg?style=flat)](https://pypi.python.org/pypi/django-showurls/)


Adds a new management command that outputs all configured urls to your Django
project.

This is equivalent to Ruby on Rails command "rake routes", which I have found
quite useful lately.

## Usage
First you'll need to add the django_showurls app in your Django project's
settings.py file:

    ..
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'showurls',
    ]
    ..

After that you should be able to get an overview of all the urls in your project
by calling the showurls management command from your manage.py:

    ./manage.py showurls
     ^admin/
        ^$
           ^login/$
              ^logout/$
    ..

## Installation
Install with pip (or easy_install)::

    pip install django-showurls

## License

BSD, just as the main Django project. See LICENSE file in root of this repo.

## Contributing

This project accepts contributions via GitHub pull requests.

* follow Google's Python style guide
  https://google-styleguide.googlecode.com/svn/trunk/pyguide.html 
* make commits of logical units, messages should include what changed and why
  and be written in past tense
