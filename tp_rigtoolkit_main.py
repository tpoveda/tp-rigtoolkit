import os
import sys

# register environment variables
os.environ['TPDCC_ENV_DEV'] = 'True'
os.environ['TPDCC_TOOLS_ROOT'] = r'E:\tools\dev\tp-dcc\packages\tp-dcc-bootstrap'
os.environ['TPDCC_DEPS_ROOT'] = r'E:\tools\dev\tp-dcc\venv\Lib\site-packages'
os.environ['TRIGTOOLKIT_ENV_DEV'] = os.environ['TPDCC_ENV_DEV']
os.environ['TPRIGTOOLKIT_TOOLS_ROOT'] = r'E:\tools\dev\tp-rigtoolkit\packages\tp-rigtoolkit-bootstrap'

# make sure to update sys.path so tpDcc Tools package manager an dependencies are available
root_paths = [os.environ['TPDCC_TOOLS_ROOT'], os.environ['TPRIGTOOLKIT_TOOLS_ROOT']]
for root_path in root_paths:
	if os.path.isdir(root_path) and root_path not in sys.path:
		sys.path.append(root_path)


def reload_modules():
	"""
	Function that forces the reloading of all related modules
	"""

	modules_to_reload = ('tp')
	for k in sys.modules.copy().keys():
		found = False
		for mod in modules_to_reload:
			if mod == k:
				del sys.modules[mod]
				found = True
				break
		if found:
			continue
		if k.startswith(modules_to_reload):
			del sys.modules[k]


import tp.rigtoolkit.bootstrap

try:
	tp.rigtoolkit.bootstrap.shutdown()
except Exception:
	pass
reload_modules()

# register environment variables after shutdown
os.environ['TPDCC_DEV'] = 'True'
os.environ['TRIGTOOLKIT_ENV_DEV'] = os.environ['TPDCC_ENV_DEV']

# load framework
import tp.rigtoolkit.bootstrap

tp.rigtoolkit.bootstrap.init()
