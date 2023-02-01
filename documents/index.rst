sphinx-plantuml 简介
====================

PlantUML 是可以用纯文本语言绘制图表的开源软件. PlantUML 支持许多统一建模语言的图, 也支持其他软件开发相关的格式/C4 模型/电脑网络图/ER 模型/甘特图/心智图和工作分解结构, 也可以用在 JSON 及 YAML 文档的可视化.

可以使用 `sphinx-contrib/plantuml <https://github.com/sphinx-contrib/plantuml/>`_ 在 Sphinx 文档中插入 PlantUML 图片. 但是构建环境需要配置 Java 以及 PlantUML 相关 jar 包. sphinx-plantuml 库是一个纯 Python 库, 不依赖其他组件, 对开发环境更友好.

sphinx-plantuml 安装
====================

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

sphinx-plantuml 使用
====================

.. plantuml::
    :align: center
    :caption: 内嵌 HTML

    @startuml
    skinparam backgroundColor transparent
    :* You can change <color:red>text color</color>
    * You can change <back:cadetblue>background color</back>
    * You can change <size:18>size</size>
    * You use <u>legacy</u> <b>HTML <i>tag</i></b>
    * You use <u:red>color</u> <s:green>in HTML</s> <w:#0000FF>tag</w>
    ----
    * image x0.5 : <img:http://plantuml.com/logo3.png{scale=0.5}>
    ----
    * image x1.5 : <img:http://plantuml.com/logo3.png{scale=1.5}>
    ;
    @enduml

.. plantuml::
    :align: center
    :caption: AWS 示例

    @startuml
    skinparam backgroundColor transparent


    !includeurl <aws/common.puml>
    !includeurl <aws/ApplicationServices/AmazonAPIGateway/AmazonAPIGateway.puml>
    !includeurl <aws/Compute/AWSLambda/AWSLambda.puml>
    !includeurl <aws/Compute/AWSLambda/LambdaFunction/LambdaFunction.puml>
    !includeurl <aws/Database/AmazonDynamoDB/AmazonDynamoDB.puml>
    !includeurl <aws/Database/AmazonDynamoDB/table/table.puml>
    !includeurl <aws/General/AWScloud/AWScloud.puml>
    !includeurl <aws/General/client/client.puml>
    !includeurl <aws/General/user/user.puml>
    !includeurl <aws/SDKs/JavaScript/JavaScript.puml>
    !includeurl <aws/Storage/AmazonS3/AmazonS3.puml>
    !includeurl <aws/Storage/AmazonS3/bucket/bucket.puml>

    skinparam componentArrowColor Black
    skinparam componentBackgroundColor White
    skinparam nodeBackgroundColor White
    skinparam agentBackgroundColor White
    skinparam artifactBackgroundColor White


    USER(user)
    CLIENT(browser)
    JAVASCRIPT(js,SDK)

    AWSCLOUD(aws) {

        AMAZONS3(s3) {
            BUCKET(site,www.insecurity.co)
            BUCKET(logs,logs.insecurity.co)
        }

        AMAZONAPIGATEWAY(api)

        AWSLAMBDA(lambda) {
            LAMBDAFUNCTION(addComments,addComments)
        }

        AMAZONDYNAMODB(dynamo) {
            TABLE(comments,Comments)
        }
    }

    user - browser

    browser -d-> site :**1a**) get\nstatic\ncontent
    site ~> logs :1a
    site .u.> browser :**1b**
    browser - js
    js -r-> comments :**2a**) get\ncomments
    comments ..> js :**2b**

    js -r-> api :**3**) add\ncomment

    api -d-> addComments :**4**

    addComments -> comments :**5**

    comments ..> js :**6**) new\ncomments
    @enduml

.. plantuml::
    :caption: C4 模型示例
    :format: svg
    :align: center

    @startuml
    !include <c4/C4_Context.puml>
    skinparam backgroundColor transparent

    'ref http://plantuml.com/stdlib
    !include <office/Users/user.puml>
    !include <office/Users/mobile_user.puml>

    'LAYOUT_WITH_LEGEND

    title System Context diagram for Internet Banking System

    Person(customer  , Customer , "<$user> <$mobile_user>\n A customer of the bank, with personal bank accounts" )

    System(banking_system, "Internet Banking System", "Allows customers to view information about their bank accounts, and make payments.")

    System_Ext(mail_system, "E-mail system", "The internal Microsoft Exchange e-mail system.")
    System_Ext(mainframe, "Mainframe Banking System", "Stores all of the core banking information about customers, accounts, transactions, etc.")

    Rel(customer, banking_system, "Uses")
    Rel_Back(customer, mail_system, "Sends e-mails to")
    Rel_Neighbor(banking_system, mail_system, "Sends e-mails", "SMTP")
    Rel(banking_system, mainframe, "Uses")
    @enduml
