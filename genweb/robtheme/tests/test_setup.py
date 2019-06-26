# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from genweb.robtheme.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of genweb.robtheme into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if genweb.robtheme is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('genweb.robtheme'))

    def test_uninstall(self):
        """Test if genweb.robtheme is cleanly uninstalled."""
        self.installer.uninstallProducts(['genweb.robtheme'])
        self.assertFalse(self.installer.isProductInstalled('genweb.robtheme'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that IGenwebRobthemeLayer is registered."""
        from genweb.robtheme.interfaces import IGenwebRobthemeLayer
        from plone.browserlayer import utils
        self.failUnless(IGenwebRobthemeLayer in utils.registered_layers())
