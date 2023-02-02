sphinx-plantuml 简介
====================

PlantUML 是可以用纯文本语言绘制图表的开源软件. PlantUML 支持许多统一建模语言, 也支持其他软件开发相关的格式, 比如 C4 模型/电脑网络图/ER 模型/甘特图/心智图和工作分解结构图等, 也可以用在 JSON 及 YAML 文档的可视化.

在 Sphinx 中, 你可以使用 `sphinx-contrib/plantuml <https://github.com/sphinx-contrib/plantuml/>`_ 在文档中插入 PlantUML 图片. 但是构建环境需要配置 Java 以及 PlantUML 相关 jar 包, 配置起来比较麻烦. 此外, 本地编译也比较慢, 拖慢整个构建过程.

因此我开发了 sphinx-plantuml 库, sphinx-plantuml 的优点有:

- 纯 Python 库, 无需配置任何环境或者依赖, 开箱即用.
- 快速的构建速度, 因为构建过程无需编译 PlantUML.
- 兼容内置 ``figure`` 命令大部分参数, 容易上手.
- 支持 ``.uml`` 文件的引用, 便于项目管理.

sphinx-plantuml 原理
====================

sphinx-plantuml 工作原理如 :numref:`working_principle_figure` 所示.

.. _working_principle_figure:
.. plantuml::
    :caption: sphinx-plantuml 工作原理
    :align: center

    @startuml
    skinparam backgroundColor transparent

    start
    :读取 plantuml 命令中的代码 code;
    :利用 Deflate 算法对 code 进行压缩, 得到压缩后的字符串 compressed_code;
    :利用 https://plantuml.com 渲染 compressed_code;
    :输出到 Sphinx 文档中;
    stop
    @enduml

sphinx-plantuml 利用 https://plantuml.com 网站对 PlantUML 代码进行渲染. 构建的时候不需要渲染, 也不需要联网. 只有在文档被浏览时才会渲染, 因此浏览的时候需要联网. 由于是利用官方网站进行渲染, 因此构建环境无需配置 PlantUML 相关依赖.

sphinx-plantuml 安装
====================

使用 ``python3 -m pip install sphinx-plantuml`` 安装 sphinx-plantuml.

然后在你的 ``conf.py`` 文件中添加插件的引用, 如下代码所示.

.. code-block:: python

    extensions = [
        ...
        'sphinxcontrib.plantuml',
        ...
    ]

sphinx-plantuml 使用
====================

sphinx-plantuml 提供了 ``plantuml`` 命令. 你可以直接在 ``plantuml`` 中写 UML 语言, 比如 :numref:`plantuml_demo_1` 所示的 reST 代码.

.. _plantuml_demo_1:
.. code-block:: rest
    :caption: 可以直接 ``plantuml`` 环境中写 UML 代码

    .. plantuml::
        :align: center

        @startuml
        Alice -> Bob: test
        @enduml

其渲染结果如下图所示.

.. plantuml::
    :align: center
    :caption: :numref:`plantuml_demo_1` 渲染效果

    @startuml
    Alice -> Bob: test
    @enduml

sphinx-plantuml 默认将图片渲染成 ``.svg``, 如果你想渲染成 ``.png``, 可以使用 ``:format:`` 参数指定渲染格式, 比如 :numref:`plantuml_demo_2` 所示的 reST 代码.

.. _plantuml_demo_2:
.. code-block:: rest
    :caption: 指定图片渲染格式

    .. plantuml::
        :align: center
        :format: png

        @startuml
        Alice -> Bob: test
        @enduml

其渲染结果如下图所示.

.. plantuml::
    :align: center
    :format: png
    :caption: png 渲染效果

    @startuml
    Alice -> Bob: test
    @enduml

如果你想给图片添加标题, 可以使用 ``:caption:`` 参数指定标题, 如 :numref:`plantuml_demo_3` 所示的 reST 代码.

.. _plantuml_demo_3:
.. code-block:: rest
    :caption: 指定图片标题

    .. plantuml::
        :align: center
        :format: png
        :caption: 苟利国家生死以, 岂因祸福避趋之

        @startuml
        Alice -> Bob: test
        @enduml

其渲染结果如下图所示.

.. plantuml::
    :align: center
    :format: png
    :caption: 苟利国家生死以, 岂因祸福避趋之

    @startuml
    Alice -> Bob: test
    @enduml

Sphinx 内置的 ``figure`` 命令的大部分参数 ``plantuml`` 都支持, 比如你可以使用 ``:width:`` 参数来设置图片的大小, 如 :numref:`plantuml_demo_4` 所示.

.. _plantuml_demo_4:
.. code-block:: rest
    :caption: 指定图片宽度

    .. plantuml::
        :align: center
        :format: png
        :width: 50%

        @startuml
        Alice -> Bob: test
        @enduml

其渲染结果如下图所示.

.. plantuml::
    :align: center
    :format: png
    :width: 50%
    :caption: 50% 宽度的图片

    @startuml
    Alice -> Bob: test
    @enduml

.. note::

    不是所有的 ``figure`` 的参数都支持, 因为无法提前获取图片的尺寸, ``:scale:`` 参数就无法支持.

如果你的 PlantUML 代码是在另一个文件中, 可以采用如 :numref:`reference_code_file` 所示代码实现.

.. _reference_code_file:
.. code-block:: rest
    :caption: 引用 PlantUML 代码文件

    .. plantuml:: /umls/insert_html.uml
        :align: center
        :width: 50%
        :caption: 内嵌 HTML 示例

    .. plantuml:: /umls/aws_demo.uml
        :align: center
        :width: 50%
        :caption: AWS 示例

    .. plantuml:: /umls/c4_demo.uml
        :caption: C4 模型示例
        :format: svg
        :width: 50%
        :align: center

:numref:`reference_code_file` 中的代码的渲染效果如下所示.

.. plantuml:: /umls/insert_html.uml
    :align: center
    :width: 50%
    :caption: 内嵌 HTML 示例

.. plantuml:: /umls/aws_demo.uml
    :align: center
    :width: 50%
    :caption: AWS 示例

.. plantuml:: /umls/c4_demo.uml
    :caption: C4 模型示例
    :format: svg
    :width: 50%
    :align: center

其中三个 ``.uml`` 文件的下载链接如下:

- :download:`insert_html.uml </umls/insert_html.uml>`;
- :download:`aws_demo.uml </umls/aws_demo.uml>`;
- :download:`c4_demo.uml </umls/c4_demo.uml>`.
