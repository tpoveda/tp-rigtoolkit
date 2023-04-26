#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains tp-dcc-core startup functionality
"""

import os
import sys
import inspect

from Qt.QtWidgets import QApplication

from tp.bootstrap import log
from tp.bootstrap.core import manager, exceptions as bootstrap_exceptions
from tp.core.managers import resources
from tp.common.python import path

logger = log.tpLogger


def startup(package_manager):
	"""
	This function is automatically called by tpDcc packages Manager when environment setup is initialized.

	:param package_manager: current tpDcc packages Manager instance.
	:return: tpDccPackagesManager
	"""

	root_file_path = path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
	package = manager.get_package_from_path(root_file_path)
	if not package:
		raise bootstrap_exceptions.MissingPackage(package)

	logger.info('Loading tp-rigtoolkit-core package...')

	# Make sure QApplication instance exists before registering resources
	app = QApplication.instance() or QApplication(sys.argv)
	resources_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'core', 'resources')
	resources.register_resource(resources_path, key='tp-rigtoolkit-core')
