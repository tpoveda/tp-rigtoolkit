import os
import inspect

from tp.core import log
from tp.bootstrap.core import manager, exceptions as bootstrap_exceptions
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

	logger.info('Loadding tp-rigtoolkit-houdini package...')


def shutdown(package_manager):
	"""
	Shutdown function that is called during tpDcc framework shutdown.
	This function is called at the end of tpDcc framework shutdown.
	"""
	logger.info('Shutting down tp-rigtoolkit-houdini package...')
