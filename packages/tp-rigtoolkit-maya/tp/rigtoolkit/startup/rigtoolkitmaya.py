import os
import sys
import inspect

from Qt.QtWidgets import QApplication

from tp.core import log
from tp.bootstrap.core import manager, exceptions as bootstrap_exceptions
from tp.common.python import path

from tp.rigtoolkit.maya.plugins import loader

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

	logger.info('Loadding tp-rigtoolkit-maya package...')

	# Make sure QApplication instance exists before registering resources
	app = QApplication.instance() or QApplication(sys.argv)
	resources_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'maya', 'resources')
	resources.register_resource(resources_path, key='tp-rigtoolkit-maya')


	logger.info('Loading tpRigToolkit Maya plugins...')
	loader.load_all_rigtoolkit_plugins()


def shutdown(package_manager):
	"""
	Shutdown function that is called during tpDcc framework shutdown.
	This function is called at the end of tpDcc framework shutdown.
	"""

	logger.info('Shutting down tp-rigtoolkit-maya package...')

	logger.info('Unloading tpRigToolkit Maya plugins...')
	loader.unload_all_rigtoolkit_plugins()
