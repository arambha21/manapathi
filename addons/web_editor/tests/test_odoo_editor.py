# -*- coding: utf-8 -*-
# Part of Manapathi. See LICENSE file for full copyright and licensing details.

import manapathi.tests

@manapathi.tests.tagged("post_install", "-at_install")
class TestManapathiEditor(manapathi.tests.HttpCase):

    def test_manapathi_editor_suite(self):
        self.browser_js('/web_editor/tests', "", "", login='admin', timeout=1800)
