# -*- coding: utf-8 -*-
"""
/***************************************************************************
 TestMtdt
                                 A QGIS plugin
 Insert fish occurrence data to NOFA DB
                              -------------------
        begin                : 2017-01-09
        git sha              : $Format:%H$
        copyright            : (C) 2017 by NINA
        contributors         : stefan.blumentrath@nina.no
                               matteo.destefano@nina.no
                               jakob.miksch@nina.no
                               ondrej.svoboda@nina.no
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os
import unittest
import logging
import ConfigParser

LOGGER = logging.getLogger('QGIS')


class TestMtdt(unittest.TestCase):
    """Test for plugin metadata."""

    def shortDescription(self):
        """
        Method that overrides default behaviour
        and allows printing multiline test description.
        """

        return self._testMethodDoc

    def test_mtdt(self):
        """Tests that the plugin metadata contains mandatory information."""

        mand_mtdt = [
            'name',
            'description',
            'version',
            'qgisMinimumVersion',
            'email',
            'author']

        mtdt_fp = os.path.abspath(os.path.join(
            os.path.dirname(__file__), os.pardir, 'metadata.txt'))
        LOGGER.info('metadata file path: "{}"'.format(mtdt_fp))

        parser = ConfigParser.ConfigParser()
        parser.optionxform = str
        parser.read(mtdt_fp)

        sxn_name = 'general'
        msg = 'Cannot find section "{}" in "{}"'.format(sxn_name, mtdt_fp)

        assert parser.has_section(sxn_name), msg

        mtdt = dict(parser.items(sxn_name))
        LOGGER.info('metadata in section "{}": "{}"'.format(sxn_name, mtdt))

        for exp_mtdt in mand_mtdt:
            msg = (
                'Cannot find metadata "{}" in section "{}" of "{}".'
                .format(exp_mtdt, sxn_name, mtdt_fp))

            self.assertIn(exp_mtdt, mtdt, msg)

if __name__ == '__main__':
    unittest.main()
