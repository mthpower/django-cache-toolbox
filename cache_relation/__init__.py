"""
:mod:`cache_relation` --- Toolbox of caching tools for Django
=============================================================

Introduction
------------

``cache_relation`` is intended to be a lightweight series of independent tools
to leverage caching within Django projects.

The tools are deliberately `non-magical`. That is to say, instances are never
retrieved from caches behind your back and regular Django ``.filter()`` /
``.get()`` queries continue to work exactly as before.

Because of this, you can introduce ``cache_relation`` into your project slowly
when needed rather than "switching" to it with invasive changes.

Links
-----

View/download code
  https://github.com/playfire/django-cache-relation

File a bug
  https://github.com/playfire/django-cache-relation/issues
"""

from .model import cache_model
from .relation import cache_relation
