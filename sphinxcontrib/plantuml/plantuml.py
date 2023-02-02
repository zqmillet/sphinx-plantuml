"""
this module provides the directive excel.
"""

from typing import List
from docutils.parsers.rst import directives
from docutils.parsers.rst.directives.images import Figure
from docutils.statemachine import StringList
from docutils.nodes import figure
from sphinx.util.docutils import SphinxDirective

from .encode import encode

def parse_figure_format(argument: str) -> str:
    """
    this function is used to parse overflow parameter.
    """
    return directives.choice(argument, ('svg', 'png'))

class PlantUMLDirective(Figure, SphinxDirective):
    """
    an environment for figure
    """
    required_arguments = 0
    optional_arguments = 1

    option_spec = {
        **Figure.option_spec,
        'caption': directives.unchanged,
        'format': parse_figure_format,
    }

    def get_uml(self) -> str:
        if not self.arguments:
            return '\n'.join(self.content)

        file_path, *_ = self.arguments  # type: ignore
        _, file_path = self.env.relfn2path(file_path)

        with open(file_path, 'r', encoding='utf8') as file:
            return file.read()

    def run(self) -> List[figure]:
        """
        render this environment
        """
        image_type = self.options.get('format', 'svg')

        url = f'https://www.plantuml.com/plantuml/{image_type}/{encode(self.get_uml())}'
        self.arguments = [url]

        if 'caption' in self.options:
            self.content = StringList([self.options['caption']])
        else:
            self.content = StringList()

        return super().run()
