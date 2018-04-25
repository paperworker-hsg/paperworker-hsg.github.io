#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = '종이접는 사회사업가'
SITENAME = '종이접는 사회사업가'
SITEURL = 'https://paperworker-hsg.github.io'

PATH = 'content'

ABOUT_ME = 'PaperWorker =<br>Paper + Social Work'
AVATAR = 'images/pwAvatar.png'

TIMEZONE = 'Asia/Seoul'
DEFAULT_LANG = 'ko'
DEFAULT_DATE_FORMAT = '%Y년 %m월 %d일 %A'

THEME = 'theme/pelican-bootstrap3'
CUSTOM_CSS = 'static/custom.css'
STATIC_PATHS = ['images', 'extra/custom.css']
EXTRA_PATH_METADATA = {'extra/custom.css': {'path': 'static/custom.css'}}

ARTICLE_URL = '{category}/{slug}'
ARTICLE_SAVE_AS = '{category}/{slug}.html'

USE_FOLDER_AS_CATEGORY = True

PLUGIN_PATHS = ['plugins/']
PLUGINS = ['i18n_subsites']

DISQUS_SITENAME = 'https-paperworker-hsg-github-io'
ADDTHIS_PROFILE = '5ae00816a4f2ac96'
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = 'feeds/%s.atom.xml'
AUTHOR_FEED_RSS = 'feeds/%s.rss.xml'

# Blogroll
LINKS = (('사회복지 정보원', 'http://cafe.daum.net/cswcamp'),
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
