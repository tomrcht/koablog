#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime

TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'fr'
COPYRIGHT_YEAR = datetime.now().year

AUTHOR = 'Tom Rochat'
SITEURL = 'http://localhost:8000'
SITELOGO = '/assets/logo.jpg'
FAVICON = '/assets/favicon.ico'

SITENAME = 'Koablog'
SITETITLE = 'Koablog'
SITESUBTITLE = 'Kind of a blog'
SITEDESCRIPTION = 'Kind of a blog about programming and stuff'
ROBOTS = 'index, follow'

BROWSER_COLOR = '#ff4049'
PYGMENTS_STYLE = 'monokai'

THEME = 'Flex'

PATH = 'content'
OUTPUT_PATH = 'output/'
DEFAULT_PAGINATION = 10

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

SOCIAL = (
  ('github', 'https://github.com/tomrcht'),
  ('stack-overflow', 'https://stackoverflow.com/users/8370553/tomrcht'),
  ('linkedin', 'https://www.linkedin.com/in/tom-rochat/'),
)

MENUITEMS = (
  ('Archives', '/archives.html'),
  ('Categories', '/categories.html'),
  ('Tags', '/tags.html'),
)

# CC_LICENSE = {
#     'name': 'Creative Commons Attribution-ShareAlike',
#     'version': '4.0',
#     'slug': 'by-sa'
# }

# THEME_COLOR = '#ff4049'
# THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
# THEME_COLOR_ENABLE_USER_OVERRIDE = True

USE_LESS = True

STATIC_PATHS = [ 'assets' ] # 'extra/ads.txt'
# EXTRA_PATH_METADATA = {'extra/ads.txt': {'path': 'ads.txt'},}

# # Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# # Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
