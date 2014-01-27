#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals
import os


SITENAME = u"Jan's Blog"
SITESUBTITLE = u'Test Site-Subtitle'
AUTHOR = u'Jan Hendrik Metzen'
TAGLINE = u''
SITEURL = 'http://localhost:8000'
FEED_DOMAIN = SITEURL
#FEED_ATOM = 'feeds/all.atom.xml'
FEED_RSS = 'feeds/all.rss'
TIMEZONE = 'Europe/Berlin'
DEFAULT_LANG = u'en'
DATE_FORMATS = {
    'en': '%Y-%m-%d',
}

DEFAULT_PAGINATION = 5

THEME = 'themes/pelican-octopress'


# display items
MENUITEMS = (
    ('Archives', '/archives.html'),
    ('Home Page', 'http://www.informatik.uni-bremen.de/~jhm/')
)
DISPLAY_PAGES_ON_MENU = False
FOOTER_MESSAGE = u'This work is licensed under the <a href="http://creativecommons.org/licenses/by-sa/3.0/" rel="license">CC BY-SA</a>.'

#STATIC_PATHS = ()
FILES_TO_COPY = (
    ('extra/README', 'README'),
    ('extra/LICENSE', 'LICENSE'),
    ('extra/humans.txt', 'humans.txt'),
    ('extra/favicon.ico', 'favicon.ico'),
    ('extra/404.html', '404.html'),
)

# Plugins and their settings.
PLUGIN_PATH = 'pelican-plugins'
PLUGINS = [#'summary', #'sitemap',
           'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.include_code',
           'liquid_tags.notebook']

# This header file is automatically generated by the notebook plugin
if not os.path.exists('_nb_header.html'):
    import warnings
    warnings.warn("_nb_header.html not found. "
                  "Rerun make html to finalize build.")
else:
    EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')

GITHUB_USERNAME = 'jmetzen'
GITHUB_REPO_COUNT= 5
GITHUB_SKIP_FORK= False
GITHUB_SHOW_USER_LINK= False
#GITHUB_AUTH_TOKEN = os.environ.get('GITHUB_AUTH_TOKEN')
#if GITHUB_AUTH_TOKEN is None:
#    raise NotImplementedError("You should define GITHUB_AUTH_TOKEN in your OS's environment.")

# Search
SEARCH_BOX = True

# Sharing
GOOGLE_PLUS_ID = "114354937594844867963"
GOOGLE_PLUS_ONE = True
GOOGLE_PLUS_HIDDEN = False
