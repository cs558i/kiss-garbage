#!/usr/bin/env python
# setup.py generated by flit for tools that don't yet use PEP 517

from distutils.core import setup

packages = \
['tg']

package_data = \
{'': ['*'], 'tg': ['resources/*']}

install_requires = \
['python-telegram==0.12.0']

entry_points = \
{'console_scripts': ['tg = tg.main:main']}

setup(name='tg',
      version='0.2.0',
      description='Terminal client for telegram',
      author='Paul Nameless',
      author_email='reacsdas@gmail.com',
      url='https://github.com/paul-nameless/tg',
      packages=packages,
      package_data=package_data,
      install_requires=install_requires,
      entry_points=entry_points,
      python_requires='>=3.8',
     )
