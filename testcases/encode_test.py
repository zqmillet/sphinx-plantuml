from textwrap import dedent

from pytest import mark

from sphinxcontrib.plantuml.encode import encode

@mark.parametrize(
    'text, encoded_text', [
        (
            dedent(
                '''
                Alice -> Bob: Authentication Request
                Bob --> Alice: Authentication Response
                '''
            ).strip(),
            'Syp9J4vLqBLJSCfFib9mB2t9ICqhoKnEBCdCprC8IYqiJIqkuGBAAUW2rJY256DHLLoGdrUS2W0='
        ),
        (
            dedent(
                '''
                @startuml
                Alice->Bob : I am using hex
                @enduml
                '''
            ).strip(),
            'SoWkIImgAStDuNBCoKnErRLpoazIi5BmL4ZCLIWjpinBLyX8hU1oICrB0Qe100=='
        ),
        (
            '',
            '0m0='
        )
    ]
)
def test_encode(text, encoded_text):
    assert encode(text) == encoded_text
