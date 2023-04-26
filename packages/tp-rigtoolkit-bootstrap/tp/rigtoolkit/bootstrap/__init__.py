#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Initialization module for tp-rigtookit-bootstrap
"""

import os
import sys
from distutils.util import strtobool

from tp.bootstrap import log
from tp.bootstrap.utils import env

logger = log.bootstrapLogger

_RIGTOOLKIT_PACKAGE_MANAGER = None


def init(**kwargs):
	"""
	Initializes tp-rigtoolkit packages manager.

	:param dict kwargs: keyword arguments.
	:return: tp-dcc Package Manager instance.
	:rtype: tpDccPackagesManager
	"""

	global _RIGTOOLKIT_PACKAGE_MANAGER

	# First we make sure tp-rigtoolkit framework is initialized
	import tp.bootstrap
	tpdcc_package_manager = tp.bootstrap.init()
	if not tpdcc_package_manager:
		logger.error('tp-dcc framework was not initialized!')
		return None

	dev = bool(strtobool(os.getenv('TPRIGTOOLKIT_ENV_DEV', 'False')))
	deps_path = kwargs.get('dependencies_path', None) or os.getenv('TPRIGTOOLKIT_DEPS_ROOT', None)

	# register dependency paths
	if deps_path and os.path.isdir(deps_path):
		py_folder = 'py2' if env.is_python2() else 'py3'
		py_deps_folders = [
			os.path.join(deps_path, env.application(), py_folder),
			os.path.join(deps_path, env.application()),
			os.path.join(deps_path, py_folder),
		]
		for dep_folder in py_deps_folders:
			if not os.path.isdir(dep_folder) or dep_folder in sys.path:
				continue
			logger.debug(f'Dependencies Path {dep_folder} registered into sys.path.successfully!')
			sys.path.insert(0, dep_folder)

		if deps_path not in sys.path:
			sys.path.append(deps_path)

	# import here to make sure that bootstrapping vendor paths are already included within sys.path
	from tp.bootstrap.core import consts, manager

	root_path = kwargs.get('root_path', None) or os.getenv('TPRIGTOOLKIT_TOOLS_ROOT', None)
	root_path = root_path or os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
	packages_folder_path = kwargs.get('packages_folder_path', '')
	package_version_file = kwargs.get('package_version_file', '')
	custom_sys_paths = kwargs.get('custom_sys_paths', list())

	logger.debug('Bootstrap init paths:')
	logger.debug(f'\tPackages Root Path: {root_path}')
	logger.debug(f'\tDependencies Root Path: {root_path}')
	logger.debug(f'\tPackages Folder Path: {packages_folder_path}')
	logger.debug(f'\tPackages Version File Path: {package_version_file}')
	logger.debug(f'\tCustom Sys Paths: {custom_sys_paths}')

	logger.debug('Registering packages paths into sys.path ...')
	packages_paths = list()
	packages_paths.extend(custom_sys_paths)

	logger.debug(f'Registering follow package paths into sys.path: {packages_paths}')
	for package_path in packages_paths:
		if package_path and os.path.isdir(package_path) and package_path not in sys.path:
			sys.path.append(package_path)
			logger.debug(f'Package Path {package_path} registered into sys.path.successfully!')

	# setup environment variables related with tp-dcc boostrap
	if packages_folder_path and os.path.isdir(packages_folder_path):
		os.environ[consts.PACKAGES_FOLDER_PATH] = packages_folder_path
	if package_version_file:
		os.environ[consts.TPDCC_PACKAGE_VERSION_FILE] = package_version_file
	logger.debug('Setting up environment variables related with bootstrapping process ...')
	logger.debug(f'\t{consts.PACKAGES_FOLDER_PATH}: {os.environ.get(consts.PACKAGES_FOLDER_PATH, "")}')
	logger.debug(f'\t{consts.TPDCC_PACKAGE_VERSION_FILE}: {os.environ.get(consts.TPDCC_PACKAGE_VERSION_FILE, "")}')

	# create package manager and resolve (initialize) packages
	logger.debug('Creating tp-rigtoolkit framework environment ...')
	logger.debug(f'\tRoot Path: {root_path}')
	logger.debug(f'\tDev Mode: {dev}')
	current_env = manager.get_package_manager_from_path(root_path, dev=dev)
	logger.debug(f'Created tp-rigtoolkit environment instance: {current_env}')
	logger.debug('Resolving tp-rigtoolkit environment:')
	logger.debug(f'\tResolver: {current_env.resolver}')
	logger.debug(f'\tEnvironment configuration file: {current_env.resolver.get_environment_path()}')
	current_env.resolver.resolve_from_path(current_env.resolver.get_environment_path())
	_RIGTOOLKIT_PACKAGE_MANAGER = current_env

	# Make sure we set active package manager to tp-rigtoolkit
	manager.set_current_package_manager(tpdcc_package_manager)

	return current_env


def shutdown():

	global _RIGTOOLKIT_PACKAGE_MANAGER

	# import here to make sure that bootstrapping vendor paths are already included within sys.path
	from tp import bootstrap

	if not _RIGTOOLKIT_PACKAGE_MANAGER:
		logger.debug('No tp-rigtoolkit framework environment found to set shutdowon')
		return False

	logger.debug(f'Shutting down tp-rigging framework environment: {_RIGTOOLKIT_PACKAGE_MANAGER}')
	logger.debug(f'\tRoot Path: {_RIGTOOLKIT_PACKAGE_MANAGER.root_path}')
	logger.debug(f'\tDev: {_RIGTOOLKIT_PACKAGE_MANAGER.is_dev()}')

	_RIGTOOLKIT_PACKAGE_MANAGER.shutdown()

	bootstrap.shutdown()
