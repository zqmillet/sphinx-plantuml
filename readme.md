# sphinx-plantuml <img src = "./documents/statics/logo.png" height = 120 align="right">

[![sphinx-plantuml](https://img.shields.io/badge/pypi-sphinx--plantuml-brightgreen)](https://pypi.org/project/sphinx-plantuml/)
[![Documentation Status](https://readthedocs.org/projects/sphinx-plantuml/badge/?version=latest)](https://sphinx-plantuml.readthedocs.io/en/latest/?badge=latest)
![pytest](https://github.com/zqmillet/sphinx-plantuml/actions/workflows/pytest.yml/badge.svg)
![mypy](https://github.com/zqmillet/sphinx-plantuml/actions/workflows/mypy.yml/badge.svg)
![flake8](https://github.com/zqmillet/sphinx-plantuml/actions/workflows/flake8.yml/badge.svg)
![pytest](https://github.com/zqmillet/sphinx-plantuml/actions/workflows/pytest.yml/badge.svg)

## introduction

sphinx-plantuml can render PlantUML figure in your Sphinx document without any dependencies in an instant

## installation

you can install sphinx-plantuml by `pip`.

``` bash
python3 -m pip install sphinx-plantuml
```

## setup

please add `sphinxcontrib.plantuml` into your `conf.py` file.

``` python
extensions = [
    'sphinxcontrib.plantuml',
]
```

## usage

you can use the following code to insert a figure into your document.

``` rest
.. plantuml::

    @startuml
    Alice -> Bob: test
    @enduml
```

sphinx-plantuml renders the figure in `.svg` format, if you want `.png` format, you can use `:format:` argument.

``` rest
.. plantuml::
    :format: png

    @startuml
    Alice -> Bob: test
    @enduml
```

if you want add a caption, you can use `:caption:` argument.

``` rest
.. plantuml::
    :caption: this is caption

    @startuml
    Alice -> Bob: test
    @enduml
```

sphinx-plantuml directive can load PlantUML code from file.

``` rest
.. plantuml:: /the/path/of/file.uml
    :caption: this is caption
```

sphinx-plantuml directive supports almost all arguments of sphinx builtin figure directive. for example, you can use `:align:` argument to control the layout of the figure.

``` rest
.. plantuml:: /the/path/of/file.uml
    :caption: this is caption
    :align: center
```
