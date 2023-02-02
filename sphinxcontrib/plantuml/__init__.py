"""
this is the package sphinxcontrib.plantuml.
"""
__version__ = (1, 0, 0)

from typing import Dict
from typing import Any
from sphinx.application import Sphinx

from .plantuml import PlantUMLDirective

def setup(application: Sphinx) -> Dict[str, Any]:
    """
    setup extension.
    """
    application.add_directive('plantuml', PlantUMLDirective)
    return {"version": __version__, "parallel_read_safe": True}
