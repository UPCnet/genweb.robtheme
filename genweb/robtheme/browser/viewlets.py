# -*- coding: utf-8 -*-
from five import grok
from plone.app.layout.viewlets.interfaces import IPortalHeader

from genweb.robtheme.interfaces import IGenwebRobthemeLayer
from genweb.theme.browser.viewlets import gwHeader as gwHeader


class HeaderGWRobTheme(gwHeader):
    grok.name('robtheme.header')
    grok.viewletmanager(IPortalHeader)
    grok.template('header')
    grok.layer(IGenwebRobthemeLayer)
