# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.utils import normalizeString

from plone import api
from plone.app.contenttypes.behaviors.richtext import IRichText
from plone.dexterity.utils import createContentInContainer

from genweb.robtheme.browser.plantilles import get_plantilles


def setupRobTheme(context):
    # Ordinarily, GenericSetup handlers check for the existence of XML files.
    # Here, we are not parsing an XML file, but we use this text file as a
    # flag to check that we actually meant for this import step to be run.
    # The file is found in profiles/default.

    if context.readDataFile('genweb.robtheme.txt') is None:
        return

    portal = api.portal.get()

    templates = portal.get('templates', None)
    if templates:
        for plt in get_plantilles():
            plantilla = create_content(templates, 'Document', normalizeString(plt['titol']), title=plt['titol'], description=plt['resum'])
            plantilla.text = IRichText['text'].fromUnicode(plt['cos'])
            plantilla.reindexObject()


def create_content(container, portal_type, id, publish=True, **kwargs):
    if not getattr(container, id, False):
        obj = createContentInContainer(container, portal_type, checkConstraints=False, **kwargs)
        if publish:
            publish_content(obj)
    return getattr(container, id)


def publish_content(context):
        """ Make the content visible either in both possible genweb.simple and
            genweb.review workflows.
        """
        pw = getToolByName(context, "portal_workflow")
        object_workflow = pw.getWorkflowsFor(context)[0].id
        object_status = pw.getStatusOf(object_workflow, context)
        if object_status:
            api.content.transition(obj=context, transition={'genweb_simple': 'publish', 'genweb_review': 'publicaalaintranet'}[object_workflow])
