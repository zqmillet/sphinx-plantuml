"""
this is the setup of this package.
"""

from setuptools import setup

from sphinxcontrib.excel import __version__

with open('sphinxcontrib/requirements.txt', 'r', encoding='utf8') as file:
    install_requires = list(map(lambda x: x.strip(), file.readlines()))

with open('readme.md', 'r', encoding='utf8') as file:
    long_description = file.read()

setup(
    name='sphinx-excel',
    version='.'.join(map(str, __version__)),
    author='kinopico',
    author_email='zqmillet@qq.com',
    url='https://github.com/zqmillet/sphinx-excel',
    description='an extension for sphinx to display excel table in sphinx documents',
    packages=['sphinxcontrib.excel'],
    install_requires=install_requires,
    long_description=long_description,
    long_description_content_type='text/markdown',
    include_package_data=True,
    namespace_packages=["sphinxcontrib"],
)
