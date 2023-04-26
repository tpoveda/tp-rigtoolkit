#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains utils functions related with Ziva plugin
"""

from tp.core import dcc

PLUGIN_NAME = 'ziva'


def load_ziva_plugin():
    if not is_ziva_plugin_loaded():
        dcc.load_plugin(PLUGIN_NAME, quiet=True)

    return is_ziva_plugin_loaded()


def is_ziva_plugin_loaded():
    return dcc.is_plugin_loaded(PLUGIN_NAME)
