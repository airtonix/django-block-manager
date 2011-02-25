from distutils.core import setup
from setuptools import find_packages, setup
setup(
	name='django_block_manager',
	version='0.0.1dev',
	maintainer = "Zenobius Jiricek",
	maintainer_email = "airtonix@gmail.com",
	url="airtonix.net/projects/markdown-qrcode",
	description = "Simple Django per-application block content template 'thingo'.",
	license='LICENSE.md',
	packages=find_packages(exclude='tests'),
	include_package_data = True
)

