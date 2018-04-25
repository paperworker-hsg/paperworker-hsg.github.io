#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = '종이접는 사회사업가'
SITENAME = '종이접는 사회사업가'
SITEURL = '.'

PATH = 'content'

TIMEZONE = 'Asia/Seoul'

DEFAULT_LANG = 'ko'

THEME = 'theme/pelican-bootstrap3'

PLUGIN_PATHS = ['plugins/']
PLUGINS = ['i18n_subsites']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = 'feeds/%s.atom.xml'
AUTHOR_FEED_RSS = 'feeds/%s.rss.xml'

# Blogroll
LINKS = (('사회복지 정보원', 'http://www.welfare.or.kr'),
         ('사회복지사 사무소 구슬', 'http://cafe.daum.net/coolwelfare'),
         )

# Social widget
SOCIAL = (('Facebook', 'https://www.facebook.com/paperworker.hsg'),
          ('Instagram', 'https://www.instagram.com/paperworker.hsg/')
          ,)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#bootstrap3 seetings
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
I18N_TEMPLATES_LANG ='ko'
