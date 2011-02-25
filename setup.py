from distutils.core import setup
from setuptools import find_packages, setup

setup(
	name='django_block_manager',
	version='0.1dev',
	maintainer = "Zenobius Jiricek",
	maintainer_email = "airtonix@gmail.com",
	url="airtonix.net/projects/markdown-qrcode",
	description = "A package to help automate creation of testing in Django",
	long_description=open('README.md').read(),
	license='LICENSE.md',
	packages=find_packages(exclude='tests'),
	include_package_data = True
)

