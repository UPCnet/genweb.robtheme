# -*- coding: utf-8 -*-
from Products.CMFPlone.interfaces import IPloneSiteRoot

from plone import api
from five import grok

from genweb.robtheme.interfaces import IGenwebRobthemeLayer


class removeTemplatesRobTheme(grok.View):
    grok.name('remove_templates_robtheme')
    grok.context(IPloneSiteRoot)
    grok.layer(IGenwebRobthemeLayer)
    grok.require('cmf.ManagePortal')

    def render(self):
        portal = api.portal.get()
        templates = portal.get('templates', None)
        if templates:
            for template in templates:
                if template.startswith('rob-theme-'):
                    templates.manage_delObjects([template])
        return 'Done'
