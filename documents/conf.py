from os.path import dirname
from sys import path

path.insert(0, dirname(dirname(__file__)))

author = 'kinopico'
project = 'the manual of sphinx-plantuml'
html_favicon = './statics/logo.png'

extensions = [
    'sphinxcontrib.plantuml',
]

numfig = True

html_theme = 'sphinx_rtd_theme'
source_suffix = ['.rst']
