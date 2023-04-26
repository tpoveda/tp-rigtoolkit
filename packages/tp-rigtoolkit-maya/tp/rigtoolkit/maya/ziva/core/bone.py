#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains functions to work with Ziva bones
"""

import maya.cmds as cmds
import maya.mel as mel


def is_bone(mesh):
    """
    Returns whether given mesh is a Ziva Bone mesh or not
    :param mesh: str, name of a mesh node
    :return: bool
    """

    cmds.select(clear=True)
    cmds.select(mesh)
    ziva_tissue = mel.eval('zQuery -type "zBone"')
    if not ziva_tissue:
        return False

    return True
