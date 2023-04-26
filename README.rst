tp-rigtoolkit
============================================================

.. image:: https://img.shields.io/badge/Python-3.7-yellow?logo=python
    :target: https://www.python.org/

.. image:: https://img.shields.io/badge/Windows-blue?logo=windows
    :target: https://www.python.org/

.. image:: https://img.shields.io/badge/code_style-pep8-blue
    :target: https://www.python.org/dev/peps/pep-0008/

.. image:: https://img.shields.io/badge/Maya-2022-green?logo=autodesk
    :target: https://www.autodesk.com/

.. image:: https://img.shields.io/badge/Maya-2023-green?logo=autodesk
    :target: https://www.autodesk.com/

.. image:: https://img.shields.io/static/v1?message=UE5&color=000000&logo=unrealengine&logoColor=white&label=
    :target: https://www.unreal.com/

.. image:: https://img.shields.io/static/v1?message=Houdini&color=FF4713&logo=Houdini&logoColor=FFFFFF&label=
    :target: https://www.houdini.com/

============================================================

Framework that allows to streamline the rigging process in different DCCs

Packages
============================================================

* **tp-rigtoolkit-bootstrap**: Package that handles the initialization of the tp-rigtoolkit framework and all their packages.
* **tp-rigtoolkit-core**: Package that contains a collection of Python modules with generic rigging classes and functions.
* **tp-rigtoolkit-maya**: Package that contains a collection of Python modules to streamline the rigging workflow in Maya.
* **tp-rigtoolkit-unreal**: Package that contains a collection of Python modules to streamline the rigging workflow in Unreal Engine.
* **tp-rigtoolkit-houdini**: Package that contains a collection of Python modules to streamline the rigging workflow in Houdini.

Requirements
============================================================

* Make sure **Python 3.X** is installed in your machine.

    .. note::
        Scripts expect to find Python executables in their default locations:
            * **Python 3**: C:\Python3X

        You can edit **setup_venv_py.bat** if you want to use custom Python installation directory.

* Make sure **virtualenv** is installed:

      .. code-block::

            pip install virtualenv


* Make **Git** client is installed : https://git-scm.com/


How to use
============================================================

1. Run **setup_venv_py.bat**: to create virtual environment for Python 3.

2. Execute **tp_rigtoolkit_main.py** in your favorite Python DCC editor to load tp-rigtoolkit framework.