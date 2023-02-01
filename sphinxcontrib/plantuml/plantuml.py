"""
this module provides the directive excel.
"""

from typing import List
from docutils.parsers.rst import directives
from docutils.parsers.rst.directives.images import Figure
from docutils.statemachine import StringList
from sphinx.util.docutils import SphinxDirective

from .encode import encode

def parse_figure_format(argument):
    """
    this function is used to parse overflow parameter.
    """
    return directives.choice(argument, ('svg', 'png'))

class PlantUMLDirective(Figure, SphinxDirective):
    """
    an environment for figure
    """
    required_arguments = 0

    option_spec = {
        **Figure.option_spec,
        'caption': directives.unchanged,
        'format': parse_figure_format,
    }

    def run(self) -> List:
        """
        render this environment
        """
        uml = '\n'.join(self.content)
        image_type = self.options.get('format', 'svg')

        url = f'https://www.plantuml.com/plantuml/{image_type}/{encode(uml)}'
        self.arguments = [url]

        if 'caption' in self.options:
            self.content = StringList([self.options['caption']])
        else:
            self.content = StringList()
        return super().run()
